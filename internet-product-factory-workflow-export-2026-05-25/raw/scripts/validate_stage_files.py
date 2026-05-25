from __future__ import annotations

import re
from pathlib import Path

from workflow_schema import (
    ANALYSIS_HEADINGS,
    BASE_STAGE_FILES,
    BUSINESS_WORKFLOW_GATE_TERMS,
    BUSINESS_WORKFLOW_SCORE_TERMS,
    CONFIDENCE_LEVELS,
    DATA_ANALYSIS_HEADINGS,
    DEMAND_BIAS_GATE_TERMS,
    DEMAND_BIAS_SCORE_TERMS,
    EVIDENCE_TABLE_HEADER,
    GITHUB_LAUNCH_PAGE_GATE_TERMS,
    GITHUB_README_REQUIRED_SECTIONS,
    IMPLEMENTATION_DEPTH_GATE_TERMS,
    IMPLEMENTATION_DEPTH_SCORE_TERMS,
    METHOD_FIT_GATE_TERMS,
    METHOD_FIT_SCORE_TERMS,
    NEXT_STAGE_BRIEF_HEADINGS,
    PRODUCT_DEPTH_GATE_TERMS,
    PRODUCT_DEPTH_SCORE_TERMS,
    Q_GATE_DECISIONS,
    REAL_WORLD_DEPTH_GATE_TERMS,
    REAL_WORLD_DEPTH_SCORE_TERMS,
    REQUIRED_SUBSTAGE_HEADINGS,
    STAGES,
)

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "products"

REQUIRED_ROOT = ["README.md", "AGENTS.md", ".env.example"]
REQUIRED_TOP_DIRS = ["workflows", "templates", "products", "memory", "skills", "audit", "scripts", "internal-tools"]
REQUIRED_TEMPLATES = [
    "acceptance-criteria-template.md",
    "audit-report-template.md",
    "bilingual-github-release-plan.md",
    "checkpoint-template.md",
    "configuration-freshness-gate.md",
    "core-capability-gate.md",
    "decision-log-template.md",
    "demand-discovery-report-template.md",
    "demand-scorecard-template.md",
    "frontend-calculator-trap-check.md",
    "input-automation-gate.md",
    "internal-tool-classification.md",
    "launch-plan-template.md",
    "launch-slot-scorecard.md",
    "mvp-prd-template.md",
    "next-stage-brief-template.md",
    "product-build-brief.md",
    "product-discovery-template.md",
    "product-folder-template.md",
    "prompt-log-template.md",
    "public-product-quality-bar.md",
    "q-gate-checklist.md",
    "q-gate-template.md",
    "readme-claim-check.md",
    "real-data-path-gate.md",
    "reflection-template.md",
    "stage-report-template.md",
    "subagent-persona-template.md",
    "substage-report-template.md",
    "technical-spec-template.md",
    "user-friction-gate.md",
    "build-depth-checklist.md",
    "implementation-depth-gate.md",
    "ui-specificity-gate.md",
    "core-mechanism-requirement.md",
    "fixture-and-edge-case-depth.md",
    "output-actionability-gate.md",
    "real-world-depth-gate.md",
    "ecosystem-compatibility-gate.md",
    "external-data-integration-gate.md",
    "remediation-depth-gate.md",
    "real-corpus-benchmark-gate.md",
    "ci-automation-readiness-gate.md",
    "demand-bias-check.md",
    "github-launch-page-gate.md",
    "business-workflow-depth-gate.md",
    "data-sufficiency-gate.md",
    "business-constraint-gate.md",
    "source-system-preset-gate.md",
    "operational-actionability-gate.md",
    "what-if-simulation-gate.md",
    "realistic-business-fixture-gate.md",
    "disciplinary-method-fit-gate.md",
    "method-depth-gate.md",
    "multi-perspective-reasoning-gate.md",
]
REQUIRED_WORKFLOWS = [
    "00_context.md",
    "01_demand_discovery.md",
    "02_demand_scoring.md",
    "03_q_gate.md",
    "04_product_discovery.md",
    "05_mvp_specification.md",
    "06_build_execution.md",
    "07_multi_agent_audit.md",
    "08_packaging_launch.md",
    "09_post_launch_feedback.md",
    "10_reflection_memory.md",
]

LEGACY_FILE = PRODUCTS / "_legacy-pre-substage-products.md"
COMPLETED_STATUSES = {"COMPLETE", "COMPLETED"}
SKIP_500_STATUSES = {"NOT_STARTED", "BLOCKED", "LEGACY_RECLASSIFIED", "RETROFITTED_AFTER_FAILURE", "REMOTE_DELETED"}
FILLER_PHRASES = (
    "with the development of technology",
    "in today's fast-paced world",
    "businesses need to adapt",
    "this is very important",
    "as we all know",
)
THIN_TOOL_TERMS = (
    "checklist",
    "simple analyzer",
    "readme optimizer",
    "config checker",
    ".env sync",
    "log summarizer",
    "one-file cli",
    "simple parser",
    "basic scoring script",
)
RESEARCH_KINDS = {"research", "audit", "packaging"}
DATA_HEAVY_KINDS = {"data_analysis"}
ANALYTICS_CLAIM_TERMS = (
    "analytics",
    "simulator",
    "simulation",
    "observability",
    "monitor",
    "analyzer",
    "trace",
    "logs",
    "cost",
    "workflow",
)
REAL_DATA_TERMS = (
    "real data path",
    "jsonl trace",
    "csv export",
    "log file",
    "trace import",
    "langsmith",
    "langfuse",
    "helicone",
    "openai",
    "litellm",
    "github issues",
    "repo metadata",
    "api connection",
    "sdk",
    "proxy",
    "plugin",
    "github action",
)
MANUAL_JSON_TERMS = (
    "manual json",
    "hand-written json",
    "manually writes complex json",
    "manually enter all important values",
    "sample json alone",
)
IMPLEMENTATION_DEPTH_UPGRADE_PRODUCT_NUMBER = 16
REAL_WORLD_DEPTH_UPGRADE_PRODUCT_NUMBER = 17
DEMAND_BIAS_UPGRADE_PRODUCT_NUMBER = 17
GITHUB_LAUNCH_PAGE_UPGRADE_PRODUCT_NUMBER = 18
BUSINESS_WORKFLOW_UPGRADE_PRODUCT_NUMBER = 19
METHOD_FIT_UPGRADE_PRODUCT_NUMBER = 23
IMPLEMENTATION_DEPTH_ARTIFACTS = {
    "core-mechanism-design.md",
    "ui-specificity-design.md",
    "fixture-plan.md",
    "core-logic-depth-report.md",
    "fixture-test-report.md",
}
REAL_WORLD_DEPTH_ARTIFACTS = {
    "real-world-depth-design.md",
    "ecosystem-compatibility-plan.md",
    "external-data-integration-plan.md",
    "real-corpus-benchmark-plan.md",
    "real-corpus-benchmark-report.md",
    "ci-automation-readiness-report.md",
    "remediation-depth-report.md",
}
DEMAND_BIAS_ARTIFACTS = {"demand-bias-check.md"}
DEMAND_BIAS_STAGE1_SUBSTAGES = {
    "01_broad_source_scan.md",
    "02_pain_signal_extraction.md",
    "03_opportunity_clustering.md",
    "04_cross_audience_comparison.md",
    "05_evidence_quality_ranking.md",
    "06_product_opportunity_framing.md",
}
GITHUB_LAUNCH_PAGE_ARTIFACTS = {"README.md", "README.zh-CN.md", "launch-summary.md"}
GITHUB_LAUNCH_PAGE_STAGE8_SUBSTAGES = {
    "01_positioning_star_pull_angle.md",
    "03_problem_differentiation_copy.md",
    "04_demo_screenshot_gif_plan.md",
    "05_quick_start_example_output.md",
    "06_github_description_topics.md",
    "07_english_readme.md",
    "08_chinese_readme.md",
    "09_readme_claim_check.md",
    "10_launch_summary.md",
}
BUSINESS_WORKFLOW_STAGE7_SUBSTAGES = {"12_business_workflow_reviewer.md"}
BUSINESS_WORKFLOW_ARTIFACTS = {
    "business-workflow-map.md",
    "data-sufficiency-map.md",
    "constraint-map.md",
    "source-system-map.md",
    "data-quality-report.md",
    "missing-field-report.md",
    "business-fixture-report.md",
    "what-if-simulation-report.md",
    "business-constraint-report.md",
}
METHOD_FIT_STAGE7_SUBSTAGES = {"13_method_problem_fit_reviewer.md"}
METHOD_FIT_ARTIFACTS = {
    "method-fit-map.md",
    "analytical-core-design.md",
    "uncertainty-and-assumption-map.md",
    "method-implementation-report.md",
}


