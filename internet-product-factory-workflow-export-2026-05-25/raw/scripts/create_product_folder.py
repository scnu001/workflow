from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from workflow_schema import BASE_STAGE_FILES, EVIDENCE_TABLE_HEADER, GITHUB_README_REQUIRED_SECTIONS, NEXT_STAGE_BRIEF_HEADINGS, STAGES

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "products"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def substage_content(stage_name: str, substage, timestamp: str) -> str:
    data_checks = "Required. Complete Baseline Analysis, Robustness Check, Sensitivity Check, Error / Outlier Check, Interpretation, and Decision Impact before marking COMPLETE." if substage.requires_data_analysis else "Not required unless this substage introduces quantitative scoring, ranking, benchmarking, cost simulation, pricing comparison, model/API output evaluation, or metrics."
    extra_guidance = ""
    if substage.file == "13_method_problem_fit_reviewer.md":
        extra_guidance = """

## Method-Problem Fit Reviewer Checklist

- Method-Problem Fit Reviewer: TBD
- Does the method naturally fit the problem? TBD
- Is there fake complexity or method theater? TBD
- Is this simple scoring with fancy wording? TBD
- Are assumptions challenged? TBD
- Is uncertainty handled? TBD
- Would a domain-aware user respect this analysis? TBD
"""
    return f"""# Substage: {substage.name}

- Stage: {stage_name}
- Substage file: {substage.file}
- Substage type: {substage.kind}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## 1. Objective

{substage.objective}

## 2. Why This Matters

TBD. Explain why this substage materially affects product selection, scoring, Q-Gate, build, audit, packaging, launch, or memory.

## 3. Method

TBD. Collect evidence before analysis. List local files read, prior substage files read, external sources checked, data analyzed, commands run, or reasoning method used. If external web access is unavailable, write `WEB_ACCESS_UNAVAILABLE` in Source Log and do not fabricate sources.

## 4. Evidence Pack

No evidence, no conclusion.

If evidence is unavailable, write: `Evidence unavailable. This is a hypothesis, not a finding.`

Source quota guidance: {substage.source_quota}

{EVIDENCE_TABLE_HEADER}
|---|---|---|---|---|---|---:|---:|---|
| E1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | No |

## 5. Source Log

### Queries Attempted

- TBD

### Sources Opened

- TBD

### Sources Rejected

- TBD

### Access Failures

- TBD

### Evidence Gaps

- TBD

### Claims That Must Remain Hypotheses

- TBD

## 6. Analysis

Every major claim must reference evidence IDs from the Evidence Pack. Unsupported claims belong under Weak Hypotheses.

### Evidence-Backed Findings

- TBD

### Reasonable Inferences

- TBD

### Weak Hypotheses

- TBD

### Unknowns

- TBD

### Implications for Product Decision

- TBD

### Data Analysis Checks

Data-analysis requirement: {data_checks}

#### Baseline Analysis

- Data source:
- Sample size:
- Variables used:
- Assumptions:
- Formula or scoring method:
- Baseline result:
- Interpretation:

#### Robustness Check

- Alternative or conservative check:
- Did the conclusion survive assumption changes:

#### Sensitivity Check

- +20% / -20% key positive factors:
- +20% / -20% key negative factors:
- Higher Depth Penalty:
- Higher 30-Minute Copy Risk:
- Lower Expected Star Pull:
- Lower Demo Pull:

#### Error / Outlier Check

- Duplicate sources:
- Duplicated signals:
- Low-quality sources:
- Outlier scores:
- Over-weighted single source:
- Unsupported high scores:
- Missing evidence IDs:
- Missing confidence rating:

#### Decision Impact

- TBD

## 7. Scores

| Dimension | Score 1-10 | Evidence IDs | Notes |
| --- | ---: | --- | --- |
| Signal Strength | TBD | TBD | TBD |
| User Pain | TBD | TBD | TBD |
| Demo Potential | TBD | TBD | TBD |
| Distribution Potential | TBD | TBD | TBD |
| Differentiation | TBD | TBD | TBD |
| Copy Risk | TBD | TBD | TBD |
| Trust / Compliance Risk | TBD | TBD | TBD |
| Core Logic Depth | TBD | TBD | Blocks PUBLIC_PRODUCT if < 5; blocks TOP_10_PUBLISH if < 7. |
| UI Specificity | TBD | TBD | <= 4 blocks TOP_10_PUBLISH. |
| Parser/Data Depth | TBD | TBD | Must show real data understanding, not just labels. |
| Edge Case Coverage | TBD | TBD | Must include realistic edge cases. |
| Test Depth | TBD | TBD | Happy-path smoke test alone is not enough. |
| Output Actionability | TBD | TBD | TOP_10_PUBLISH requires >= 6. |
| Non-Trivial Mechanism Depth | TBD | TBD | < 6 blocks TOP_10_PUBLISH. |
| Scaffold Reuse Risk | TBD | TBD | High reuse requires stronger core mechanism. |
| Toy Implementation Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |
| Ecosystem Compatibility | TBD | TBD | Toy-only ecosystem support blocks TOP_10_PUBLISH. |
| External Data Integration | TBD | TBD | Security/risk/pricing claims need authoritative data or honest scope. |
| Remediation Depth | TBD | TBD | Generic advice blocks TOP_10_PUBLISH. |
| Real Corpus Benchmark | TBD | TBD | Must include realistic/large/complex corpus evidence. |
| CI / Automation Readiness | TBD | TBD | Developer tools need CLI/export/CI path. |
| UI Domain Specificity | TBD | TBD | Generic upload-report UI is penalized. |
| README Claim Honesty | TBD | TBD | Claims must match implemented depth. |
| Evidence Breadth Score | TBD | TBD | Broad demand discovery must inspect multiple demand pools. |
| Cross-Audience Strength Score | TBD | TBD | Winning category must beat alternatives on evidence, not preference. |
| Source Diversity Score | TBD | TBD | GitHub/Hacker News overconcentration lowers confidence. |
| Demand Specificity Score | TBD | TBD | Pain must be concrete enough to frame a product. |
| Buildability Bias Risk | TBD | TBD | High if chosen mainly because Codex can build it easily. |
| GitHub Bias Risk | TBD | TBD | High if GitHub publishability is confused with market demand. |
| Category Overconcentration Risk | TBD | TBD | High if shortlist is dominated by one audience without evidence justification. |
| Data Sufficiency Score | TBD | TBD | Non-developer products must verify natural data availability and missing-field behavior. |
| Business Constraint Depth | TBD | TBD | Operational products need real constraints, not just spreadsheet math. |
| Operational Actionability | TBD | TBD | Outputs must tell the user what to do next, first, why, and with what risk. |
| Source-System Fit | TBD | TBD | CSV/XLSX products must name source systems and mapping/preset needs. |
| What-if Depth | TBD | TBD | Decision-support products need sensitivity or constraint simulation. |
| Realistic Fixture Depth | TBD | TBD | Business products need messy realistic fixtures, not clean toy rows. |
| Business Workflow Depth | TBD | TBD | Measures whether real operating work is reduced. |
| Spreadsheet Trap Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |
| Disciplinary Method Fit | TBD | TBD | Method must naturally fit the problem. |
| Method Depth | TBD | TBD | Analytical products with < 6 cannot be TOP_10_PUBLISH. |
| Analytical Originality | TBD | TBD | Scores whether the core is more than generic scoring. |
| Uncertainty Handling | TBD | TBD | Required when uncertainty affects decisions. |
| Assumption Challenge | TBD | TBD | Assumptions that drive recommendations must be challenged. |
| Multi-Perspective Reasoning | TBD | TBD | Complex judgment products need more than one-pass scoring. |
| Method Theater Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |
| Shallow Scoring Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |

## 8. Risks / Weak Points

- TBD

## 9. Output to Next Substage

- TBD

## 10. Confidence Rating

Choose one:
- HIGH
- MEDIUM
- LOW
- SPECULATIVE

## 11. Decision

Choose one:
- CONTINUE
- NEED_MORE_EVIDENCE
- WEAK_SIGNAL
- PARK
- PIVOT
- KILL

## 12. Minimum Quality Check

Confirm when marking COMPLETE:
- At least 500 meaningful words
- No generic filler
- Evidence Pack completed before Analysis
- Source Log completed
- Analysis references evidence IDs
- Confidence rating included
- Scores included where applicable
- Risks included
- Next-step output included
- Data-heavy substages include baseline, robustness, sensitivity, and error/outlier checks
{extra_guidance}
"""


