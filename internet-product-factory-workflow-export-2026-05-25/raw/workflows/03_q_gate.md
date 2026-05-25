# Stage 3: Q-Gate / Kill-or-Continue

## Purpose
Prevent weak ideas from reaching Build.

## Required Input Files
- Stage 2 `next-stage-brief.md`
- Stage 1 `demand-bias-check.md`
- `classification-table.md`
- `launch-slot-ranking.md`
- `templates/public-product-quality-bar.md`
- `templates/q-gate-checklist.md`

## Required Substages
1. `01_public_product_bar_check.md` - Public Product Bar Check
2. `02_github_visitor_test.md` - GitHub Visitor Test
3. `03_30_minute_copy_test.md` - 30-Minute Copy Test
4. `04_risk_compliance_check.md` - Risk / Compliance Check
5. `05_kill_continue_decision.md` - Kill / Continue Decision

## Required Output Files
- all required substage files
- `q-gate-report.md`
- `pre-mortem.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Decision Output
Output only one:
- `CONTINUE`
- `PIVOT`
- `PAUSE`
- `KILL`
- `BUILD_INTERNAL_ONLY`
- `NEEDS_V2_BEFORE_LAUNCH`

## Substage Quality Rule
Each completed Q-Gate substage must follow `templates/substage-report-template.md` and contain at least 500 meaningful words. The evidence must be specific enough to justify continuing, pivoting, pausing, killing, or routing to internal tools.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` states the Q-Gate decision, classification after Q-Gate, public-product bar result, copy-risk result, risk/compliance result, and exact next-stage instructions.

## Failure / Blocker Behavior
If `KILL`, update `memory/failed-ideas.md` and stop product build. If `BUILD_INTERNAL_ONLY`, route to `internal-tools/` and do not consume a public GitHub slot.

If `NEEDS_V2_BEFORE_LAUNCH`, keep the idea as promising but stop publication/build-to-launch claims until the missing core capability, real data path, automation, configuration freshness, or estimation quality is implemented.

## Category Bias Check
Before `CONTINUE`, Q-Gate must verify that the selected candidate did not win by default audience bias.

Required checks:
- If the winner is a developer tool, compare it against the strongest non-developer candidate from Stage 1 and Stage 2.
- If the winner is a non-developer product, compare it against the strongest developer candidate from Stage 1 and Stage 2.
- Confirm the decision is based on evidence quality, pain intensity, feasibility, distribution, demo potential, and product depth.
- Confirm the product was not selected mainly because it is easy for Codex to build.
- Confirm the product was not selected mainly because it is easy to package on GitHub.

If category bias is unresolved, return `PAUSE`, `PIVOT`, or `KILL` rather than `CONTINUE`.

## Evidence-First Rule
Q-Gate decisions must cite evidence IDs and source substages. A candidate cannot pass Q-Gate mainly on `LOW` or `SPECULATIVE` confidence. A candidate cannot become `PUBLIC_PRODUCT` unless demand evidence and demo potential are at least `MEDIUM`. No evidence, no conclusion.

## Product Depth Q-Gate Questions
1. Is the core capability actually implemented?
2. Is this more than a frontend calculator?
3. Can the user get value without manually preparing complex JSON?
4. Is there a real data import path?
5. Are key assumptions configurable?
6. Can users update pricing, config, model lists, limits, or external data if they change?
7. Does the product reduce user work, or merely reformat user-provided work?
8. Is first useful output achievable within reasonable effort?
9. Would a real target user use this twice?
10. Is this V1 launchable, or only a prototype that needs V2?

## Implementation Depth Q-Gate Questions
1. Is the product more than a reused frontend shell?
2. Is the backend more than a shallow rule scanner?
3. Is the core mechanism non-trivial?
4. Are there multiple realistic fixtures?
5. Are edge cases tested?
6. Is the output actionable enough?
7. Is this merely a toy analyzer with polished packaging?
8. Would a serious developer trust this output?
9. What makes this product hard to replicate in one afternoon?
10. Should this be `NEEDS_V2_BEFORE_LAUNCH`?

If the core logic is mostly keyword matching, regex matching, or shallow if-statements without additional parser, graph, benchmark, auto-fix, confidence, or fixture depth, Q-Gate must return `NEEDS_V2_BEFORE_LAUNCH`, `BUILD_INTERNAL_ONLY`, `PIVOT`, or `KILL`.

## Real-World Depth Q-Gate Questions
1. Does the product support real-world ecosystem variants?
2. Is the product tested beyond toy fixtures?
3. If it claims security/risk/vulnerability/pricing/market analysis, does it use authoritative external data?
4. If no external data is used, is the output clearly labeled structural/local/heuristic?
5. Are findings remediable with concrete next actions?
6. Was a real corpus benchmark recorded?
7. Does the tool have CLI/export/CI automation readiness?
8. Does the UI show domain-specific views rather than generic upload/report?
9. Does README claim honesty match implementation depth?
10. Should this be `NEEDS_V2_BEFORE_LAUNCH` until real-world depth exists?

## Business Workflow Q-Gate Questions
For non-developer operational products, ask:
1. Is this more than a spreadsheet analyzer?
2. Does it model real business constraints?
3. Does it reduce real operating work?
4. Are required fields realistic?
5. Does it handle missing data honestly?
6. Does it tell the user what to do next?
7. Does it support source-system exports or flexible mapping?
8. Does it include realistic messy samples?
9. Does it support what-if or sensitivity analysis?
10. Would the target user use this instead of a spreadsheet?

If the product is CSV -> score -> dashboard/report with generic recommendations, Q-Gate must return `PIVOT`, `NEEDS_V2_BEFORE_LAUNCH`, or `KILL`.

## Disciplinary Method Fit Q-Gate Questions
For analytical, decision-support, risk, prioritization, planning, or recommendation products, ask:
1. What discipline or analytical tradition does this problem belong to?
2. Does the chosen method naturally fit the problem?
3. Is the analytical core deeper than simple thresholds or generic scoring?
4. Which methods are unnecessary or artificial?
5. What is the minimum serious method core for this product?
6. Does the product handle uncertainty when uncertainty affects the decision?
7. Are assumptions challenged or sensitivity-tested?
8. If the product recommends an action, does it explain what would flip the recommendation?
9. Is this method theater or fake complexity?
10. Would a domain-aware user respect the analysis?

If Method Fit < 6, Method Depth < 6 for an analytical product, Shallow Scoring Risk > 6, or Method Theater Risk > 6, Q-Gate must return `PIVOT`, `NEEDS_V2_BEFORE_LAUNCH`, `BUILD_INTERNAL_ONLY`, or `KILL`.
