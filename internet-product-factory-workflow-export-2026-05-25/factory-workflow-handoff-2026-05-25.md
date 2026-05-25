# Internet Product Factory Handoff

Generated: 2026-05-25

This document hands off the current `internet-product-factory` workflow to another AI agent.

It summarizes the operating system. Exact source files are included under `raw/`.

## Repository

Root:

```text
E:/aipro/internet-product-factory
```

Important folders:

```text
AGENTS.md
README.md
workflows/
templates/
scripts/
memory/
products/
internal-tools/
handoff/
skills/internet-product-factory-workflow/
```

The factory root may not be a git repository. Do not initialize git at the factory root unless the user explicitly asks.

## Core Philosophy

The factory optimizes for GitHub asset value, not output count.

A product can be small, but it cannot be shallow.

The workflow is not a checklist. It is a forcing function:

```text
Evidence -> Method fit -> Architecture -> Fixtures -> Tests -> Audit -> Packaging -> Memory
```

If an agent only fills files and passes validators, the product can still be bad. The product is good only when the evidence, method, implementation, audit, and packaging form one coherent chain.

## Source Of Truth

Files are memory.

Do not rely on chat memory, Codex memory, or implicit context.

Resume in this order:

1. `products/_product-index.md`
2. current product folder
3. latest `next-stage-brief.md`
4. latest `checkpoint.md`
5. latest `stage-report.md`
6. relevant substage files
7. `memory/*.md`
8. this handoff package

Every important finding, source, score, decision, blocker, assumption, command output, and handoff must be written into Markdown.

## Product Classifications

Every candidate must be classified before build:

- `PUBLIC_PRODUCT`: external-user product that may become a standalone public GitHub repo.
- `INTERNAL_FACTORY_TOOL`: useful to the factory but not worth a public repo slot.
- `EXPERIMENT`: validates a risky mechanism or demand signal without launch.
- `PARK`: promising but evidence is insufficient.
- `KILL`: weak, risky, undifferentiated, or not worth more work.

Stage 3 Q-Gate outputs:

- `CONTINUE`
- `PIVOT`
- `PAUSE`
- `KILL`
- `BUILD_INTERNAL_ONLY`
- `NEEDS_V2_BEFORE_LAUNCH`

`NEEDS_V2_BEFORE_LAUNCH` means the idea may be good, but the current implementation is too shallow to publish.

## Evidence-First Rule

Every research, demand, scoring, Q-Gate, product discovery, audit, and packaging substage follows:

```text
Collect evidence -> Evidence Pack -> Source Log -> Analysis -> Decision
```

No evidence, no conclusion.

No robustness, no ranking.

No demo, no public product.

If evidence is unavailable, write exactly:

```text
Evidence unavailable. This is a hypothesis, not a finding.
```

Each completed substage must contain at least 500 meaningful words. Generic filler does not count.

Analysis must cite evidence IDs. Unsupported claims belong under Weak Hypotheses.

Data-heavy substages require baseline analysis, robustness check, sensitivity check, error/outlier check, interpretation, and decision impact.

## Stage Machine

The canonical schema is `raw/scripts/workflow_schema.py` or live `scripts/workflow_schema.py`.

Stages:

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

Every stage must include:

- all required substage files
- `stage-report.md`
- `checkpoint.md`
- `prompt-log.md`
- `decision-log.md`
- `next-stage-brief.md`

The next stage reads the previous `next-stage-brief.md` first.

## Broad Demand Discovery

Do not preselect the audience.

Do not default to developer tools.

Do not force non-developer products.

Stage 1 must inspect broad demand pools before selecting product ideas:

- Developer / AI builder / technical workflow users
- Students / international students / applicants
- Job seekers / career planners
- Creators / content workers / solo operators
- Small business / freelancers
- Personal finance / budgeting / decision-making users
- Life admin / family admin / healthcare admin users
- Productivity / AI tool users
- Education / tutoring / learning users
- Emerging niches discovered during search

