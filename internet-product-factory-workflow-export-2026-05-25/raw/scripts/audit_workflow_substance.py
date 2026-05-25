from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "products"
INDEX = PRODUCTS / "_product-index.md"


STATUS_RE = re.compile(r"^\s*-\s*Status:\s*([A-Z_]+)", re.MULTILINE)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def product_id(path: Path) -> str:
    return path.name


def index_row(pid: str) -> list[str]:
    for line in read(INDEX).splitlines():
        if line.startswith(f"| {pid} "):
            return [cell.strip() for cell in line.strip("|").split("|")]
    return []


def index_status(pid: str) -> dict[str, str]:
    row = index_row(pid)
    if len(row) < 7:
        return {}
    return {
        "status": row[1],
        "stage": row[2],
        "classification": row[4],
        "q_gate": row[5],
        "ship": row[6],
    }


def is_complete(pid: str, product_dir: Path) -> bool:
    status = index_status(pid)
    state = read(product_dir / "workflow-state.md")
    haystack = " ".join([status.get("status", ""), status.get("ship", ""), state]).upper()
    return any(marker in haystack for marker in ("COMPLETE", "PUBLISHED", "LOCAL_READY"))


def md_files(product_dir: Path) -> list[Path]:
    files: list[Path] = []
    for stage_dir in product_dir.glob("[0-9][0-9]_*"):
        files.extend(path for path in stage_dir.rglob("*.md") if path.is_file())
    return files


def status_of(text: str) -> str:
    match = STATUS_RE.search(text)
    return match.group(1) if match else "UNKNOWN"


def core_python_files(repo: Path) -> list[Path]:
    if not repo.exists():
        return []
    ignored_parts = {"tests", "scripts", "__pycache__", ".venv", "venv"}
    files = []
    for path in repo.rglob("*.py"):
        if any(part in ignored_parts for part in path.parts):
            continue
        files.append(path)
    return files


def line_count(path: Path) -> int:
    return len(read(path).splitlines())


def fixture_files(repo: Path) -> list[Path]:
    if not repo.exists():
        return []
    files = []
    for folder_name in ("fixtures", "samples", "examples"):
        folder = repo / folder_name
        if folder.exists():
            files.extend(path for path in folder.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
    return files


def test_files(repo: Path) -> list[Path]:
    folder = repo / "tests"
    if not folder.exists():
        return []
    return [path for path in folder.rglob("test_*.py") if path.is_file()]


def artifact_language(repo: Path) -> bool:
    combined = "\n".join(
        read(path)
        for path in (
            repo / "README.md",
            repo / "launch-summary.md",
            repo / "readme-claim-check.md",
        )
    ).lower()
    artifact_terms = (
        "letter",
        "appeal",
        "packet",
        "filing",
        "calendar",
        ".ics",
        "patch",
        "diff",
        "decision record",
        "action plan",
        "checklist",
        "draft",
    )
    return any(term in combined for term in artifact_terms)


def audit_product(product_dir: Path, strict: bool) -> tuple[list[str], list[str]]:
    pid = product_id(product_dir)
    warnings: list[str] = []
    failures: list[str] = []
    complete = is_complete(pid, product_dir)
    status = index_status(pid)
    public = status.get("classification") == "PUBLIC_PRODUCT"

    files = md_files(product_dir)
    not_started = []
    tbd_heavy = []
    for path in files:
        text = read(path)
        if status_of(text) == "NOT_STARTED":
            not_started.append(path)
        if text.count("TBD") >= 5:
            tbd_heavy.append(path)

    if complete and not_started:
        message = f"{pid}: completed/published status but {len(not_started)} workflow markdown files remain Status: NOT_STARTED"
        warnings.append(message)
        if strict:
            failures.append(message)
    if complete and tbd_heavy:
        message = f"{pid}: completed/published status but {len(tbd_heavy)} workflow markdown files still contain heavy TBD residue"
        warnings.append(message)
        if strict:
            failures.append(message)

    repo = product_dir / "repo"
    core_files = core_python_files(repo)
    test_count = len(test_files(repo))
    fixture_count = len(fixture_files(repo))

    if public and repo.exists():
        if core_files:
            counts = sorted((line_count(path), path) for path in core_files)
            total = sum(count for count, _ in counts)
            largest_count, largest_path = counts[-1]
            largest_share = largest_count / max(total, 1)
            if len(core_files) <= 2 or largest_share >= 0.72:
                message = (
                    f"{pid}: core may be under-modularized "
                    f"({len(core_files)} core Python files; largest file {largest_path.relative_to(repo)} is {largest_share:.0%} of core LOC)"
                )
                warnings.append(message)
                if strict:
                    failures.append(message)
        else:
            warnings.append(f"{pid}: public product repo has no detected core Python files; verify stack-specific audit manually")

        if test_count < 3:
            message = f"{pid}: shallow test matrix risk ({test_count} test files)"
            warnings.append(message)
            if strict:
                failures.append(message)
        if fixture_count < 5:
            message = f"{pid}: shallow fixture/sample matrix risk ({fixture_count} files across fixtures/samples/examples)"
            warnings.append(message)
            if strict:
                failures.append(message)
        if not artifact_language(repo):
            message = f"{pid}: README/package does not clearly describe a user-ready artifact beyond report/dashboard output"
            warnings.append(message)
            if strict:
                failures.append(message)

    return warnings, failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Soft audit for workflow substance beyond file-existence validation.")
    parser.add_argument("products", nargs="*", help="Product IDs such as product-025. Defaults to all products.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when completed products have substance failures.")
    args = parser.parse_args()

    targets = args.products or [path.name for path in sorted(PRODUCTS.glob("product-*")) if path.is_dir()]
    all_warnings: list[str] = []
    all_failures: list[str] = []

    for pid in targets:
        product_dir = PRODUCTS / pid
        if not product_dir.exists():
            all_failures.append(f"{pid}: product directory does not exist")
            continue
        warnings, failures = audit_product(product_dir, args.strict)
        all_warnings.extend(warnings)
        all_failures.extend(failures)

    if all_warnings:
        print("Workflow substance audit warnings:")
        for item in all_warnings:
            print(f"- {item}")
    else:
        print("Workflow substance audit passed with no warnings.")

    if all_failures:
        print("\nStrict mode failures:")
        for item in all_failures:
            print(f"- {item}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