def product_number(product_dir: Path) -> int:
    match = re.search(r"product-(\d+)", product_dir.name)
    return int(match.group(1)) if match else 999999


def is_pre_implementation_depth_product(product_dir: Path) -> bool:
    return product_number(product_dir) < IMPLEMENTATION_DEPTH_UPGRADE_PRODUCT_NUMBER


def is_pre_real_world_depth_product(product_dir: Path) -> bool:
    return product_number(product_dir) < REAL_WORLD_DEPTH_UPGRADE_PRODUCT_NUMBER


def is_pre_demand_bias_product(product_dir: Path) -> bool:
    return product_number(product_dir) < DEMAND_BIAS_UPGRADE_PRODUCT_NUMBER


def is_pre_github_launch_page_product(product_dir: Path) -> bool:
    return product_number(product_dir) < GITHUB_LAUNCH_PAGE_UPGRADE_PRODUCT_NUMBER


def is_pre_business_workflow_product(product_dir: Path) -> bool:
    return product_number(product_dir) < BUSINESS_WORKFLOW_UPGRADE_PRODUCT_NUMBER


def is_pre_method_fit_product(product_dir: Path) -> bool:
    return product_number(product_dir) < METHOD_FIT_UPGRADE_PRODUCT_NUMBER


def stage_substage_lookup() -> dict[Path, object]:
    lookup: dict[Path, object] = {}
    for stage in STAGES:
        for substage in stage.substages:
            lookup[Path(stage.folder) / substage.file] = substage
    return lookup


SUBSTAGE_LOOKUP = stage_substage_lookup()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def file_has_content(path: Path) -> bool:
    return path.exists() and path.is_file() and bool(read_text(path).strip())