Developer products are allowed if they win the evidence comparison. Non-developer products are allowed if evidence supports them. No category quotas.

Complete `demand-bias-check.md`:

- More than 60% developer sources: flag `DEV_SOURCE_BIAS`.
- More than 70% developer candidates: require written justification.
- If winner is developer, compare against top non-developer candidate.
- If winner is non-developer, compare against top developer candidate.

## Gate Stack

Apply relevant gates before launch:

- Public Product Minimum Bar
- Demand Bias Check
- Product Depth Gates
- Implementation Depth Gates
- Real-World Depth Gates
- Business Workflow Depth Gates
- Disciplinary Method Fit Gates
- GitHub Launch Page Gate
- README Claim Check

Hard lessons:

- A runnable CLI is usually internal unless upgraded.
- A frontend/backend/README/smoke test can still be a manual calculator.
- Reused frontend shell plus shallow rules is not enough.
- A real parser/graph is not enough if only toy examples work.
- A business product is not a spreadsheet analyzer with prettier UI.
- An analytical product needs natural method fit, not fake complexity.
- README polish cannot hide implementation shallowness.

## Build Standard

Product code belongs in:

```text
products/product-XXX/repo/
```

Strong public products usually have:

- local web app or strong interactive surface
- real/natural input path
- non-trivial core mechanism
- product-specific UI view
- realistic fixtures and edge cases
- meaningful tests and smoke test
- user-ready artifact when appropriate
- English and Chinese README
- GitHub metadata
- claim check

Do not build 10 small tools. Build one high-value product first.

If no candidate passes Q-Gate, stop and record why.

## Packaging Standard

Every `PUBLIC_PRODUCT` needs:

- `README.md`
- `README.zh-CN.md`
- `github-description.md`
- `github-topics.md`
- `launch-summary.md`
- `demo-instructions.md`
- `readme-claim-check.md`
- `bilingual-github-release-plan.md`

README must behave like a product landing page:

- Hero
- Problem
- Why existing approaches are not enough
- What this project does
- Key features
- Demo / screenshots
- Quick start
- Example input/output
- Use cases
- How it works
- Project structure
- Roadmap
- Limitations near the end
- License
- Language links

Do not scatter limitations. Do not overclaim. Do not self-sabotage before the visitor understands the product.

## NIM / API Safety

Never hardcode, log, commit, print, or expose real API keys.

NIM products must use environment variables only:

- `NVIDIA_NIM_API_KEY`
- `NVIDIA_NIM_BASE_URL`
- `NVIDIA_NIM_MODEL`

Any API-powered product needs mock/offline mode and no-key smoke test.

## Memory Lessons

Read:

- `raw/memory/global-lessons.md`
- `raw/memory/scoring-calibration.md`
- `raw/memory/product-patterns.md`

Current strongest lessons:

- Product-025 proves execution discipline matters more than file layout.
- Strong outputs are often user-ready artifacts, not dashboards.
- Product-026 proves natural method fit can beat arbitrary AI complexity.
- Practice products should measure real attempts and show unit-level evidence.
- Business products must model real operating constraints.
- Developer tools must prove ecosystem depth and automation readiness.

## Validation

Run or attempt:

```powershell
python -m py_compile scripts/workflow_schema.py scripts/create_product_folder.py scripts/validate_stage_files.py scripts/validate_meaningful_substage.py scripts/audit_workflow_substance.py
python scripts/validate_stage_files.py
python scripts/validate_meaningful_substage.py
python scripts/audit_workflow_substance.py --strict product-XXX
git status
git diff --stat
```

For product repos, run product tests and smoke tests.

Before GitHub launch, run secret scan for `nvapi--`, check `.env`, and confirm README claims match implemented features.

## How To Use This Export

Use `skill/internet-product-factory-workflow` as a portable Codex Skill.

Use `raw/` for exact canonical files.

Use this handoff for onboarding another AI agent.

Use `parallel-line-operating-brief-2026-05-25.md` for a short startup prompt.