def stage_report_content(stage_name: str, timestamp: str) -> str:
    return f"""# Stage Report: {stage_name}

- Status: NOT_STARTED
- Timestamp: {timestamp}

## 1. Stage Goal
TBD

## 2. Substages Completed
TBD

## 3. Files Created
TBD

## 4. Key Findings
TBD

## 5. Decisions Made
TBD

## 6. Scores / Rankings
TBD

## 7. Risks / Blockers
TBD

## 8. What Was Rejected
TBD

## 9. What Moves Forward
TBD

## 10. Handoff Summary
TBD

## 11. Completion Check
- all required substage files exist: TBD
- all completed substage files meet the minimum quality bar: TBD
- `checkpoint.md` exists: yes
- `decision-log.md` exists: yes
- `next-stage-brief.md` exists: yes
"""


def checkpoint_content(product_id: str, stage_folder: str, stage_name: str, timestamp: str) -> str:
    return f"""# Checkpoint

## Product ID
{product_id}

## Current Stage
{stage_folder} - {stage_name}

## Current Substage
NOT_STARTED

## Last Completed File
None

## Current Classification
UNKNOWN

## Current Decision
UNDECIDED

## Files Completed
- Scaffold files created only.

## Files Remaining
- All substages
- `stage-report.md`
- `decision-log.md`
- `next-stage-brief.md`

## Blockers
- Stage work has not started.

## Next Action
Start the first substage. Read prior stage `next-stage-brief.md` first if this is not Stage 0.

## Recovery Instructions
If context is lost, resume by reading:
1. `products/_product-index.md`
2. this `checkpoint.md`
3. this stage's `next-stage-brief.md` if available
4. this stage's `stage-report.md`
5. most recent substage file

- Timestamp: {timestamp}
"""


def decision_log_content(stage_name: str, timestamp: str) -> str:
    return f"""# Decision Log

## Decision Entry

- Date: {timestamp}
- Stage: {stage_name}
- Substage: NOT_STARTED
- Decision: UNDECIDED
- Reason: Scaffold created only.
- Evidence: None yet.
- Files affected: TBD
- Alternatives considered: PUBLIC_PRODUCT / INTERNAL_FACTORY_TOOL / EXPERIMENT / PARK / KILL
- Risk: No decision has been made.
- Next action: Complete substage evidence files before making a stage decision.
"""


def prompt_log_content(stage_name: str, timestamp: str) -> str:
    return f"""# Prompt Log

## Entry 001

### Timestamp
{timestamp}

### Agent
Codex / GPT / Claude Code / external API / subagent name

### Prompt
[Full prompt or summarized task for {stage_name}]

### Response Summary
TBD

### Files Created or Modified
- TBD

### Decision Impact
TBD
"""


def next_stage_brief_content(stage_name: str, timestamp: str) -> str:
    sections = "\n\n".join(f"{heading}\n\nTBD" for heading in NEXT_STAGE_BRIEF_HEADINGS[1:-1])
    return f"""# Next Stage Brief

- Status: NOT_STARTED
- Timestamp: {timestamp}

{sections}

## 10. Handoff Decision

Choose one:
- CONTINUE_TO_NEXT_STAGE
- RETURN_TO_PREVIOUS_STAGE
- NEED_MORE_RESEARCH
- BUILD_INTERNAL_ONLY
- KILL
"""