def status_of(text: str) -> str:
    patterns = [
        r"^\s*-\s*Status:\s*([A-Z_]+)",
        r"^\s*Status:\s*([A-Z_]+)",
        r"^\s*-\s*Checkpoint status:\s*([A-Z_]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.MULTILINE)
        if match:
            return match.group(1).strip()
    return "UNKNOWN"


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'_-]*", text))


def missing_headings(text: str, headings: tuple[str, ...]) -> list[str]:
    return [heading for heading in headings if heading not in text]


def evidence_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("| E"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) >= 9:
            rows.append(cells)
    return rows


def evidence_ids(text: str) -> set[str]:
    return set(re.findall(r"\bE\d+\b", text))


def source_types(rows: list[list[str]]) -> set[str]:
    return {row[1].strip().lower() for row in rows if len(row) > 1 and row[1].strip() and row[1].strip().upper() != "TBD"}


def confidence_rating(text: str) -> str | None:
    confidence_section = re.search(r"## 10\. Confidence Rating(?P<body>.*?)(?:\n## 11\.|\Z)", text, flags=re.DOTALL)
    if not confidence_section:
        return None
    body = confidence_section.group("body")
    for level in CONFIDENCE_LEVELS:
        if re.search(rf"\b{level}\b", body):
            return level
    return None


def analysis_body(text: str) -> str:
    match = re.search(r"## 6\. Analysis(?P<body>.*?)(?:\n## 7\.|\Z)", text, flags=re.DOTALL)
    return match.group("body") if match else ""


def has_evidence_references_in_analysis(text: str) -> bool:
    return bool(evidence_ids(analysis_body(text)))


def validate_evidence_table(path: Path, text: str, substage, problems: list[str]) -> None:
    if EVIDENCE_TABLE_HEADER not in text:
        problems.append(f"{path}: missing required Evidence Pack table header")
        return
    rows = evidence_rows(text)
    if not rows:
        problems.append(f"{path}: completed substage has no evidence rows")
        return
    for row in rows:
        evidence_id = row[0]
        reliability = row[6] if len(row) > 6 else ""
        relevance = row[7] if len(row) > 7 else ""
        if not re.fullmatch(r"E\d+", evidence_id):
            problems.append(f"{path}: invalid evidence ID `{evidence_id}`")
        if not re.fullmatch(r"(10|[1-9])", reliability):
            problems.append(f"{path}: evidence {evidence_id} missing reliability score 1-10")
        if not re.fullmatch(r"(10|[1-9])", relevance):
            problems.append(f"{path}: evidence {evidence_id} missing relevance score 1-10")
    if substage.min_evidence_rows and len(rows) < substage.min_evidence_rows:
        problems.append(f"{path}: completed {substage.kind} substage has {len(rows)} evidence rows, expected at least {substage.min_evidence_rows}")
    if substage.min_source_types and len(source_types(rows)) < substage.min_source_types:
        problems.append(f"{path}: completed {substage.kind} substage has too few source types")


def validate_data_checks(path: Path, text: str, problems: list[str]) -> None:
    for heading in DATA_ANALYSIS_HEADINGS:
        if heading not in text:
            problems.append(f"{path}: missing data-analysis heading `{heading}`")
    required_markers = [
        "+20% / -20% key positive factors",
        "+20% / -20% key negative factors",
        "Higher Depth Penalty",
        "Higher 30-Minute Copy Risk",
        "Lower Expected Star Pull",
        "Lower Demo Pull",
    ]
    for marker in required_markers:
        if marker not in text:
            problems.append(f"{path}: missing sensitivity marker `{marker}`")


def is_legacy_product(product_dir: Path) -> bool:
    if (product_dir / "workflow-state.md").exists():
        return False
    legacy_text = read_text(LEGACY_FILE)
    if product_dir.name in legacy_text:
        return True
    index_text = read_text(PRODUCTS / "_product-index.md")
    return product_dir.name in index_text and "Deleted from GitHub" in index_text and "INTERNAL_FACTORY_TOOL" in index_text


def validate_substage(path: Path, substage, problems: list[str]) -> None:
    if not file_has_content(path):
        problems.append(str(path))
        return
    text = read_text(path)
    for heading in missing_headings(text, REQUIRED_SUBSTAGE_HEADINGS):
        problems.append(f"{path}: missing heading `{heading}`")
    status = status_of(text)
    if status in COMPLETED_STATUSES:
        words = word_count(text)
        if words < 500:
            problems.append(f"{path}: COMPLETE substage has {words} words, expected at least 500 meaningful words")
        lower = text.lower()
        for phrase in FILLER_PHRASES:
            if phrase in lower:
                problems.append(f"{path}: contains filler phrase `{phrase}`")
        if "## 7. Scores" in text and not re.search(r"\b(10|[1-9])\b", text):
            problems.append(f"{path}: completed substage has no numeric score evidence")
        for heading in ANALYSIS_HEADINGS:
            if heading not in text:
                problems.append(f"{path}: missing analysis heading `{heading}`")
        if substage.kind in RESEARCH_KINDS or substage.requires_data_analysis:
            validate_evidence_table(path, text, substage, problems)
            if not has_evidence_references_in_analysis(text):
                problems.append(f"{path}: analysis does not reference evidence IDs")
        confidence = confidence_rating(text)
        if confidence is None:
            problems.append(f"{path}: missing confidence rating")
        if substage.requires_data_analysis or substage.kind in DATA_HEAVY_KINDS:
            validate_data_checks(path, text, problems)
    elif status not in SKIP_500_STATUSES and status != "UNKNOWN":
        problems.append(f"{path}: unknown status `{status}`")


def validate_next_stage_brief(path: Path, problems: list[str]) -> None:
    if not file_has_content(path):
        problems.append(str(path))
        return
    text = read_text(path)
    for heading in missing_headings(text, NEXT_STAGE_BRIEF_HEADINGS):
        problems.append(f"{path}: missing heading `{heading}`")


def validate_public_product_gates(product_dir: Path, problems: list[str]) -> None:
    scoring = read_text(product_dir / "02_demand_scoring" / "classification-table.md")
    if "PUBLIC_PRODUCT" not in scoring:
        return
    combined = "\n".join([
        scoring,
        read_text(product_dir / "02_demand_scoring" / "launch-slot-ranking.md"),
        read_text(product_dir / "03_q_gate" / "q-gate-report.md"),
    ])
    lower = combined.lower()
    if any(term in lower for term in THIN_TOOL_TERMS) and "PASS_PUBLIC_PRODUCT_BAR" not in combined:
        problems.append(f"{product_dir}: shallow tool appears marked PUBLIC_PRODUCT without PASS_PUBLIC_PRODUCT_BAR")
    required_gate_terms = ["Demo Pull", "Expected Star Pull", "30-Minute Copy", "PUBLIC_PRODUCT"]
    for term in required_gate_terms:
        if term not in combined:
            problems.append(f"{product_dir}: PUBLIC_PRODUCT record missing gate term `{term}`")


def validate_product_depth_gates(product_dir: Path, problems: list[str]) -> None:
    scoring = read_text(product_dir / "02_demand_scoring" / "classification-table.md")
    launch_ranking = read_text(product_dir / "02_demand_scoring" / "launch-slot-ranking.md")
    q_gate = read_text(product_dir / "03_q_gate" / "q-gate-report.md") + read_text(product_dir / "03_q_gate" / "05_kill_continue_decision.md")
    stage4 = read_text(product_dir / "04_product_discovery" / "core-capability-design.md") + read_text(product_dir / "04_product_discovery" / "input-automation-map.md")
    stage5 = read_text(product_dir / "05_mvp_specification" / "mvp-prd.md") + read_text(product_dir / "05_mvp_specification" / "technical-spec.md") + read_text(product_dir / "05_mvp_specification" / "acceptance-criteria.md")
    stage6 = read_text(product_dir / "06_build_execution" / "build-depth-checklist.md")
    stage7 = read_text(product_dir / "07_multi_agent_audit" / "audit-report.md") + read_text(product_dir / "07_multi_agent_audit" / "subagent-feedback.md") + read_text(product_dir / "07_multi_agent_audit" / "ship-or-not.md")
    stage8 = read_text(product_dir / "08_packaging_launch" / "readme-claim-check.md")
    combined = "\n".join([scoring, launch_ranking, q_gate, stage4, stage5, stage6, stage7, stage8])
    lower = combined.lower()

    for term in PRODUCT_DEPTH_SCORE_TERMS:
        if term not in scoring and term not in launch_ranking:
            problems.append(f"{product_dir}: Stage 2 scoring missing product-depth dimension `{term}`")

    for term in PRODUCT_DEPTH_GATE_TERMS:
        if term not in combined:
            problems.append(f"{product_dir}: missing product-depth gate term `{term}`")

    if not any(decision in q_gate for decision in Q_GATE_DECISIONS):
        problems.append(f"{product_dir}: Q-Gate missing valid decision including NEEDS_V2_BEFORE_LAUNCH")
    if "NEEDS_V2_BEFORE_LAUNCH" not in q_gate:
        problems.append(f"{product_dir}: Q-Gate does not document NEEDS_V2_BEFORE_LAUNCH as an available outcome")

    for required in ("real data path", "input automation", "configuration freshness", "accuracy", "uncertainty", "anti-shallow"):
        if required not in stage5.lower():
            problems.append(f"{product_dir}: Stage 5 MVP spec missing `{required}` requirement")

    for required in ("core capability implemented", "real data path implemented", "custom config implemented", "uncertainty handled", "smoke test covers real-data path", "readme does not overclaim"):
        if required not in stage6.lower():
            problems.append(f"{product_dir}: Stage 6 build-depth checklist missing `{required}`")

    for required in ("frontend calculator", "input burden", "core capability", "doing work for the user", "trust the output"):
        if required not in stage7.lower():
            problems.append(f"{product_dir}: Stage 7 audit missing shallow-risk check `{required}`")

    for required in ("readme claim", "implemented", "demo only", "roadmap", "overclaim"):
        if required not in stage8.lower():
            problems.append(f"{product_dir}: Stage 8 README claim check missing `{required}`")

    claims_analytics = any(term in lower for term in ANALYTICS_CLAIM_TERMS)
    has_real_path = any(term in lower for term in REAL_DATA_TERMS)
    manual_json_only = any(term in lower for term in MANUAL_JSON_TERMS) and not has_real_path
    top_publish = bool(re.search(r"(Slot Decision|Launch Slot Decision|slot decision|launch slot decision|Decision)\s*[:|]\s*`?TOP_10_PUBLISH`?", combined))
    strong_public = "PUBLIC_PRODUCT" in scoring and "NEEDS_V2_BEFORE_LAUNCH" not in q_gate

    if top_publish:
        blocking_terms = (
            "Core Capability Completeness < 7",
            "Input Automation Depth < 5",
            "Real Data Path Strength < 5",
            "Frontend Calculator Risk > 6",
            "User Friction > 7",
        )
        for term in blocking_terms:
            if term in combined:
                problems.append(f"{product_dir}: TOP_10_PUBLISH blocked by `{term}`")
        if claims_analytics and not has_real_path:
            problems.append(f"{product_dir}: TOP_10_PUBLISH blocked because analytics/simulator/observability claim has no real data path")
    if strong_public and manual_json_only and "developer config tool" not in lower:
        problems.append(f"{product_dir}: manual JSON as only main input cannot be strong PUBLIC_PRODUCT without developer-config-tool justification")


def validate_implementation_depth_gates(product_dir: Path, problems: list[str]) -> None:
    scoring = read_text(product_dir / "02_demand_scoring" / "classification-table.md") + read_text(product_dir / "02_demand_scoring" / "launch-slot-ranking.md")
    q_gate = read_text(product_dir / "03_q_gate" / "q-gate-report.md") + read_text(product_dir / "03_q_gate" / "05_kill_continue_decision.md")
    stage4 = (
        read_text(product_dir / "04_product_discovery" / "core-mechanism-design.md")
        + read_text(product_dir / "04_product_discovery" / "ui-specificity-design.md")
        + read_text(product_dir / "04_product_discovery" / "fixture-plan.md")
    )
    stage5 = (
        read_text(product_dir / "05_mvp_specification" / "mvp-prd.md")
        + read_text(product_dir / "05_mvp_specification" / "technical-spec.md")
        + read_text(product_dir / "05_mvp_specification" / "acceptance-criteria.md")
    )
    stage6 = (
        read_text(product_dir / "06_build_execution" / "build-depth-checklist.md")
        + read_text(product_dir / "06_build_execution" / "core-logic-depth-report.md")
        + read_text(product_dir / "06_build_execution" / "fixture-test-report.md")
    )
    stage7 = (
        read_text(product_dir / "07_multi_agent_audit" / "09_implementation_depth_reviewer.md")
        + read_text(product_dir / "07_multi_agent_audit" / "audit-report.md")
        + read_text(product_dir / "07_multi_agent_audit" / "ship-or-not.md")
    )
    stage8 = read_text(product_dir / "08_packaging_launch" / "readme-claim-check.md")
    combined = "\n".join([scoring, q_gate, stage4, stage5, stage6, stage7, stage8])
    lower = combined.lower()

    for term in IMPLEMENTATION_DEPTH_SCORE_TERMS:
        if term not in scoring and term not in stage6:
            problems.append(f"{product_dir}: implementation-depth scoring missing `{term}`")
    for term in IMPLEMENTATION_DEPTH_GATE_TERMS:
        if term not in combined:
            problems.append(f"{product_dir}: missing implementation-depth gate term `{term}`")

    for artifact in IMPLEMENTATION_DEPTH_ARTIFACTS:
        if not any(file_has_content(product_dir / stage.folder / artifact) for stage in STAGES):
            problems.append(f"{product_dir}: missing implementation-depth artifact `{artifact}`")

    for required in ("core mechanism", "deeper than keyword matching", "data structures", "edge cases", "toy-level"):
        if required not in stage4.lower():
            problems.append(f"{product_dir}: Stage 4 implementation design missing `{required}`")
    for required in ("parser/data depth", "ui specificity", "fixture depth", "edge case", "output actionability", "anti-toy"):
        if required not in stage5.lower():
            problems.append(f"{product_dir}: Stage 5 MVP spec missing implementation-depth requirement `{required}`")
    for required in ("core logic depth", "parser / data understanding depth", "keyword / regex dependence", "fixtures tested", "edge case coverage"):
        if required not in stage6.lower():
            problems.append(f"{product_dir}: Stage 6 build records missing `{required}`")
    for required in ("implementation depth reviewer", "core logic depth", "mostly regex", "copied shell", "output is actionable", "deserves public launch"):
        if required not in stage7.lower():
            problems.append(f"{product_dir}: Stage 7 audit missing implementation-depth reviewer check `{required}`")
    for required in ("advanced analysis", "rule-based", "static rules", "sample-only", "roadmap"):
        if required not in stage8.lower():
            problems.append(f"{product_dir}: Stage 8 README depth honesty check missing `{required}`")

    sample_words = len(re.findall(r"\b(sample|fixture|example)\b", lower))
    edge_words = len(re.findall(r"\b(edge case|malformed|complex|empty input|missing field|no-issue|negative case)\b", lower))
    if "PUBLIC_PRODUCT" in scoring and sample_words < 3:
        problems.append(f"{product_dir}: PUBLIC_PRODUCT must document at least 3 sample/fixture inputs")
    if "PUBLIC_PRODUCT" in scoring and edge_words < 5:
        problems.append(f"{product_dir}: PUBLIC_PRODUCT must document at least 5 edge-case references")

    top_publish = bool(re.search(r"(Slot Decision|Launch Slot Decision|slot decision|launch slot decision|Decision)\s*[:|]\s*`?TOP_10_PUBLISH`?", combined))
    if top_publish:
        blockers = (
            "Core Logic Depth < 7",
            "UI Specificity < 5",
            "Test Depth < 5",
            "Output Actionability < 6",
            "Non-Trivial Mechanism Depth < 6",
            "Toy Implementation Risk > 6",
        )
        for blocker in blockers:
            if blocker in combined:
                problems.append(f"{product_dir}: TOP_10_PUBLISH blocked by `{blocker}`")
    if "keyword matching" in lower or "regex matching" in lower or "mostly regex" in lower:
        has_added_depth = any(term in lower for term in ("ast parser", "graph analysis", "auto-fix", "benchmark", "confidence scoring", "configurable rule engine", "multi-file project analysis"))
        if top_publish and not has_added_depth:
            problems.append(f"{product_dir}: regex/keyword scanner cannot be TOP_10_PUBLISH without additional depth")


def validate_real_world_depth_gates(product_dir: Path, problems: list[str]) -> None:
    scoring = read_text(product_dir / "02_demand_scoring" / "classification-table.md") + read_text(product_dir / "02_demand_scoring" / "launch-slot-ranking.md")
    q_gate = read_text(product_dir / "03_q_gate" / "q-gate-report.md") + read_text(product_dir / "03_q_gate" / "05_kill_continue_decision.md")
    stage4 = "\n".join(read_text(product_dir / "04_product_discovery" / artifact) for artifact in REAL_WORLD_DEPTH_ARTIFACTS)
    stage5 = read_text(product_dir / "05_mvp_specification" / "mvp-prd.md") + read_text(product_dir / "05_mvp_specification" / "technical-spec.md")
    stage6 = "\n".join(read_text(product_dir / "06_build_execution" / artifact) for artifact in REAL_WORLD_DEPTH_ARTIFACTS)
    stage7 = read_text(product_dir / "07_multi_agent_audit" / "10_real_world_depth_reviewer.md") + read_text(product_dir / "07_multi_agent_audit" / "audit-report.md") + read_text(product_dir / "07_multi_agent_audit" / "ship-or-not.md")
    stage8 = read_text(product_dir / "08_packaging_launch" / "readme-claim-check.md")
    combined = "\n".join([scoring, q_gate, stage4, stage5, stage6, stage7, stage8])
    lower = combined.lower()

    for term in REAL_WORLD_DEPTH_SCORE_TERMS:
        if term not in scoring and term not in combined:
            problems.append(f"{product_dir}: real-world-depth scoring missing `{term}`")
    for term in REAL_WORLD_DEPTH_GATE_TERMS:
        if term not in combined:
            problems.append(f"{product_dir}: missing real-world-depth gate term `{term}`")

    for artifact in REAL_WORLD_DEPTH_ARTIFACTS:
        if not any(file_has_content(product_dir / stage.folder / artifact) for stage in STAGES):
            problems.append(f"{product_dir}: missing real-world-depth artifact `{artifact}`")

    for required in ("ecosystem compatibility", "real-world variants", "large", "complex", "unsupported variants"):
        if required not in stage4.lower() and required not in stage6.lower():
            problems.append(f"{product_dir}: ecosystem compatibility records missing `{required}`")
    for required in ("external data", "authoritative", "structural risk", "honest scope"):
        if required not in combined.lower():
            problems.append(f"{product_dir}: external-data integration records missing `{required}`")
    for required in ("affected path", "severity", "confidence", "why it matters", "next command", "override", "direct dependency"):
        if required not in combined.lower():
            problems.append(f"{product_dir}: remediation-depth records missing `{required}`")
    for required in ("node count", "edge count", "runtime", "findings count", "false-positive"):
        if required not in combined.lower():
            problems.append(f"{product_dir}: real-corpus benchmark records missing `{required}`")
    for required in ("cli", "json export", "markdown export", "sarif", "github actions", "exit-code"):
        if required not in combined.lower():
            problems.append(f"{product_dir}: CI/automation readiness records missing `{required}`")
    product_identity_text = (scoring + "\n" + q_gate).lower()
    is_dependency_product = any(term in product_identity_text for term in ("package-lock", "npm dependency", "dependency product", "dependency analyzer"))
    for required in ("dependency path explorer", "duplicate version", "hotspot ranking", "risk propagation", "direct dependency blame"):
        if is_dependency_product and required not in lower:
            problems.append(f"{product_dir}: dependency UI domain specificity missing `{required}`")

    top_publish = bool(re.search(r"(Slot Decision|Launch Slot Decision|slot decision|launch slot decision|Decision)\s*[:|]\s*`?TOP_10_PUBLISH`?", combined))
    if top_publish:
        if "toy-only" in lower or "only toy" in lower:
            problems.append(f"{product_dir}: TOP_10_PUBLISH blocked by toy-only fixtures")
        if "generic upload" in lower and "domain-specific" not in lower:
            problems.append(f"{product_dir}: TOP_10_PUBLISH blocked by generic upload-report UI")
        if "no remediation" in lower or "generic advice" in lower:
            problems.append(f"{product_dir}: TOP_10_PUBLISH blocked by missing remediation depth")
        if ("security" in lower or "risk analysis" in lower or "vulnerability" in lower) and not any(term in lower for term in ("osv", "github advisory", "npm audit", "external data", "structural risk only", "structural risk")):
            problems.append(f"{product_dir}: security/risk claim needs external data or structural-risk scope")
        if "developer tool" in lower and not any(term in lower for term in ("--ci", "json export", "markdown export", "sarif", "github actions", "exit-code threshold")):
            problems.append(f"{product_dir}: developer tool without CLI/export/CI path loses TOP_10_PUBLISH")


def validate_demand_bias_gates(product_dir: Path, problems: list[str]) -> None:
    stage1 = "\n".join([
        read_text(product_dir / "01_demand_discovery" / "01_broad_source_scan.md"),
        read_text(product_dir / "01_demand_discovery" / "02_pain_signal_extraction.md"),
        read_text(product_dir / "01_demand_discovery" / "03_opportunity_clustering.md"),
        read_text(product_dir / "01_demand_discovery" / "04_cross_audience_comparison.md"),
        read_text(product_dir / "01_demand_discovery" / "05_evidence_quality_ranking.md"),
        read_text(product_dir / "01_demand_discovery" / "06_product_opportunity_framing.md"),
        read_text(product_dir / "01_demand_discovery" / "07_demand_synthesis.md"),
        read_text(product_dir / "01_demand_discovery" / "demand-bias-check.md"),
        read_text(product_dir / "01_demand_discovery" / "next-stage-brief.md"),
    ])
    scoring = read_text(product_dir / "02_demand_scoring" / "classification-table.md") + read_text(product_dir / "02_demand_scoring" / "launch-slot-ranking.md")
    selection = stage1 + "\n" + scoring
    lower = selection.lower()

    for term in DEMAND_BIAS_GATE_TERMS:
        if term not in selection:
            problems.append(f"{product_dir}: missing demand-bias gate term `{term}`")
    for term in DEMAND_BIAS_SCORE_TERMS:
        if term not in scoring and term not in selection:
            problems.append(f"{product_dir}: Stage 2 scoring missing demand-bias dimension `{term}`")

    pools = (
        "developer",
        "student",
        "job seeker",
        "creator",
        "small business",
        "personal finance",
        "life admin",
        "productivity",
        "education",
    )
    represented = sum(1 for pool in pools if pool in lower)
    if represented < 5:
        problems.append(f"{product_dir}: broad demand discovery must mention at least 5 demand pools")
    for required in ("top developer", "top non-developer", "github bias", "buildability bias", "category overconcentration", "source diversity"):
        if required not in lower:
            problems.append(f"{product_dir}: demand-bias check missing `{required}`")
    if "developer tool" in lower and "top non-developer" not in lower:
        problems.append(f"{product_dir}: developer winner must be compared against top non-developer candidate")
    if "non-developer" in lower and "top developer" not in lower:
        problems.append(f"{product_dir}: non-developer winner must be compared against top developer candidate")
    if "TOP_10_PUBLISH" in selection and ("DEV_SOURCE_BIAS" in selection or "CATEGORY_OVERCONCENTRATION" in selection) and "PASS_BIAS_CHECK" not in selection:
        problems.append(f"{product_dir}: TOP_10_PUBLISH blocked until demand bias check passes")


def complete_stage(path: Path) -> bool:
    text = read_text(path)
    return status_of(text) in COMPLETED_STATUSES or "COMPLETE" in text or "READY_FOR_GITHUB" in text


def validate_github_launch_page_gates(product_dir: Path, problems: list[str]) -> None:
    stage8_dir = product_dir / "08_packaging_launch"
    audit_dir = product_dir / "07_multi_agent_audit"
    readme_en = stage8_dir / "README.md"
    readme_zh = stage8_dir / "README.zh-CN.md"
    description = stage8_dir / "github-description.md"
    topics = stage8_dir / "github-topics.md"
    claim_check = stage8_dir / "readme-claim-check.md"
    launch_summary = stage8_dir / "launch-summary.md"
    reviewer = audit_dir / "11_github_readme_reviewer.md"

    combined = "\n".join(
        read_text(path)
        for path in (readme_en, readme_zh, description, topics, claim_check, launch_summary, reviewer)
    )

    for term in GITHUB_LAUNCH_PAGE_GATE_TERMS:
        if term not in combined:
            problems.append(f"{product_dir}: missing GitHub launch-page gate term `{term}`")

    for path in (readme_en, readme_zh, description, topics, claim_check, launch_summary, reviewer):
        if not file_has_content(path):
            problems.append(str(path))

    completed = complete_stage(stage8_dir / "checkpoint.md") or "READY_FOR_GITHUB" in combined or "SHIP" in read_text(product_dir / "07_multi_agent_audit" / "ship-or-not.md")
    if not completed:
        return

    en = read_text(readme_en)
    zh = read_text(readme_zh)
    for section in GITHUB_README_REQUIRED_SECTIONS:
        if section not in en:
            problems.append(f"{readme_en}: missing README section `{section}`")

    zh_required = (
        "问题",
        "为什么现有方式不够",
        "这个项目做什么",
        "核心功能",
        "演示",
        "快速开始",
        "输入 / 输出示例",
        "使用场景",
        "工作原理",
        "项目结构",
        "路线图",
        "限制",
        "许可证",
    )
    for section in zh_required:
        if section not in zh:
            problems.append(f"{readme_zh}: missing Chinese README section `{section}`")

    if "README.zh-CN.md" not in en or "README.md" not in zh:
        problems.append(f"{product_dir}: README language links missing")

    lower_en = en.lower()
    first_problem = lower_en.find("## problem")
    first_quick = lower_en.find("## quick start")
    first_limit = lower_en.find("## limitations")
    if first_problem == -1 or (first_quick != -1 and first_quick < first_problem):
        problems.append(f"{readme_en}: first screen must explain value before installation/quickstart-heavy content")
    if first_limit != -1 and first_limit < int(len(en) * 0.6):
        problems.append(f"{readme_en}: limitations section appears too early; group limitations near the end")
    scattered_terms = ("only a prototype", "not perfect", "just a simple tool", "not production ready", "does not really")
    body_before_limit = lower_en[: first_limit if first_limit != -1 else len(lower_en)]
    for term in scattered_terms:
        if term in body_before_limit:
            problems.append(f"{readme_en}: self-sabotaging limitation phrase appears before Limitations section: `{term}`")

    if "Why this is useful" not in en:
        problems.append(f"{readme_en}: missing `Why this is useful` star-pull copy")
    if "Short Repo Description" not in read_text(description) or "Alternative Descriptions" not in read_text(description):
        problems.append(f"{description}: missing short description or alternatives")
    topic_lines = [line for line in read_text(topics).splitlines() if line.strip().startswith("- ") and "TBD" not in line]
    if topic_lines and not (10 <= len(topic_lines) <= 20):
        problems.append(f"{topics}: completed topic list should contain 10-20 topics")
    for required in (
        "Every major README claim",
        "Roadmap",
        "Demo",
        "Mock",
        "Limitations",
        "English and Chinese",
        "Quick Start",
    ):
        if required.lower() not in read_text(claim_check).lower():
            problems.append(f"{claim_check}: missing claim-check requirement `{required}`")
    for required in (
        "understand",
        "10 seconds",
        "star",
        "first screen",
        "too technical",
        "limitations",
        "Chinese README",
        "English README",
    ):
        if required.lower() not in read_text(reviewer).lower():
            problems.append(f"{reviewer}: missing GitHub README Reviewer check `{required}`")


def validate_business_workflow_gates(product_dir: Path, problems: list[str]) -> None:
    scoring = read_text(product_dir / "02_demand_scoring" / "classification-table.md") + read_text(product_dir / "02_demand_scoring" / "launch-slot-ranking.md")
    q_gate = read_text(product_dir / "03_q_gate" / "q-gate-report.md") + read_text(product_dir / "03_q_gate" / "05_kill_continue_decision.md")
    stage1 = read_text(product_dir / "01_demand_discovery" / "demand-discovery-report.md") + read_text(product_dir / "01_demand_discovery" / "raw-signal-log.md")
    stage4 = "\n".join(read_text(product_dir / "04_product_discovery" / artifact) for artifact in ("business-workflow-map.md", "data-sufficiency-map.md", "constraint-map.md", "source-system-map.md"))
    stage5 = read_text(product_dir / "05_mvp_specification" / "mvp-prd.md") + read_text(product_dir / "05_mvp_specification" / "technical-spec.md")
    stage6 = "\n".join(read_text(product_dir / "06_build_execution" / artifact) for artifact in ("data-quality-report.md", "missing-field-report.md", "business-fixture-report.md", "what-if-simulation-report.md", "business-constraint-report.md", "build-log.md", "fixture-test-report.md"))
    stage7 = read_text(product_dir / "07_multi_agent_audit" / "12_business_workflow_reviewer.md") + read_text(product_dir / "07_multi_agent_audit" / "audit-report.md") + read_text(product_dir / "07_multi_agent_audit" / "ship-or-not.md")
    stage8 = read_text(product_dir / "08_packaging_launch" / "README.md") + read_text(product_dir / "08_packaging_launch" / "readme-claim-check.md")
    combined = "\n".join([stage1, scoring, q_gate, stage4, stage5, stage6, stage7, stage8])
    lower = combined.lower()

    for term in BUSINESS_WORKFLOW_SCORE_TERMS:
        if term not in scoring and term not in combined:
            problems.append(f"{product_dir}: Stage 2 scoring missing business-workflow dimension `{term}`")
    for term in BUSINESS_WORKFLOW_GATE_TERMS:
        if term not in combined:
            problems.append(f"{product_dir}: missing business-workflow gate term `{term}`")

    for artifact in BUSINESS_WORKFLOW_ARTIFACTS:
        if not any(file_has_content(product_dir / stage.folder / artifact) for stage in STAGES):
            problems.append(f"{product_dir}: missing business-workflow artifact `{artifact}`")

    for required in ("where the user's data lives", "naturally exists", "operational constraints", "decision the user needs", "current workaround"):
        if required not in lower:
            problems.append(f"{product_dir}: Stage 1 demand discovery missing business context `{required}`")
    for required in ("required fields", "optional fields", "missing-field behavior", "confidence downgrade", "source systems", "export formats"):
        if required not in stage4.lower() and required not in stage5.lower():
            problems.append(f"{product_dir}: business discovery/spec missing `{required}`")
    for required in ("data quality", "missing field", "realistic", "malformed", "edge", "what-if", "sensitivity", "constraint"):
        if required not in stage6.lower():
            problems.append(f"{product_dir}: Stage 6 business build evidence missing `{required}`")
    for required in ("spreadsheet", "real business operations", "constraints modeled", "input realistic", "outputs actionable", "more useful than excel"):
        if required not in stage7.lower():
            problems.append(f"{product_dir}: Business Workflow Reviewer missing `{required}`")
    for required in ("supported input", "source", "assumptions", "limitations", "overclaim"):
        if required not in stage8.lower():
            problems.append(f"{product_dir}: Stage 8 business README honesty missing `{required}`")

    top_publish = bool(re.search(r"(Slot Decision|Launch Slot Decision|slot decision|launch slot decision|Decision)\s*[:|]\s*`?TOP_10_PUBLISH`?", combined))
    if top_publish:
        blockers = (
            "Spreadsheet Trap Risk > 6",
            "Business Constraint Depth < 5",
            "Operational Actionability < 6",
            "Data Sufficiency Score < 6",
            "toy samples",
            "happy-path-only",
            "generic recommendations",
        )
        for blocker in blockers:
            if blocker.lower() in lower:
                problems.append(f"{product_dir}: TOP_10_PUBLISH blocked by `{blocker}`")
        if "missing fields silently" in lower or "no missing-field handling" in lower:
            problems.append(f"{product_dir}: missing-field handling blocks TOP_10_PUBLISH")


def validate_method_fit_gates(product_dir: Path, problems: list[str]) -> None:
    scoring = read_text(product_dir / "02_demand_scoring" / "classification-table.md") + read_text(product_dir / "02_demand_scoring" / "launch-slot-ranking.md")
    q_gate = read_text(product_dir / "03_q_gate" / "q-gate-report.md") + read_text(product_dir / "03_q_gate" / "05_kill_continue_decision.md")
    stage4 = "\n".join(read_text(product_dir / "04_product_discovery" / artifact) for artifact in ("method-fit-map.md", "analytical-core-design.md", "uncertainty-and-assumption-map.md"))
    stage5 = read_text(product_dir / "05_mvp_specification" / "mvp-prd.md") + read_text(product_dir / "05_mvp_specification" / "technical-spec.md") + read_text(product_dir / "05_mvp_specification" / "acceptance-criteria.md")
    stage6 = read_text(product_dir / "06_build_execution" / "method-implementation-report.md") + read_text(product_dir / "06_build_execution" / "build-log.md")
    stage7 = read_text(product_dir / "07_multi_agent_audit" / "13_method_problem_fit_reviewer.md") + read_text(product_dir / "07_multi_agent_audit" / "audit-report.md") + read_text(product_dir / "07_multi_agent_audit" / "ship-or-not.md")
    stage8 = read_text(product_dir / "08_packaging_launch" / "README.md") + read_text(product_dir / "08_packaging_launch" / "readme-claim-check.md")
    combined = "\n".join([scoring, q_gate, stage4, stage5, stage6, stage7, stage8])
    lower = combined.lower()

    for term in METHOD_FIT_SCORE_TERMS:
        if term not in scoring and term not in combined:
            problems.append(f"{product_dir}: Stage 2 scoring missing method-fit dimension `{term}`")
    for term in METHOD_FIT_GATE_TERMS:
        if term not in combined:
            problems.append(f"{product_dir}: missing method-fit gate term `{term}`")

    for artifact in METHOD_FIT_ARTIFACTS:
        if not any(file_has_content(product_dir / stage.folder / artifact) for stage in STAGES):
            problems.append(f"{product_dir}: missing method-fit artifact `{artifact}`")

    for required in ("discipline", "methods that fit", "methods that do not fit", "minimum serious method core", "method theater", "shallow"):
        if required not in stage4.lower():
            problems.append(f"{product_dir}: Stage 4 method-fit map missing `{required}`")
    for required in ("core analytical mechanism", "user inputs", "inferred parameters", "model", "output interpretation", "better than simple scoring"):
        if required not in stage4.lower() and required not in stage5.lower():
            problems.append(f"{product_dir}: analytical core design/spec missing `{required}`")
    for required in ("uncertain inputs", "assumptions", "confidence logic", "sensitivity", "what would flip"):
        if required not in stage4.lower() and required not in stage5.lower():
            problems.append(f"{product_dir}: uncertainty and assumption map missing `{required}`")
    for required in ("method core", "minimum analytical depth", "uncertainty handling", "assumption challenge", "method-specific tests", "anti-shallow-scoring"):
        if required not in stage5.lower():
            problems.append(f"{product_dir}: Stage 5 MVP spec missing method requirement `{required}`")
    for required in ("implemented method", "code locations", "assumptions used", "sensitivity", "robustness", "not simple threshold scoring"):
        if required not in stage6.lower():
            problems.append(f"{product_dir}: Stage 6 method implementation report missing `{required}`")
    for required in ("method-problem fit reviewer", "naturally fit", "fake complexity", "simple scoring", "assumptions challenged", "uncertainty handled", "domain-aware"):
        if required not in stage7.lower():
            problems.append(f"{product_dir}: Stage 7 Method-Problem Fit Reviewer missing `{required}`")
    for required in ("method", "assumptions", "limitations", "monte carlo", "multi-agent", "optimization"):
        if required not in stage8.lower():
            problems.append(f"{product_dir}: Stage 8 method honesty missing `{required}`")

    top_publish = bool(re.search(r"(Slot Decision|Launch Slot Decision|slot decision|launch slot decision|Decision)\s*[:|]\s*`?TOP_10_PUBLISH`?", combined))
    if top_publish:
        blockers = (
            "Method Fit < 6",
            "Method Depth < 6",
            "Method Theater Risk > 6",
            "Shallow Scoring Risk > 6",
            "simple thresholds",
            "generic scoring",
            "uncertainty ignored",
            "assumptions are never challenged",
        )
        for blocker in blockers:
            if blocker.lower() in lower:
                problems.append(f"{product_dir}: TOP_10_PUBLISH blocked by `{blocker}`")
    forbidden_claim = "claims monte carlo" in lower or "implemented monte carlo" in lower or "uses monte carlo" in lower
    if forbidden_claim and any(term in lower for term in ("not natural", "does not fit", "method theater", "fake complexity")):
        problems.append(f"{product_dir}: arbitrary Monte Carlo / method theater must downgrade Method Fit")
    if "recommendation" in lower and "what would flip" not in lower and "sensitivity" not in lower:
        problems.append(f"{product_dir}: recommendations need assumption-flip or sensitivity explanation")


def validate_legacy_product(product_dir: Path, problems: list[str]) -> None:
    for stage in STAGES:
        stage_dir = product_dir / stage.folder
        if not stage_dir.is_dir():
            problems.append(str(stage_dir))
            continue
        for required in ("stage-report.md", "checkpoint.md", "decision-log.md"):
            path = stage_dir / required
            if not file_has_content(path):
                problems.append(str(path))
    classification = read_text(product_dir / "02_demand_scoring" / "classification-table.md")
    if "INTERNAL_FACTORY_TOOL" not in classification:
        problems.append(f"{product_dir}: legacy product must be classified INTERNAL_FACTORY_TOOL")


def validate_state_machine_product(product_dir: Path, problems: list[str]) -> None:
    if not file_has_content(product_dir / "workflow-state.md"):
        problems.append(str(product_dir / "workflow-state.md"))
    for stage in STAGES:
        stage_dir = product_dir / stage.folder
        if not stage_dir.is_dir():
            problems.append(str(stage_dir))
            continue
        for substage in stage.substages:
            if is_pre_demand_bias_product(product_dir) and stage.folder == "01_demand_discovery" and substage.file in DEMAND_BIAS_STAGE1_SUBSTAGES:
                continue
            if is_pre_implementation_depth_product(product_dir) and substage.file == "09_implementation_depth_reviewer.md":
                continue
            if is_pre_real_world_depth_product(product_dir) and substage.file == "10_real_world_depth_reviewer.md":
                continue
            if is_pre_github_launch_page_product(product_dir) and substage.file == "11_github_readme_reviewer.md":
                continue
            if is_pre_business_workflow_product(product_dir) and substage.file in BUSINESS_WORKFLOW_STAGE7_SUBSTAGES:
                continue
            if is_pre_method_fit_product(product_dir) and substage.file in METHOD_FIT_STAGE7_SUBSTAGES:
                continue
            if is_pre_github_launch_page_product(product_dir) and stage.folder == "08_packaging_launch" and substage.file in GITHUB_LAUNCH_PAGE_STAGE8_SUBSTAGES:
                continue
            validate_substage(stage_dir / substage.file, substage, problems)
        for file_name in BASE_STAGE_FILES:
            path = stage_dir / file_name
            if file_name == "next-stage-brief.md":
                validate_next_stage_brief(path, problems)
            elif not file_has_content(path):
                problems.append(str(path))
        for artifact in stage.artifacts:
            if is_pre_demand_bias_product(product_dir) and artifact in DEMAND_BIAS_ARTIFACTS:
                continue
            if is_pre_implementation_depth_product(product_dir) and artifact in IMPLEMENTATION_DEPTH_ARTIFACTS:
                continue
            if is_pre_real_world_depth_product(product_dir) and artifact in REAL_WORLD_DEPTH_ARTIFACTS:
                continue
            if is_pre_github_launch_page_product(product_dir) and artifact in GITHUB_LAUNCH_PAGE_ARTIFACTS:
                continue
            if is_pre_business_workflow_product(product_dir) and artifact in BUSINESS_WORKFLOW_ARTIFACTS:
                continue
            if is_pre_method_fit_product(product_dir) and artifact in METHOD_FIT_ARTIFACTS:
                continue
            path = stage_dir / artifact
            if not file_has_content(path):
                problems.append(str(path))

    scoring_table = product_dir / "02_demand_scoring" / "classification-table.md"
    if not file_has_content(scoring_table):
        problems.append(str(scoring_table))
    q_gate = read_text(product_dir / "03_q_gate" / "q-gate-report.md") + read_text(product_dir / "03_q_gate" / "05_kill_continue_decision.md")
    if not any(decision in q_gate for decision in Q_GATE_DECISIONS):
        problems.append(f"{product_dir}: Stage 3 Q-Gate decision missing")
    validate_public_product_gates(product_dir, problems)
    validate_product_depth_gates(product_dir, problems)
    if not is_pre_implementation_depth_product(product_dir):
        validate_implementation_depth_gates(product_dir, problems)
    if not is_pre_real_world_depth_product(product_dir):
        validate_real_world_depth_gates(product_dir, problems)
    if not is_pre_demand_bias_product(product_dir):
        validate_demand_bias_gates(product_dir, problems)
    if not is_pre_github_launch_page_product(product_dir):
        validate_github_launch_page_gates(product_dir, problems)
    if not is_pre_business_workflow_product(product_dir):
        validate_business_workflow_gates(product_dir, problems)
    if not is_pre_method_fit_product(product_dir):
        validate_method_fit_gates(product_dir, problems)
    combined_substages = "\n".join(read_text(product_dir / stage.folder / substage.file) for stage in STAGES for substage in stage.substages)
    if "PUBLIC_PRODUCT" in read_text(product_dir / "02_demand_scoring" / "classification-table.md"):
        low_confidence = len(re.findall(r"\b(LOW|SPECULATIVE)\b", combined_substages))
        high_or_medium = len(re.findall(r"\b(HIGH|MEDIUM)\b", combined_substages))
        if low_confidence > high_or_medium:
            problems.append(f"{product_dir}: PUBLIC_PRODUCT blocked because evidence confidence is mostly LOW or SPECULATIVE")


def main() -> int:
    problems: list[str] = []

    for file_name in REQUIRED_ROOT:
        path = ROOT / file_name
        if not file_has_content(path):
            problems.append(str(path))

    for dir_name in REQUIRED_TOP_DIRS:
        path = ROOT / dir_name
        if not path.is_dir():
            problems.append(str(path))

    for file_name in REQUIRED_TEMPLATES:
        path = ROOT / "templates" / file_name
        if not file_has_content(path):
            problems.append(str(path))

    for file_name in REQUIRED_WORKFLOWS:
        path = ROOT / "workflows" / file_name
        if not file_has_content(path):
            problems.append(str(path))

    internal_index = ROOT / "internal-tools" / "_internal-tool-index.md"
    if not file_has_content(internal_index):
        problems.append(str(internal_index))

    product_dirs = sorted(p for p in PRODUCTS.glob("product-*") if p.is_dir())
    if not product_dirs:
        problems.append(str(PRODUCTS / "product-*"))

    legacy_count = 0
    state_machine_count = 0
    for product_dir in product_dirs:
        if is_legacy_product(product_dir):
            legacy_count += 1
            validate_legacy_product(product_dir, problems)
        else:
            state_machine_count += 1
            validate_state_machine_product(product_dir, problems)

    if problems:
        print("Validation failed. Missing, empty, or invalid:")
        for item in problems:
            print(f"- {item}")
        return 1

    print("Validation passed.")
    print(f"Products checked: {len(product_dirs)}")
    print(f"Legacy products: {legacy_count}")
    print(f"Substage state-machine products: {state_machine_count}")
    print("Required templates, workflows, handoff rules, and product records are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
