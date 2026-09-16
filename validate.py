#!/usr/bin/env python3
"""Repository validator for the Prompt & Agent Engineering Workshop.

Standard library only. Runs on Windows, macOS, and Linux with Python 3.8+.

Checks performed
----------------
1. schedule.json arithmetic: blocks are contiguous, sum to the declared total,
   and every block's segments are contiguous and sum to the block duration.
2. Timing agreement: every canonical range string appears in the artifacts that
   are required to quote it (README, facilitator guide, participant workbook).
3. Slide outline: 25-35 slides, sequential numbering, valid segment ids, and
   full coverage of every schedule id.
4. Machine-readable examples: .json parses, .jsonl parses line by line, .csv has
   a consistent column count, and .yaml files pass lightweight repository-safe checks.
5. The structured-output example satisfies the required fields and enums of the
   structured-output JSON Schema.
6. Markdown relative links resolve to files that exist in the repository.
7. Callout labels use only the approved vocabulary.

Usage
-----
    python validate.py            # from the repository root
    python validate.py --verbose
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

ALLOWED_OPTIONAL_LABELS = {
    "OPTIONAL — MICROSOFT FOUNDRY",
    "OPTIONAL — GITHUB COPILOT",
}

SKIP_DIRS = {".git", ".github/workflows"}

errors: list = []
warnings: list = []
checks_run = 0


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def read_text(relative_path: str) -> str:
    with open(os.path.join(ROOT, relative_path), "r", encoding="utf-8") as handle:
        return handle.read()


def iter_files(extension: str):
    for current_dir, dir_names, file_names in os.walk(ROOT):
        dir_names[:] = [d for d in dir_names if d != ".git"]
        for name in sorted(file_names):
            if name.lower().endswith(extension):
                full = os.path.join(current_dir, name)
                yield os.path.relpath(full, ROOT).replace("\\", "/")


def load_schedule() -> dict:
    global checks_run
    checks_run += 1
    path = os.path.join(ROOT, "schedule.json")
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, ValueError) as exc:
        print("ERROR: schedule.json could not be read as JSON: %s" % exc)
        raise SystemExit(1)


def check_schedule_math(schedule: dict) -> None:
    global checks_run
    checks_run += 1
    total = schedule["total_minutes"]
    blocks = schedule["blocks"]
    cursor = 0
    for block in blocks:
        if block["start"] != cursor:
            fail(
                "schedule.json: block '%s' starts at %s but the previous block ended at %s"
                % (block["id"], block["start"], cursor)
            )
        if block["end"] - block["start"] != block["duration"]:
            fail("schedule.json: block '%s' duration does not match start/end" % block["id"])
        if block["range"] != "%s-%s" % (block["start"], block["end"]):
            fail("schedule.json: block '%s' range string is inconsistent" % block["id"])
        cursor = block["end"]

        segments = block.get("segments") or []
        if segments:
            seg_cursor = block["start"]
            seg_total = 0
            for segment in segments:
                if segment["start"] != seg_cursor:
                    fail(
                        "schedule.json: segment '%s' starts at %s but previous segment ended at %s"
                        % (segment["id"], segment["start"], seg_cursor)
                    )
                if segment["end"] - segment["start"] != segment["duration"]:
                    fail("schedule.json: segment '%s' duration mismatch" % segment["id"])
                if segment["range"] != "%s-%s" % (segment["start"], segment["end"]):
                    fail("schedule.json: segment '%s' range string is inconsistent" % segment["id"])
                seg_cursor = segment["end"]
                seg_total += segment["duration"]
            if seg_total != block["duration"]:
                fail(
                    "schedule.json: segments of '%s' sum to %s minutes, expected %s"
                    % (block["id"], seg_total, block["duration"])
                )
            if seg_cursor != block["end"]:
                fail("schedule.json: segments of '%s' do not end at the block end" % block["id"])

    if cursor != total:
        fail("schedule.json: blocks end at minute %s, expected %s" % (cursor, total))

    session_blocks = [b for b in blocks if b["id"].startswith("session-")]
    for block in session_blocks:
        if block["duration"] != 75:
            fail("schedule.json: %s must be exactly 75 minutes" % block["id"])

    break_blocks = [b for b in blocks if b["id"] == "break"]
    if len(break_blocks) != 1 or break_blocks[0]["duration"] != 15:
        fail("schedule.json: exactly one 15 minute break block is required")

    outside = total - sum(b["duration"] for b in blocks if b["id"].startswith("session-")) - 15
    if outside != 15:
        fail("schedule.json: minutes outside the two sessions and the break must equal 15, found %s" % outside)


def check_timing_in_docs(schedule: dict) -> None:
    global checks_run
    readme = read_text("README.md")
    guide = read_text("facilitator-guide.md")
    workbook = read_text("participant-workbook.md")

    for block in schedule["blocks"]:
        checks_run += 1
        if block["range"] not in readme:
            fail("README.md is missing the canonical range '%s' for block '%s'" % (block["range"], block["id"]))
        if block["range"] not in guide:
            fail("facilitator-guide.md is missing the canonical range '%s'" % block["range"])
        for segment in block.get("segments") or []:
            checks_run += 1
            if segment["range"] not in guide:
                fail(
                    "facilitator-guide.md is missing the canonical range '%s' for segment '%s'"
                    % (segment["range"], segment["id"])
                )
            if segment.get("kind") == "activity" and segment["range"] not in workbook:
                fail(
                    "participant-workbook.md is missing the canonical range '%s' for activity '%s'"
                    % (segment["range"], segment["id"])
                )


def all_ids(schedule: dict) -> dict:
    ids = {}
    for block in schedule["blocks"]:
        ids[block["id"]] = block
        for segment in block.get("segments") or []:
            ids[segment["id"]] = segment
    return ids


def check_slides(schedule: dict) -> None:
    global checks_run
    checks_run += 1
    text = read_text("slides/slide-outline.md")
    ids = all_ids(schedule)

    headings = re.findall(r"^## Slide (\d+) — (.+)$", text, flags=re.MULTILINE)
    numbers = [int(number) for number, _ in headings]
    if not 25 <= len(numbers) <= 35:
        fail("slides/slide-outline.md has %s slides; 25-35 required" % len(numbers))
    if numbers != list(range(1, len(numbers) + 1)):
        fail("slides/slide-outline.md slide numbers are not sequential starting at 1")

    used = re.findall(r"^- Segment: `([a-z0-9-]+)`$", text, flags=re.MULTILINE)
    if len(used) != len(numbers):
        fail(
            "slides/slide-outline.md: %s slides but %s 'Segment:' lines"
            % (len(numbers), len(used))
        )
    for segment_id in used:
        if segment_id not in ids:
            fail("slides/slide-outline.md references unknown schedule id '%s'" % segment_id)

    timings = re.findall(r"^- Timing: minutes ([0-9]+-[0-9]+)$", text, flags=re.MULTILINE)
    if len(timings) != len(numbers):
        fail("slides/slide-outline.md: every slide needs exactly one 'Timing: minutes X-Y' line")
    for index, (segment_id, timing) in enumerate(zip(used, timings), start=1):
        if segment_id in ids and ids[segment_id]["range"] != timing:
            fail(
                "slides/slide-outline.md slide %s: timing '%s' does not match segment '%s' (%s)"
                % (index, timing, segment_id, ids[segment_id]["range"])
            )

    missing = sorted(
        {
            identifier
            for identifier, entry in ids.items()
            if not entry.get("segments")
        }
        - set(used)
    )
    if missing:
        fail("slides/slide-outline.md does not cover schedule ids: %s" % ", ".join(missing))

    notes = len(re.findall(r"^- Speaker notes:", text, flags=re.MULTILINE))
    if notes != len(numbers):
        fail("slides/slide-outline.md: every slide needs exactly one 'Speaker notes:' line")


def check_data_files() -> None:
    global checks_run
    for path in iter_files(".json"):
        checks_run += 1
        try:
            with open(os.path.join(ROOT, path), "r", encoding="utf-8") as handle:
                json.load(handle)
        except Exception as exc:  # noqa: BLE001 - reported to the user
            fail("%s is not valid JSON: %s" % (path, exc))

    for path in iter_files(".jsonl"):
        checks_run += 1
        with open(os.path.join(ROOT, path), "r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    json.loads(line)
                except Exception as exc:  # noqa: BLE001
                    fail("%s line %s is not valid JSON: %s" % (path, line_number, exc))

    for path in iter_files(".csv"):
        checks_run += 1
        with open(os.path.join(ROOT, path), "r", encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.reader(handle) if row]
        if not rows:
            fail("%s is empty" % path)
            continue
        width = len(rows[0])
        for index, row in enumerate(rows[1:], start=2):
            if len(row) != width:
                fail("%s row %s has %s columns, expected %s" % (path, index, len(row), width))

    for path in iter_files(".yaml"):
        checks_run += 1
        text = read_text(path)
        if "\t" in text:
            fail("%s contains a tab character; YAML requires spaces" % path)
        if text.strip() and not text.endswith("\n"):
            warn("%s does not end with a newline" % path)


def check_structured_output_example() -> None:
    global checks_run
    checks_run += 1
    schema_path = "exercises/03-structured-output.schema.json"
    example_path = "exercises/03-structured-output.example.json"
    schema = json.loads(read_text(schema_path))
    example = json.loads(read_text(example_path))

    required = schema.get("required", [])
    properties = schema.get("properties", {})
    for field in required:
        if field not in example:
            fail("%s is missing required field '%s'" % (example_path, field))
    for field, value in example.items():
        if field not in properties:
            if schema.get("additionalProperties") is False:
                fail("%s has field '%s' that the schema does not allow" % (example_path, field))
            continue
        spec = properties[field]
        if "enum" in spec and value not in spec["enum"]:
            fail("%s field '%s' value '%s' is not in the schema enum" % (example_path, field, value))
        expected_type = spec.get("type")
        type_map = {
            "string": str,
            "boolean": bool,
            "number": (int, float),
            "integer": int,
            "array": list,
            "object": dict,
        }
        if isinstance(expected_type, str) and expected_type in type_map:
            if expected_type == "number" and isinstance(value, bool):
                fail("%s field '%s' should be a number" % (example_path, field))
            elif not isinstance(value, type_map[expected_type]):
                fail("%s field '%s' should be of type %s" % (example_path, field, expected_type))


LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_markdown_links() -> None:
    global checks_run
    for path in iter_files(".md"):
        checks_run += 1
        text = read_text(path)
        base_dir = os.path.dirname(os.path.join(ROOT, path))
        for target in LINK_PATTERN.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = os.path.normpath(os.path.join(base_dir, clean))
            if not os.path.exists(resolved):
                fail("%s links to missing path '%s'" % (path, target))


OPTIONAL_PATTERN = re.compile(r"OPTIONAL\s*[—–-]+\s*[A-Z][A-Z0-9 ]*[A-Z]")


def check_callout_labels() -> None:
    global checks_run
    for path in iter_files(".md"):
        checks_run += 1
        text = read_text(path)
        for match in OPTIONAL_PATTERN.findall(text):
            normalized = re.sub(r"\s+", " ", match).strip()
            if normalized not in ALLOWED_OPTIONAL_LABELS:
                fail("%s uses non-standard callout label '%s'" % (path, normalized))
        for legacy in re.finditer(r"Azure AI Foundry", text):
            window = text[max(0, legacy.start() - 60):legacy.start()]
            if "formerly" not in window.lower():
                warn(
                    "%s mentions 'Azure AI Foundry' without a nearby 'formerly' qualifier"
                    % path
                )


def check_required_files() -> None:
    global checks_run
    required = [
        "README.md",
        "facilitator-guide.md",
        "participant-workbook.md",
        "train-the-trainer.md",
        "resources.md",
        "contingency-plan.md",
        "participant-preflight.md",
        "facilitator-materials.md",
        "schedule.json",
        "slides/slide-outline.md",
        "exercises/README.md",
        "governance/pr-checklist.md",
        "optional/foundry.md",
        "optional/github-copilot.md",
        ".github/CODEOWNERS",
        ".github/pull_request_template.md",
    ]
    for relative in required:
        checks_run += 1
        if not os.path.exists(os.path.join(ROOT, relative)):
            fail("required file missing: %s" % relative)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the workshop repository.")
    parser.add_argument("--verbose", action="store_true", help="print each check group as it runs")
    args = parser.parse_args()

    groups = [
        ("required files", check_required_files),
        ("data files", check_data_files),
        ("structured output example", check_structured_output_example),
        ("markdown links", check_markdown_links),
        ("callout labels", check_callout_labels),
    ]

    schedule = load_schedule()
    if args.verbose:
        print("checking schedule arithmetic")
    check_schedule_math(schedule)
    if args.verbose:
        print("checking timing agreement across artifacts")
    check_timing_in_docs(schedule)
    if args.verbose:
        print("checking slide outline")
    check_slides(schedule)

    for name, function in groups:
        if args.verbose:
            print("checking %s" % name)
        function()

    for message in warnings:
        print("WARNING: %s" % message)

    if errors:
        for message in errors:
            print("ERROR: %s" % message)
        print("\nFAILED: %s error(s), %s warning(s), %s checks run." % (len(errors), len(warnings), checks_run))
        return 1

    print("OK: %s checks run, 0 errors, %s warning(s)." % (checks_run, len(warnings)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