def artifact_content(artifact: str, stage_name: str, timestamp: str) -> str:
    title = artifact.replace(".md", "").replace("-", " ").replace("_", " ").title()
    if artifact == "README.md":
        sections = "\n\n".join(f"## {section}\n\nTBD." for section in GITHUB_README_REQUIRED_SECTIONS[1:])
        return f"""# Product Name

English | [中文](README.zh-CN.md)

One sentence explaining what the product does, who it helps, and why it matters.

- Key value 1: TBD
- Key value 2: TBD
- Key value 3: TBD

Screenshot/GIF to be added before launch.

Quick demo:

```bash
TBD
```

## Hero Section

This first screen must answer within 10 seconds: what this is, who it is for, what pain it solves, what output it creates, why a visitor should care, and how to try it.

{sections}

## Why this is useful

TBD. Explain the differentiated value with concrete product language, not generic productivity claims.

## Language

- English: `README.md`
- Chinese: `README.zh-CN.md`

<!--
Status: NOT_STARTED
Stage: {stage_name}
Timestamp: {timestamp}
GitHub Launch Page Gate: README.md must be product-oriented, honest, bilingual-linked, and claim-checked before launch.
-->
"""
    if artifact == "README.zh-CN.md":
        return f"""# 产品名称

中文 | [English](README.md)

一句话说明这个产品做什么、帮谁解决问题、为什么值得关注。

- 核心价值 1：TBD
- 核心价值 2：TBD
- 核心价值 3：TBD

上线前补充截图 / GIF。

快速演示：

```bash
TBD
```

## Hero Section

首屏必须在 10 秒内讲清楚：这是什么、给谁用、解决什么痛点、会产出什么、为什么值得关心、怎么快速试用。

## 问题

TBD。

## 为什么现有方式不够

TBD。

## 这个项目做什么

TBD。请用 `输入 -> 处理 -> 输出` 解释真实产品流程。

## 核心功能

TBD。

## 演示 / 截图

上线前补充截图、GIF、终端演示、前后对比或样例输出图。

## 快速开始

TBD。

## 输入 / 输出示例

TBD。

## 使用场景

TBD。

## 工作原理

TBD。

## 项目结构

TBD。

## 路线图

TBD。未实现功能必须放在路线图，不要写成已实现能力。

## 限制

TBD。限制集中放在这里，前文不要反复自我削弱。

## 许可证

TBD。

## 语言

- 中文：`README.zh-CN.md`
- English：`README.md`

<!--
Status: NOT_STARTED
Stage: {stage_name}
Timestamp: {timestamp}
Bilingual README Requirement: Chinese README must be complete, natural, and consistent with the English claims.
-->
"""
    if artifact == "launch-summary.md":
        return f"""# Launch Summary

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Product Positioning
TBD.

## GitHub Launch Page Gate
- English README complete: TBD
- Chinese README complete: TBD
- Strong first screen: TBD
- Clear repo description: TBD
- Strong GitHub topics: TBD
- Screenshot/GIF plan: TBD
- Demo instructions: TBD
- Sample input/output: TBD
- Limitations grouped near end: TBD
- README claim check passed: TBD

## Final GitHub Assets
- `README.md`
- `README.zh-CN.md`
- `github-description.md`
- `github-topics.md`
- `demo-instructions.md`
- `launch-posts.md`
- `launch-summary.md`

## Launch Decision
Choose one:
- READY_FOR_GITHUB_WITH_APPROVAL
- NEEDS_README_REWRITE
- NEEDS_DEMO_ASSET
- NEEDS_CLAIM_FIX
- DO_NOT_SHIP
"""
    if artifact == "github-description.md":
        return f"""# GitHub Description

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Short Repo Description
TBD. Must be under 160 characters.

## Longer Description
TBD. One paragraph explaining what the product is, who it helps, what pain it solves, and what output it creates.

## Alternative Descriptions
1. TBD
2. TBD
3. TBD

## Claim Check
- Does the description avoid overclaiming? TBD
- Does it name the actual implemented capability? TBD
- Does it avoid irrelevant trending keywords? TBD
"""
    if artifact == "github-topics.md":
        return f"""# GitHub Topics

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Topic Rules
- Use 10-20 topics.
- Include domain-specific keywords.
- Include product-type keywords.
- Avoid irrelevant trending spam.

## Topics
- TBD-topic-1
- TBD-topic-2
- TBD-topic-3
- TBD-topic-4
- TBD-topic-5
- TBD-topic-6
- TBD-topic-7
- TBD-topic-8
- TBD-topic-9
- TBD-topic-10
"""
    if artifact == "core-capability-design.md":
        return f"""# Core Capability Design

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Core Capability
TBD. Define the one non-trivial capability that makes this product more than a UI, checklist, prompt wrapper, or deterministic calculator.

## Why It Is Non-Trivial
TBD. Explain the data processing, automation, integration, import, detection, simulation, or adaptive logic that creates product depth.

## Required Data
TBD. List required real user data, logs, traces, files, APIs, datasets, repos, reviews, or records.

## Data Entry Path
- Demo-only input:
- Acceptable V1 input:
- Real data path:
- Unacceptable shallow input:

## Automation Boundary
- Automated by product:
- User-provided:
- Manual only in demo mode:

## Shallow Failure Mode
TBD. Name what would make this product only a frontend calculator or formatted report.

## Minimum Acceptable V1 Capability
TBD. If this is missing, classify as `EXPERIMENT`, `PARK`, `BUILD_INTERNAL`, or `NEEDS_V2_BEFORE_LAUNCH`.

## V2 Upgrade Path
TBD. Define the import, integration, SDK, proxy, parser, or automation needed before public launch if V1 is incomplete.
"""
    if artifact == "input-automation-map.md":
        return f"""# Input Automation Map

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Ideal Input Path
TBD. Define the lowest-friction real data path, such as log import, trace upload, API connection, SDK, proxy, GitHub Action, or repo parser.

## Acceptable V1 Input Path
TBD. Define the minimum real-data path that can support a public launch.

## Unacceptable Shallow Input Path
- Manual complex JSON as the only main workflow input
- User manually entering all important numbers
- User manually researching prices, token counts, failure rates, or external data

## Import Options
TBD. List CSV, JSONL, log, trace export, GitHub issue/repo, browser export, API, SDK, proxy, or plugin options.

## Automation Options
TBD. List what can be auto-detected, parsed, estimated, validated, or enriched.

## Friction Risks
TBD. Estimate setup steps, user expertise required, and whether a time-poor user would quit before first useful output.

## Input Automation Score
TBD / 10. If score <= 3 and the product depends on structured user input, Q-Gate must return `PIVOT` or `NEEDS_V2_BEFORE_LAUNCH`.
"""
    if artifact == "build-depth-checklist.md":
        return f"""# Build Depth Checklist

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Critical Checks
- Core capability implemented: TBD
- Real data path implemented: TBD
- Custom config implemented: TBD
- Sample data included: TBD
- Input validation implemented: TBD
- Uncertainty handled: TBD
- Robustness/sensitivity implemented: TBD
- Smoke test covers real-data path: TBD
- README does not overclaim: TBD

## Feature Type Classification
- Demo-only features:
- Real user features:
- Mock features:
- Incomplete V2 features:

## Launch Readiness Rule
If any critical item is missing, do not mark build as launch-ready. Use `NEEDS_V2_BEFORE_LAUNCH` when the idea is good but the implementation is too shallow.
"""
    if artifact == "readme-claim-check.md":
        return f"""# README Claim Check

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## GitHub Launch Page Gate
- English README exists: TBD
- Chinese README exists: TBD
- Strong first screen: TBD
- Clear repo description: TBD
- Strong GitHub topics: TBD
- Screenshot/GIF plan: TBD
- Demo instructions: TBD
- Sample input/output: TBD
- Limitations grouped near the end: TBD
- README claim check complete: TBD

## Claim Mapping
| README Claim | Implemented? | Evidence File / Command | Demo Only? | Roadmap? | Revision Needed |
| --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD |

## README Claim Check
- Do not call the product observability, analyzer, monitor, guard, importer, or automation unless that feature exists.
- Explain the implemented analytical method honestly.
- State assumptions and limitations near the end.
- Do not claim AI-powered, Monte Carlo, multi-agent, optimization, forecasting, graph analysis, or advanced analysis unless implemented.
- Do not use method language to hide simple threshold scoring.
- Future roadmap must be labeled as roadmap.
- Demo-only and mock features must be labeled clearly.
- Every major README claim must map to implemented functionality.
- Limitations must be grouped near the end.
- Do not scatter self-sabotaging caveats through the hero, problem, features, or quickstart sections.
- English and Chinese README claims must be consistent.
- README first screen must answer what, who, pain, output, why care, and how to try within 10 seconds.
- Quick Start must work.

## README Structure Requirement
- Hero Section
- Problem
- Why Existing Approaches Are Not Enough
- What This Project Does
- Key Features
- Demo / Screenshots
- Quick Start
- Example Input / Output
- Use Cases
- How It Works
- Project Structure
- Roadmap
- Limitations
- License
"""
    if artifact in {"mvp-prd.md", "technical-spec.md", "acceptance-criteria.md"}:
        return f"""# {title}

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Core Specification
TBD. This synthesis artifact must reference the relevant substage evidence files before it is marked complete.

## Product Depth Requirements
- must-have core capability:
- real data path:
- input automation:
- configuration freshness:
- accuracy / uncertainty:
- import/export support:
- anti-shallow rule:

## Method Core Specification
- method core:
- minimum analytical depth:
- uncertainty handling:
- assumption challenge:
- method-specific tests:
- anti-shallow-scoring rule:
- scenario analysis or sensitivity analysis when relevant:
- user-adjustable assumptions, weights, thresholds, or priorities when relevant:
- confidence or uncertainty explanation:
- recommendation robustness check:
- what would flip the recommendation:

## Implementation Depth Requirements
- parser/data depth:
- UI specificity:
- fixture depth:
- edge case test plan:
- output actionability:
- anti-toy rule:

## Business Workflow Requirements
- required fields:
- optional fields:
- missing-field behavior:
- business constraints modeled:
- source-system presets or flexible mapping:
- action-oriented outputs:
- what-if/sensitivity:
- realistic fixture requirements:
- README honesty requirements:
"""
    if artifact == "bilingual-github-release-plan.md":
        return f"""# Bilingual GitHub Release Plan

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## 1. Release Strategy

- English default branch: main
- Chinese branch name: zh-CN
- Product code localization needed? Default: No.
- GitHub repo metadata language: Default English because description/topics are repo-level.

## 2. English Public Asset

- README source: readme-final.md
- GitHub description: github-description.md
- GitHub topics: github-topics.md
- Demo instructions: demo-instructions.md
- Launch posts: launch-posts.md
- README claim check completed: TBD

## 3. Chinese Branch Asset

- Chinese README source: readme-final-zh-CN.md
- Chinese description copy: github-description-zh-CN.md
- Chinese launch posts: launch-posts-zh-CN.md
- Files allowed to differ from English branch: README and GitHub-facing markdown only.
- Files that must remain unchanged: app/source code, tests, sample schemas, env vars, API routes, commands.

## 4. Branch Procedure

1. Prepare English main branch.
2. Commit product code and English packaging.
3. Create `zh-CN` from the same commit.
4. Replace or add Chinese GitHub-facing docs only.
5. Verify product behavior remains unchanged.
6. Push both branches after explicit approval.

## 5. Secret And Safety Check

- `.env` ignored: TBD
- `.env.example` uses placeholders: TBD
- No API key in README/logs/examples: TBD
- Frontend does not expose secrets: TBD

## 6. Decision

Choose one:
- READY_TO_PUSH_WITH_APPROVAL
- NEEDS_COPY_REVIEW
- NEEDS_SECRET_FIX
- DO_NOT_PUSH
"""
    if artifact == "core-mechanism-design.md":
        return f"""# Core Mechanism Design

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Non-Trivial Mechanism
TBD. Define the mechanism that makes the product more than keyword matching, regex scanning, a static checklist, one prompt, one formula, or a generic Markdown report generator.

## Why It Is Deeper Than Keyword Matching
TBD. Explain whether the product uses an AST parser, schema diff engine, graph model, timeline reconstruction, simulation, confidence scoring, auto-fix patch generation, benchmark, SDK/proxy/plugin, multi-file analysis, or configurable rule engine.

## Data Structures Needed
TBD. Describe entities, relationships, intermediate representations, indexes, graphs, timelines, clusters, traces, route maps, permission maps, or other structured data.

## Algorithms / Parsers / Rules Needed
TBD. List parsing stages, normalization rules, matching algorithms, graph traversal, diff logic, scoring model, or confidence model.

## Edge Cases That Matter
TBD. Include ambiguous input, malformed input, empty input, complex input, multi-file input, duplicated signals, false positives, and no-issue cases.

## Toy-Level Failure Mode
TBD. State what would make this product only a toy analyzer with polished packaging.

## Minimum Mechanism Score
TBD / 10. Non-Trivial Mechanism Depth < 6 blocks TOP_10_PUBLISH.
"""
    if artifact == "ui-specificity-design.md":
        return f"""# UI Specificity Design

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Product-Specific View
TBD. Define the view that only makes sense for this product and this domain.

## Domain-Specific Visualization
TBD. Examples: route diff table, permission matrix, failure timeline, attack path, cost curve, dependency graph, scenario comparison, confidence map, or patch preview.

## Unique Interaction
TBD. Define interactions beyond upload-button-report-output.

## Reused Shell Risk
TBD. If reusing a frontend shell, explain what domain-specific UI was added and why the reuse is justified by deeper core capability.

## UI Specificity Score
TBD / 10. UI Specificity <= 4 blocks TOP_10_PUBLISH.
"""
    if artifact == "fixture-plan.md":
        return f"""# Fixture Plan

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Required Fixture Set
- At least 3 realistic sample inputs:
- At least 5 edge cases:
- At least 1 malformed input case:
- At least 1 complex input case:
- At least 1 negative / no-issue case if relevant:

## Test Coverage Requirement
Tests must cover normal case, edge case, malformed case, empty input or missing field, complex case, and no-issue case if relevant.

## Launch Rule
One toy sample and a happy-path smoke test are not enough for TOP_10_PUBLISH.
"""
    if artifact == "core-logic-depth-report.md":
        return f"""# Core Logic Depth Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Core Logic Depth Score
TBD / 10

## Parser / Data Understanding Depth
TBD / 10

## Non-Trivial Mechanism Evidence
TBD. Cite implemented files, tests, fixtures, data structures, algorithms, and edge-case behavior.

## Keyword / Regex Dependence
TBD. If regex or keyword matching is used, explain the additional depth that makes the product publishable.

## Launch Decision
Choose one:
- PASS_IMPLEMENTATION_DEPTH_GATE
- NEEDS_V2_BEFORE_LAUNCH
- BUILD_INTERNAL
- KILL
"""
    if artifact == "fixture-test-report.md":
        return f"""# Fixture Test Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Fixtures Tested
| Fixture | Type | Expected Behavior | Command/Test | Result |
| --- | --- | --- | --- | --- |
| TBD | normal | TBD | TBD | TBD |
| TBD | edge | TBD | TBD | TBD |
| TBD | malformed | TBD | TBD | TBD |
| TBD | complex | TBD | TBD | TBD |
| TBD | no-issue | TBD | TBD | TBD |

## Edge Case Coverage
TBD. At least 5 edge cases must be documented for a strong public product.

## Test Depth Score
TBD / 10. Test Depth < 5 blocks TOP_10_PUBLISH.
"""
    if artifact == "real-world-depth-design.md":
        return f"""# Real-World Depth Design

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Real-World Depth Gate
TBD. Define what real ecosystem complexity this product must handle before TOP_10_PUBLISH.

## Ecosystem Compatibility Gate
TBD. List supported real-world variants, unsupported variants, and downgrade rules. For npm: package-lock v1/v2/v3, workspaces, monorepos, dev/prod/optional/peer deps, overrides, large lockfiles.

## External Data Integration Gate
TBD. If claiming security, pricing, vulnerability, market, or risk analysis, identify authoritative data sources or state that output is structural risk only.

## Remediation Depth Gate
TBD. Findings must include affected path, severity, confidence, why it matters, suggested direct dependency upgrade, override/resolution option if relevant, and next command/action.

## Real Corpus Benchmark Gate
TBD. Plan realistic projects/fixtures, complex case, large case, node count, edge count, runtime, findings count, and false-positive concerns.

## CI / Automation Readiness Gate
TBD. Define CLI --ci mode, JSON export, Markdown export, SARIF export, GitHub Actions example, or exit-code threshold.

## README Claim Honesty Gate
TBD. State what claims must be avoided unless implemented.
"""
    if artifact == "ecosystem-compatibility-plan.md":
        return f"""# Ecosystem Compatibility Plan

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Supported Variants
TBD

## Unsupported Variants
TBD

## Variant Test Matrix
| Variant | Fixture / Corpus | Expected Behavior | Status |
| --- | --- | --- | --- |
| normal | TBD | TBD | TBD |
| complex | TBD | TBD | TBD |
| large | TBD | TBD | TBD |

## Decision Rule
If only toy samples are supported, block TOP_10_PUBLISH.
"""
    if artifact == "external-data-integration-plan.md":
        return f"""# External Data Integration Plan

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Claims Requiring External Data
TBD. Security, vulnerability, pricing, market, package metadata, deprecation, benchmark, or risk claims need authoritative sources.

## Authoritative Sources
TBD. Examples: npm audit, OSV, GitHub Advisory, package metadata, deprecation info, official pricing pages, official API docs.

## Honest Scope If Not Integrated
TBD. If no external data is used, README must say structural risk / local heuristic / graph triage only.
"""
    if artifact == "real-corpus-benchmark-plan.md":
        return f"""# Real Corpus Benchmark Plan

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Required Corpus
- At least 3 realistic projects or fixtures:
- At least 1 complex case:
- At least 1 large case when relevant:

## Metrics To Record
- node count
- edge count
- runtime
- findings count
- false-positive concerns

## Decision Rule
Toy-only fixtures cannot support TOP_10_PUBLISH.
"""
    if artifact == "business-workflow-map.md":
        return f"""# Business Workflow Map

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Business Workflow Depth Gate
TBD. Explain the current manual workflow and how the product reduces real operating work.

## Current Manual Workflow
- Where data comes from:
- What format it naturally exists in:
- Current workaround:
- Decisions made:
- Bottlenecks:
- Time/cash/risk pressure:

## Decision The User Needs To Make
- What should the user do next?
- What should they do first?
- Why?
- Under what constraint?
- With what risk?
- What changes if assumptions change?

## Output That Reduces Work
TBD. Describe the exact action, priority, export/copy path, and decision support.
"""
    if artifact == "data-sufficiency-map.md":
        return f"""# Data Sufficiency Map

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Data Sufficiency Gate

## Required Fields
TBD

## Optional Fields
TBD

## Estimated Fields
TBD

## Missing-Field Behavior
TBD. State which missing fields break analysis, which downgrade confidence, and which can be estimated.

## Scores
- Data Availability: TBD / 10
- Field Completeness: TBD / 10
- Data Quality Handling: TBD / 10
- Missing Field Robustness: TBD / 10

## Rule
If missing fields silently produce confident output, block TOP_10_PUBLISH.
"""
    if artifact == "constraint-map.md":
        return f"""# Constraint Map

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Business Constraint Gate

## Constraints Considered
- budget:
- time:
- cash flow:
- supplier lead time:
- MOQ:
- storage capacity:
- shelf life:
- labor availability:
- payment status:
- legal/compliance boundary:
- customer relationship risk:
- seasonality:
- uncertainty:
- priority tradeoff:

## Constraints V1 Handles
TBD

## Constraints In Roadmap
TBD

## Rule
TOP_10_PUBLISH requires at least 2 meaningful constraints modeled or explicitly handled.
"""
    if artifact == "source-system-map.md":
        return f"""# Source-System Map

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Source-System Preset Gate

## Likely Source Systems
- Shopify:
- Square:
- QuickBooks:
- Xero:
- Stripe:
- PayPal:
- Etsy:
- WooCommerce:
- generic Excel export:

## Natural Export Formats
TBD

## Known Column Variants
TBD

## Presets Or Flexible Mapping Needed
TBD

## README Requirement
README must state supported input sources honestly. Do not say "supports CSV" as if all CSV files are equal.
"""
    if artifact == "method-fit-map.md":
        return f"""# Method Fit Map

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Disciplinary Method Fit Gate
TBD. Define the discipline or analytical tradition this problem belongs to, such as decision analysis, operations research, accounting workflow, dependency graph analysis, policy rule matching, inventory planning, evidence triage, or another natural domain.

## Methods That Naturally Fit
TBD. List methods that fit because they directly improve the user's decision, reduce uncertainty, model constraints, explain paths, or produce action.

## Methods That Do Not Fit
TBD. Explicitly reject method theater. Do not add Monte Carlo, multi-agent debate, AI classification, graph analysis, or optimization unless the problem actually needs it.

## Minimum Serious Method Core
TBD. Define the minimum analytical mechanism required before this product can be considered a serious PUBLIC_PRODUCT.

## Shallow Failure Mode
TBD. Explain what would make the product only parse input, score a few fields, and generate a report.

## Over-Engineering Failure Mode
TBD. Explain what would make the product more complex without improving the user decision.

## Decision Impact
TBD. Explain how the chosen method changes what the user can decide or do next.
"""
    if artifact == "analytical-core-design.md":
        return f"""# Analytical Core Design

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Core Analytical Mechanism
TBD. Define the model, parser, scoring method, simulation, rule system, graph traversal, utility ranking, sensitivity analysis, confidence logic, or other method implemented by the product.

## User Inputs
TBD. List explicit user inputs and whether they are uploaded, pasted, inferred, configured, or imported.

## Inferred Parameters
TBD. List values the product infers, estimates, normalizes, clusters, parses, ranks, or validates.

## Model / Scoring / Simulation Logic
TBD. Explain formulas, rules, algorithms, thresholds, assumptions, and why they fit the discipline.

## Output Interpretation
TBD. Explain how users should interpret rankings, priorities, probabilities, confidence, flags, or recommendations.

## Better Than Simple Scoring
TBD. Identify exactly what makes the mechanism more serious than threshold scoring or generic report generation.
"""
    if artifact == "uncertainty-and-assumption-map.md":
        return f"""# Uncertainty and Assumption Map

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Uncertain Inputs
TBD. List uncertain values, missing data, external conditions, policy ambiguity, price volatility, demand variance, user behavior assumptions, or model uncertainty.

## Assumptions
TBD. List assumptions that materially affect the recommendation or output.

## Confidence Logic
TBD. Define how confidence is assigned, downgraded, or explained.

## Sensitivity Checks
TBD. Define what changes under optimistic, conservative, or alternate assumptions.

## Assumption Challenge
TBD. Define the devil's-advocate, counterexample, robustness, or contradiction check.

## What Would Flip The Decision
TBD. State what input or assumption changes would alter the top recommendation, priority, or launch decision.
"""
    if artifact == "demand-bias-check.md":
        return f"""# Demand Bias Check

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Principle
Do not preselect the audience. Do not default to developer tools. Do not force non-developer products. Start from broad market demand discovery, then let evidence decide.

## Demand Pools Inspected
| Demand Pool | Sources Checked | Pain Signals | Candidate Opportunities | Evidence Quality | Feasibility | Distribution Path | Likely Product Format |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| Developer / AI builder / technical workflow users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Students / international students / applicants | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Job seekers / career planners | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Creators / content workers / solo operators | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Small business / freelancers | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Personal finance / budgeting / decision-making users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Life admin / family admin / healthcare admin users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Productivity / AI tool users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Education / tutoring / learning users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Emerging niche | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Bias Questions
1. Did we over-sample developer sources?
2. Did we over-weight GitHub/Hacker News because they are easy for Codex?
3. Did we ignore non-developer pain because it is harder to implement?
4. Did we choose a product mainly because it is easy to build?
5. Did we confuse GitHub publishability with actual demand?
6. Did we force a non-developer idea without enough evidence?
7. Did the winning opportunity truly have the strongest evidence?

## Bias Rules
- If more than 60% of sources are developer sources, flag `DEV_SOURCE_BIAS`.
- If more than 70% of candidates are developer tools, require written justification.
- If the final winner is a developer tool, compare it against the top non-developer candidate.
- If the final winner is a non-developer tool, compare it against the top developer candidate.
- The winner must be justified by evidence, not category preference.

## Demand Bias Gates
- Broad Demand Discovery: TBD
- Demand Bias Check: TBD
- Developer Tool Bias Check: TBD
- Cross-Audience Comparison: TBD
- Category-Neutral Product Selection: TBD

## Final Selection Justification
- Why this audience/problem won:
- Evidence supporting the winner:
- Competing opportunities rejected:
- Why developer-tool bias or non-developer bias did not decide the outcome:
- Why this is not merely the easiest thing for Codex to build:
- Why this deserves Product Discovery:

## Decision
Choose one:
- PASS_BIAS_CHECK
- DEV_SOURCE_BIAS_NEEDS_JUSTIFICATION
- CATEGORY_OVERCONCENTRATION_NEEDS_RESEARCH
- NEED_MORE_EVIDENCE
- PARK
- KILL
"""
    if artifact in {"demand-scorecard.md", "opportunity-ranking.md", "batch-shortlist.md", "launch-slot-ranking.md", "classification-table.md"}:
        return f"""# {title}

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Launch Slot Scoring Fields
| Dimension | Score 1-10 | Evidence IDs | Notes |
| --- | ---: | --- | --- |
| User Pain | TBD | TBD | TBD |
| Buyer Value | TBD | TBD | TBD |
| Distribution Leverage | TBD | TBD | TBD |
| Differentiation | TBD | TBD | TBD |
| Demo Pull | TBD | TBD | TBD |
| Expected Star Pull | TBD | TBD | TBD |
| Core Capability Completeness | TBD | TBD | TBD |
| Input Automation Depth | TBD | TBD | TBD |
| Real Data Path Strength | TBD | TBD | TBD |
| Core Logic Depth | TBD | TBD | TBD |
| UI Specificity | TBD | TBD | TBD |
| Non-Trivial Mechanism Depth | TBD | TBD | TBD |
| Ecosystem Compatibility | TBD | TBD | TBD |
| External Data Integration | TBD | TBD | TBD |
| Remediation Depth | TBD | TBD | TBD |
| Real Corpus Benchmark | TBD | TBD | TBD |
| Evidence Breadth Score | TBD | TBD | Must reflect multiple demand pools, not one convenient source category. |
| Cross-Audience Strength Score | TBD | TBD | Compare developer and non-developer opportunities. |
| Source Diversity Score | TBD | TBD | Penalize GitHub-only or HN-only discovery. |
| Demand Specificity Score | TBD | TBD | Pain must be concrete and repeated. |
| Buildability Bias Risk | TBD | TBD | High if selected mainly because Codex can build it easily. |
| GitHub Bias Risk | TBD | TBD | High if selected mainly because GitHub packaging is convenient. |
| Category Overconcentration Risk | TBD | TBD | High if shortlist is dominated by one audience without evidence justification. |
| Data Sufficiency Score | TBD | TBD | Non-developer products must verify natural data availability and missing-field behavior. |
| Business Constraint Depth | TBD | TBD | Operational products need real constraints, not just spreadsheet math. |
| Operational Actionability | TBD | TBD | Outputs must tell the user what to do next, first, why, and with what risk. |
| Source-System Fit | TBD | TBD | CSV/XLSX products must name source systems and mapping/preset needs. |
| What-if Depth | TBD | TBD | Decision-support products need sensitivity or constraint simulation. |
| Realistic Fixture Depth | TBD | TBD | Business products need messy realistic fixtures, not clean toy rows. |
| Business Workflow Depth | TBD | TBD | Measures whether real operating work is reduced. |
| Spreadsheet Trap Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |
| Disciplinary Method Fit | TBD | TBD | Natural method fit; < 6 blocks TOP_10_PUBLISH. |
| Method Depth | TBD | TBD | Analytical products with < 6 cannot be TOP_10_PUBLISH. |
| Analytical Originality | TBD | TBD | Must be more than generic field scoring. |
| Uncertainty Handling | TBD | TBD | Downgrade if uncertainty matters but is ignored. |
| Assumption Challenge | TBD | TBD | Assumptions driving conclusions must be challenged. |
| Multi-Perspective Reasoning | TBD | TBD | Judgment products need scenario, weights, critique, confidence, or synthesis. |
| Method Theater Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |
| Shallow Scoring Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |

## Demand Bias Gates
- Broad Demand Discovery: TBD
- Demand Bias Check: TBD
- Developer Tool Bias Check: TBD
- Cross-Audience Comparison: TBD
- Category-Neutral Product Selection: TBD

## Final Product Selection
- Why this audience/problem won:
- What evidence supports it:
- What competing opportunities were rejected:
- Why developer-tool bias or non-developer bias did not decide the outcome:
- Why this is not merely the easiest thing for Codex to build:
- Why this deserves to proceed to Product Discovery:

## Business Workflow Depth Gates
- Business Workflow Depth Gate: TBD
- Data Sufficiency Gate: TBD
- Business Constraint Gate: TBD
- Source-System Preset Gate: TBD
- Operational Actionability Gate: TBD
- What-if / Constraint Simulation Gate: TBD
- Realistic Business Fixture Gate: TBD

## Disciplinary Method Fit Gates
- Disciplinary Method Fit Gate: TBD
- Method Depth Gate: TBD
- Multi-Perspective Reasoning Gate: TBD
- Method Theater Risk: TBD
- Shallow Scoring Risk: TBD

## Content
TBD. This synthesis artifact must reference the relevant substage evidence files before it is marked complete.
"""
    if artifact == "real-corpus-benchmark-report.md":
        return f"""# Real Corpus Benchmark Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

| Corpus / Fixture | Realism | Node Count | Edge Count | Runtime | Findings Count | False-Positive Concerns | Result |
| --- | --- | ---: | ---: | --- | ---: | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Decision
Choose PASS_REAL_CORPUS_BENCHMARK / NEEDS_MORE_CORPUS / NEEDS_V2_BEFORE_LAUNCH.
"""
    if artifact == "ci-automation-readiness-report.md":
        return f"""# CI Automation Readiness Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Automation Paths
- CLI --ci mode:
- JSON export:
- Markdown export:
- SARIF export:
- GitHub Actions example:
- Exit-code threshold:

## Decision Rule
Developer tools without CLI/export/CI path lose launch readiness.
"""
    if artifact == "remediation-depth-report.md":
        return f"""# Remediation Depth Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Finding Actionability Checklist
- affected path:
- severity:
- confidence:
- why it matters:
- suggested direct dependency upgrade:
- override/resolution option if relevant:
- next command/action:

## Decision Rule
Generic advice is not enough. Products without remediation guidance cannot be TOP_10_PUBLISH.
"""
    if artifact == "data-quality-report.md":
        return f"""# Data Quality Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Data Sufficiency Gate
- Required fields checked:
- Optional fields checked:
- Missing fields detected:
- Estimated fields:
- Confidence downgrade logic:

## Decision
Choose PASS_DATA_SUFFICIENCY_GATE / NEEDS_DATA_HANDLING_FIX / NEEDS_V2_BEFORE_LAUNCH.
"""
    if artifact == "missing-field-report.md":
        return f"""# Missing Field Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Missing Field Behavior
TBD. Record errors, warnings, fallback estimates, confidence downgrades, and blocked analyses.
"""
    if artifact == "business-fixture-report.md":
        return f"""# Business Fixture Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Realistic Business Fixture Gate
- at least 20 realistic rows/items/cases if table-based:
- multiple user/client/vendor/customer groups:
- missing fields:
- malformed values:
- edge cases:
- no-action cases:
- high-priority cases:
- low-priority cases:
- conflicting priorities:

## Decision
Toy clean samples and happy-path-only business samples block SHIP.
"""
    if artifact == "what-if-simulation-report.md":
        return f"""# What-if Simulation Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## What-if / Constraint Simulation Gate
- demand +20% / -20%:
- lead time +20% / -20%:
- budget limit:
- price increase:
- supplier delay:
- seasonality adjustment:

## Decision Impact
TBD. If ranking changes easily under small assumption changes, downgrade confidence.
"""
    if artifact == "business-constraint-report.md":
        return f"""# Business Constraint Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Business Constraint Gate
TBD. Record the real operational constraints modeled in the product and which remain roadmap.

## Operational Actionability Gate
Every major finding should include what to do, why it matters, priority, expected impact, risk, required input/resource, next step, and export/copy/action path.
"""
    if artifact == "method-implementation-report.md":
        return f"""# Method Implementation Report

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Implemented Method
TBD. Name the discipline and method implemented. Do not claim Monte Carlo, AI, multi-agent debate, optimization, graph analysis, or forecasting unless it exists in code.

## Code Locations
| Method Component | File / Function | Evidence |
| --- | --- | --- |
| TBD | TBD | TBD |

## Assumptions Used
TBD. List assumptions, defaults, thresholds, weights, policy rules, formulas, or inferred parameters.

## Uncertainty Handling
TBD. Explain confidence scoring, missing-data handling, estimate labeling, scenario ranges, or limitation notes.

## Sensitivity / Robustness Checks
TBD. Record commands, tests, or analysis that show whether recommendations survive assumption changes.

## Assumption Challenge
TBD. Record devil's advocate, counterexample, alternative weighting, conservative case, or manual review checks.

## Why This Is Not Simple Threshold Scoring
TBD. Explain the non-trivial method core and how it changes user decisions.

## Remaining Shallow Or Incomplete Areas
TBD. Label incomplete methods as roadmap or NEEDS_V2_BEFORE_LAUNCH rather than overclaiming.
"""
    return f"""# {title}

- Stage: {stage_name}
- Status: NOT_STARTED
- Timestamp: {timestamp}

## Content
TBD. This synthesis artifact must reference the relevant substage evidence files before it is marked complete.
"""


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/create_product_folder.py product-011", file=sys.stderr)
        return 2

    product_id = sys.argv[1]
    if not product_id.startswith("product-"):
        print("Product ID must look like product-011", file=sys.stderr)
        return 2

    product_dir = PRODUCTS / product_id
    if product_dir.exists():
        print(f"Refusing to overwrite existing folder: {product_dir}", file=sys.stderr)
        return 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    write(product_dir / "workflow-state.md", f"""# Workflow State

- Product ID: {product_id}
- Workflow architecture: substage-state-machine
- Created: {timestamp}
- Status: NOT_STARTED

Files are memory. Do not rely on chat or model memory.
""")

    for stage in STAGES:
        stage_dir = product_dir / stage.folder
        for substage in stage.substages:
            write(stage_dir / substage.file, substage_content(stage.name, substage, timestamp))
        for file_name in BASE_STAGE_FILES:
            if file_name == "stage-report.md":
                write(stage_dir / file_name, stage_report_content(stage.name, timestamp))
            elif file_name == "checkpoint.md":
                write(stage_dir / file_name, checkpoint_content(product_id, stage.folder, stage.name, timestamp))
            elif file_name == "decision-log.md":
                write(stage_dir / file_name, decision_log_content(stage.name, timestamp))
            elif file_name == "prompt-log.md":
                write(stage_dir / file_name, prompt_log_content(stage.name, timestamp))
            elif file_name == "next-stage-brief.md":
                write(stage_dir / file_name, next_stage_brief_content(stage.name, timestamp))
        for artifact in stage.artifacts:
            write(stage_dir / artifact, artifact_content(artifact, stage.name, timestamp))

    print(f"Created {product_dir}")
    print("Next: complete Stage 0 substages, then run python scripts/update_product_index.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
