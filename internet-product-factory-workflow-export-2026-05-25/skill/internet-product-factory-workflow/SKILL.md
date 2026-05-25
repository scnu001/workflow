---
name: internet-product-factory-workflow
description: Run or hand off the internet-product-factory workflow for evidence-first product discovery, public-product scoring, Q-Gate, deep build execution, multi-agent audit, bilingual GitHub packaging, launch, feedback, and memory updates. Use when creating the next product, auditing a product run, exporting the workflow to another AI, or enforcing the factory's anti-shallow-product gates.
---

# Internet Product Factory Workflow

Use this skill to run `E:/aipro/internet-product-factory` as a file-driven product factory.

The factory optimizes for public GitHub asset value, not output count. A product can be small, but it cannot be shallow.

## Start Here

1. Set the repository root to `E:/aipro/internet-product-factory`.
2. Read `products/_product-index.md`.
3. Read the latest product folder's `checkpoint.md`, `stage-report.md`, and `next-stage-brief.md`.
4. Read `AGENTS.md`.
5. Read `scripts/workflow_schema.py` for the canonical stage/substage list.
6. Use files as memory. Do not rely on chat memory.

For a complete handoff, read `handoff/workflow-export-2026-05-25/START_HERE.md` if it exists.

## Non-Negotiable Rules

- Files are memory.
- No evidence, no conclusion.
- No robustness, no ranking.
- No demo, no public product.
- Do not preselect the audience.
- Do not default to developer tools.
- Do not force non-developer products.
- Build one high-quality `PUBLIC_PRODUCT`, not many shallow tools.
- If no candidate passes Q-Gate, do not build.
- A frontend is not product depth.
- A smoke test is not product depth.
- README polish is not product depth.
- A manual JSON calculator is not depth.
- A reused shell with shallow rules is not depth.
- A business CSV dashboard is not enough.
- Simple scoring without method fit is not enough.
- Do not push to GitHub unless the user explicitly asks.

## Stage Machine

Run stages in this order:

1. `00_context`
2. `01_demand_discovery`
3. `02_demand_scoring`
4. `03_q_gate`
5. `04_product_discovery`
6. `05_mvp_specification`
7. `06_build_execution`
8. `07_multi_agent_audit`
9. `08_packaging_launch`
10. `09_post_launch_feedback`
11. `10_reflection_memory`

Every stage must end with:

- `stage-report.md`
- `checkpoint.md`
- `prompt-log.md`
- `decision-log.md`
- `next-stage-brief.md`

Read the previous stage's `next-stage-brief.md` before starting the next stage.

For the detailed stage/substage map, read `references/stage-machine.md`.

## Required Classifications

Every candidate must be classified:

- `PUBLIC_PRODUCT`
- `INTERNAL_FACTORY_TOOL`
- `EXPERIMENT`
- `PARK`
- `KILL`

Stage 3 Q-Gate decisions:

- `CONTINUE`
- `PIVOT`
- `PAUSE`
- `KILL`
- `BUILD_INTERNAL_ONLY`
- `NEEDS_V2_BEFORE_LAUNCH`

## Evidence-First Substage Structure

Every completed substage must include:

- Objective
- Why This Matters
- Method
- Evidence Pack
- Source Log
- Analysis
- Scores
- Risks / Weak Points
- Output to Next Substage
- Confidence Rating
- Decision
- Minimum Quality Check

Every completed substage needs at least 500 meaningful words. Generic filler does not count.

Every major claim in Analysis must cite evidence IDs such as `E1`, `E3`, or `E7`. Unsupported claims go under Weak Hypotheses.

If evidence is unavailable, write exactly:

```text
Evidence unavailable. This is a hypothesis, not a finding.
```

For detailed evidence/data rules, read `references/execution-protocol.md`.

## Gate Stack

Apply all relevant gates before `PUBLIC_PRODUCT`, `TOP_10_PUBLISH`, launch, or GitHub publication:

- Public Product Minimum Bar
- Broad Demand Discovery and Demand Bias Check
- Core Capability Gate
- Input Automation Gate
- User Friction Gate
- Configuration Freshness Gate
- Real Data Path Gate
- Accuracy / Estimation Quality Gate
- Frontend Calculator Trap Rule
- Implementation Depth Gate
- UI Specificity Gate
- Core Mechanism Requirement
- Fixture and Edge Case Depth
- Output Actionability Gate
- Real-World Depth Gate
- Ecosystem Compatibility Gate
- External Data Integration Gate
- Remediation Depth Gate
- Real Corpus Benchmark Gate
- CI / Automation Readiness Gate
- Business Workflow Depth Gate
- Data Sufficiency Gate
- Business Constraint Gate
- Source-System Preset Gate
- Operational Actionability Gate
- What-if / Constraint Simulation Gate
- Realistic Business Fixture Gate
- Disciplinary Method Fit Gate
- Method Depth Gate
- Multi-Perspective Reasoning Gate
- GitHub Launch Page Gate
- README Claim Check

For scoring thresholds and blocker rules, read `references/gates-and-scoring.md`.

## Build Standard

Product code belongs in:

```text
products/product-XXX/repo/
```

A strong public product should include:

- local web app or strong interactive surface
- natural real data path
- non-trivial core mechanism
- product-specific UI views
- realistic fixtures and edge cases
- tests and smoke test
- user-ready artifact, not only dashboard/report, when the domain calls for it
- English README and Chinese README
- GitHub description/topics/launch summary
- README claim check

## Packaging Standard

Every `PUBLIC_PRODUCT` needs:

- `README.md`
- `README.zh-CN.md`
- `github-description.md`
- `github-topics.md`
- `launch-summary.md`
- `readme-claim-check.md`

For the required README structure, bilingual branch plan, and anti-overclaim rules, read `references/packaging-and-launch.md`.

## Verification

Before claiming completion, run or attempt:

```powershell
python -m py_compile scripts/workflow_schema.py scripts/create_product_folder.py scripts/validate_stage_files.py scripts/validate_meaningful_substage.py scripts/audit_workflow_substance.py
python scripts/validate_stage_files.py
python scripts/validate_meaningful_substage.py
python scripts/audit_workflow_substance.py --strict product-XXX
git status
git diff --stat
```

For product repos, also run product tests, smoke tests, secret scan for `nvapi--`, and launch-package checks.

For validation details, read `references/validation.md`.

