from __future__ import annotations

import argparse
import re
from pathlib import Path

from workflow_schema import ANALYSIS_HEADINGS, DATA_ANALYSIS_HEADINGS, EVIDENCE_TABLE_HEADER, REQUIRED_SUBSTAGE_HEADINGS

ROOT = Path(__file__).resolve().parents[1]

FILLER_PHRASES = (
    "with the development of technology",
    "in today's fast-paced world",
    "businesses need to adapt",
    "this is very important",
    "as we all know",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'_-]*", text))


def status_of(text: str) -> str:
    match = re.search(r"^\s*-\s*Status:\s*([A-Z_]+)", text, flags=re.MULTILINE)
    return match.group(1) if match else "UNKNOWN"


def evidence_ids(text: str) -> set[str]:
    return set(re.findall(r"\bE\d+\b", text))


def analysis_body(text: str) -> str:
    match = re.search(r"## 6\. Analysis(?P<body>.*?)(?:\n## 7\.|\Z)", text, flags=re.DOTALL)
    return match.group("body") if match else ""


def confidence_rating(text: str) -> str | None:
    match = re.search(r"## 10\. Confidence Rating(?P<body>.*?)(?:\n## 11\.|\Z)", text, flags=re.DOTALL)
    if not match:
        return None
    body = match.group("body")
    for level in ("HIGH", "MEDIUM", "LOW", "SPECULATIVE"):
        if re.search(rf"\b{level}\b", body):
            return level
    return None


def evidence_rows(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.strip().startswith("| E")]


def validate_file(path: Path) -> list[str]:
    problems: list[str] = []
    text = read_text(path)
    for heading in REQUIRED_SUBSTAGE_HEADINGS:
        if heading not in text:
            problems.append(f"missing heading `{heading}`")
    status = status_of(text)
    if status == "COMPLETE":
        words = word_count(text)
        if words < 500:
            problems.append(f"COMPLETE substage has {words} words, expected at least 500")
        lower = text.lower()
        for phrase in FILLER_PHRASES:
            if phrase in lower:
                problems.append(f"contains filler phrase `{phrase}`")
        required_sections = ["## 4. Evidence Pack", "## 5. Source Log", "## 6. Analysis", "## 7. Scores", "## 8. Risks / Weak Points", "## 9. Output to Next Substage", "## 10. Confidence Rating", "## 11. Decision"]
        for section in required_sections:
            section_index = text.find(section)
            if section_index == -1:
                continue
            next_index = text.find("\n## ", section_index + 1)
            section_body = text[section_index: next_index if next_index != -1 else len(text)]
            if "TBD" in section_body or len(section_body.strip().splitlines()) < 3:
                problems.append(f"incomplete section `{section}`")
        if EVIDENCE_TABLE_HEADER not in text:
            problems.append("missing Evidence Pack table")
        if not evidence_rows(text):
            problems.append("missing evidence rows")
        if not evidence_ids(analysis_body(text)):
            problems.append("analysis does not reference evidence IDs")
        if confidence_rating(text) is None:
            problems.append("missing confidence rating")
        for heading in ANALYSIS_HEADINGS:
            if heading not in text:
                problems.append(f"missing analysis heading `{heading}`")
        if "### Data Analysis Checks" in text and "Required." in text:
            for heading in DATA_ANALYSIS_HEADINGS:
                if heading not in text:
                    problems.append(f"missing data-analysis heading `{heading}`")
    return problems


def iter_substage_files(root: Path) -> list[Path]:
    product_root = root / "products"
    files: list[Path] = []
    for product_dir in product_root.glob("product-*"):
        if not (product_dir / "workflow-state.md").exists():
            continue
        for path in product_dir.rglob("*.md"):
            try:
                text = read_text(path)
            except UnicodeDecodeError:
                continue
            if text.startswith("# Substage:"):
                files.append(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate meaningful substage reports.")
    parser.add_argument("path", nargs="?", help="Substage file to validate. If omitted, validates state-machine product substages.")
    args = parser.parse_args()

    targets = [Path(args.path).resolve()] if args.path else iter_substage_files(ROOT)
    if not targets:
        print("No state-machine substage files found.")
        return 0

    all_problems: list[str] = []
    for path in targets:
        problems = validate_file(path)
        for problem in problems:
            all_problems.append(f"{path}: {problem}")

    if all_problems:
        print("Meaningful substage validation failed:")
        for problem in all_problems:
            print(f"- {problem}")
        return 1

    print(f"Meaningful substage validation passed for {len(targets)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
