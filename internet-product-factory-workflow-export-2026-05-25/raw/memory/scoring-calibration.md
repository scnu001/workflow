# Scoring Calibration

Last updated: 2026-04-27

## 2026-05-03: Execution Quality Calibration

Add a new scoring lens: `Workflow Substantive Completion Score`.

This score distinguishes "files exist" from "the workflow actually reasoned." A completed public product should score high only when Stage 1-5 evidence, method design, architecture, fixture planning, and risk mitigation are substantively complete before build. A product with many scaffold files still marked `Status: NOT_STARTED`, heavy `TBD` residue, or post-hoc gate language should be downgraded even if `validate_stage_files.py` passes.

Reward:
- authority-source moat
- generated user-ready artifact rather than dashboard/report only
- modular method architecture
- fixture matrix with edge, malformed, complex, no-issue, and jurisdiction/source variants
- explicit regulatory, legal, privacy, and safety mitigations when relevant
- domain-specific UI that exposes the actual method
- source-backed Stage 1-3 decisions completed before build

Penalize:
- scaffold-complete-but-substance-light workflow records
- one-module core implementation when the domain clearly has multiple concepts
- one-test-file coverage for a multi-step product
- easy/safe topic selection when stronger evidence supports a harder product
- dashboard/report output when the user needs a letter, packet, patch, calendar, decision record, or filing artifact
- treating validator success as equivalent to product depth
- backfilling stage files after build without evidence that they shaped implementation

Rule: `Workflow Substantive Completion Score < 7` blocks `TOP_10_PUBLISH` and should prevent claiming the product completed the full workflow, even if the app runs and the structural validator passes.

## product-001
LaunchLint scored 72/100. This was enough to continue, but future scoring should:
- Penalize competitor density more explicitly.
- Require stronger proof for willingness to pay.
- Treat GitHub/demo value as separate from distribution success.
    - Add a "can be launched with current local tooling and authenticated accounts" readiness check before Stage 8.
    - Add a Stage 8 metadata readiness check: repo description clarity, topics, README first-screen clarity, and search keywords.

## Daily Launch Slot Calibration
New operating constraint:

- Estimated production capacity: about 100 candidate projects/day.
- Public GitHub publishing cap: 10 repos/day.
- Stage 2 must optimize for expected return per GitHub slot, not just build speed.

### Updated Scoring Principle
Do not reward a product mainly because it is easy to build. Ease of build is useful only after the idea clears a value threshold.

### Launch Slot Value Formula
```text
Launch Slot Value =
(User Pain * Buyer Value * Distribution Leverage * Differentiation * Demo Pull * Compound Asset Value * Monetization Optionality)
/
(Build Cost * Maintenance Cost * Competition Density * Trust/Compliance Risk * Launch Slot Opportunity Cost)
```

### Slot Decisions
- `TOP_10_PUBLISH`: worth one of today's 10 GitHub slots.
- `BUILD_INTERNAL`: useful for the factory/toolchain, but not worth public launch by default.
- `PARK`: promising but needs more evidence.
- `KILL`: weak demand, weak upside, or low slot ROI.

### Retrospective On LaunchLint
LaunchLint was successful as a workflow proof and internal factory utility. Under the new model, it is not automatically a Top 10 public launch candidate because it is simple, competitor-adjacent, and has unclear monetization. It should be classified as `BUILD_INTERNAL` or `PUBLISH_IF_SLOT_AVAILABLE`.

### New Minimum Bar
Public GitHub pushes should favor projects with:
- stronger user pain
- clearer novelty or differentiation
- greater star/fork/comment potential
- stronger distribution channel
- monetization or lead-generation path
- compound value across future products

## Daily Batch 2026-04-27 Calibration
Observed scores were too compressed: the nine new repos landed between 80 and 89. That makes ranking less useful when only 10 slots exist.

Next scoring version should add:
- `Expected Star Pull`: likelihood that a GitHub visitor immediately understands and stars the repo.
- `Demo Depth`: whether the repo can show a compelling before/after output, not just a simple text report.
- `Distribution Specificity`: named communities, search keywords, and launch angles.
- `Revenue/Lead Path`: whether the tool can become a paid product, consulting lead, newsletter asset, or API consumer.
- `Depth Penalty`: subtract points for utilities that are easy to clone or too small to feel valuable.

The next Top 10 should include at least 3 products with stronger technical depth or visible demos, not only quick CLIs.

## Post-Deletion Calibration
All 10 GitHub repos from the first daily batch were deleted after user review. Scoring must become harsher:
- A product cannot earn a public slot just because it is testable and quick.
- Add a hard Q-Gate question: "Would this repo still look valuable if a stranger saw only the title, topics, and README first screen?"
- Add a public-slot minimum: at least one of visible demo depth, unique dataset/workflow, real API leverage, painful workflow automation, or credible monetization path.
- Downgrade generic analyzers/checklists unless they are bundled into a stronger product suite.

## Required Public Slot Gates
- `Demo Pull` must be at least 7.
- `Expected Star Pull` must be at least 7.
- `Depth Penalty` must be 6 or lower.
- `30-Minute Copy Risk` must be 6 or lower.
- A product without a complete user journey cannot be `PUBLIC_PRODUCT`.
- A product with no distribution channel must be `PARK` or `KILL`.
- A checklist/analyzer/parser/config checker is `BUILD_INTERNAL` by default.

## Substage Evidence Calibration
If a candidate only looks good after generic analysis but fails under substage evidence, downgrade it.

Stage-level confidence is no longer enough. The scoring decision must survive the individual substage checks for user pain, demo pull, expected star pull, build and maintenance cost, differentiation, copy risk, monetization, and distribution. Weak substages should lower the final launch-slot decision even if the synthesized report sounds persuasive.

## Evidence And Robustness Calibration
If a candidate looks good only after generic analysis, downgrade it.

If a candidate loses under conservative assumptions, downgrade it.

If a candidate's `PUBLIC_PRODUCT` classification depends on one fragile source, one optimistic score, or one untested demo assumption, downgrade it to `PARK`, `EXPERIMENT`, or `INTERNAL_FACTORY_TOOL`.

`LOW` or `SPECULATIVE` confidence cannot carry Q-Gate. Demand evidence and demo potential must be at least `MEDIUM` before a candidate can become `PUBLIC_PRODUCT`.

## 2026-04-27 Calibration From Product-011

A candidate that survives stricter evidence and robustness checks can be built locally even without public launch. Expected Star Pull should remain provisional until GitHub publication. If a cost product lacks scenario comparison, sensitivity checks, or a visible dashboard, downgrade it to INTERNAL_FACTORY_TOOL.

## 2026-04-27 Product Depth Penalties

Add penalties for:
- manual structured input burden
- no real data import
- hardcoded or stale config
- weak estimation accuracy from manually assumed inputs
- frontend calculator risk
- README overclaiming

If a product looks good only because the user manually supplied all important values, downgrade it to `EXPERIMENT`, `PARK`, or `NEEDS_V2_BEFORE_LAUNCH`. `TOP_10_PUBLISH` requires core capability depth, low enough input friction, and a real data path when the product claims analytics, simulation, observability, workflow analysis, log analysis, or behavior analysis.

## 2026-04-27 Product-011 V2 Calibration

Manual-JSON calculator risk can be repaired when the product adds a real data path and confidence-aware analysis. For analytics/simulator products, upgrade scoring only when these are implemented and tested:
- import path for realistic user data
- automatic parsing or extraction
- editable/importable configuration
- visible uncertainty labels
- baseline plus conservative/optimized/fallback scenarios
- sensitivity to changing prices or assumptions
- smoke test that covers imported data

Agent Budget Lab V2 clears the previous `NEEDS_V2_BEFORE_LAUNCH` blocker locally, but public launch scoring still needs final browser QA and GitHub packaging review.

## 2026-04-28: Workflow File Import Beats Manual Configuration

For developer tools, raise scores when the product reads real repository artifacts such as `.github/workflows` and lowers the user's preparation burden. Keep copy-risk and competition penalties when the first version uses heuristic parsing or overlaps with mature scanners.

## 2026-04-28: Implementation Depth Penalties

Add penalties for copied frontend shell, shallow rule scanner, keyword/regex-only logic, one toy sample, happy-path-only smoke test, generic Markdown output, no product-specific UI view, no non-trivial mechanism, no edge-case coverage, and low output actionability. `Core Logic Depth < 5` blocks `PUBLIC_PRODUCT`; `Core Logic Depth < 7`, `UI Specificity < 5`, `Test Depth < 5`, `Output Actionability < 6`, `Non-Trivial Mechanism Depth < 6`, or `Toy Implementation Risk > 6` blocks `TOP_10_PUBLISH`.

## 2026-04-28: Real-World Depth Penalties

Add penalties for toy-only ecosystem support, no external authoritative data for security/risk/vulnerability/pricing/market claims, generic remediation advice, no real corpus benchmark, no large/complex case, no CLI/export/CI path, generic upload-report UI, and README overclaiming. Products with only toy fixtures cannot be `TOP_10_PUBLISH`. Developer tools without CLI/export/CI automation lose launch readiness.

## 2026-04-28: Demand Bias Calibration

Penalize:
- GitHub-only discovery
- developer-source overconcentration
- Hacker News / GitHub evidence convenience bias
- buildability-driven product choice
- choosing products because they are easy for Codex
- confusing GitHub publishability with actual demand
- category quotas that force weak non-developer ideas

Reward:
- source diversity
- repeated pain signals across communities
- strong evidence quality
- clear user urgency
- demand specificity
- feasible but non-trivial product depth
- honest comparison across developer and non-developer categories

If more than 60% of sources are developer sources, flag `DEV_SOURCE_BIAS`. If more than 70% of candidates are developer tools, require written justification. A candidate should not win only because it is easier to build or easier to package on GitHub.

## 2026-04-28: GitHub README Packaging Calibration

Penalize:
- README starts with installation instead of value
- no screenshot/GIF/demo/output example
- generic product description
- scattered limitations
- no Chinese README
- weak repo description
- poor GitHub topics
- roadmap mixed with implemented features
- overclaiming
- self-sabotaging caveats before the visitor understands the product

Reward:
- strong first screen
- clear pain and differentiation
- concrete example output
- bilingual README
- honest but confident positioning
- clean GitHub metadata
- star-worthy demo
- limitations grouped near the end

`TOP_10_PUBLISH` should require a launch page that a stranger can understand in 10 seconds. A working product with weak GitHub presentation should be classified as `NEEDS_README_REWRITE`, `NEEDS_DEMO_ASSET`, or `NEEDS_CLAIM_FIX` before publication.

## 2026-04-28: Business Workflow Depth Calibration

Penalize:
- spreadsheet analyzer with web UI
- no business constraints
- no source-system fit
- no data sufficiency check
- no missing-field confidence downgrade
- generic recommendations
- toy clean samples
- no what-if mode
- pretending "CSV support" means all business exports work

Reward:
- realistic export handling
- flexible mapping
- budget, time, cash, supplier, legal, or operational constraint modeling
- action-oriented output
- source-system presets
- missing data honesty
- realistic messy samples
- decision-impact sensitivity

For non-developer operational products, `Spreadsheet Trap Risk > 6`, `Business Constraint Depth < 5`, or `Operational Actionability < 6` blocks `TOP_10_PUBLISH`. `Data Sufficiency Score < 6` requires `FIX_BEFORE_SHIP` or `NEEDS_V2_BEFORE_LAUNCH`.

## 2026-04-28: Chargeback Evidence Calibration

Reward payment-dispute products when they model processor deadline, amount at risk, reason-code evidence requirements, tracking/refund/message evidence, and confidence downgrade for missing fields. Penalize them if they only track disputes in a table, overclaim win probability, or imply processor API/OCR integration without implementation.

## 2026-04-30: Method Fit Calibration

Reward:
- natural disciplinary method fit
- multi-perspective reasoning when the problem involves judgment or tradeoffs
- uncertainty handling
- sensitivity analysis
- assumption challenge
- decision-impact modeling
- method-specific tests
- clear explanation of what would flip a recommendation

Penalize:
- simple threshold scoring
- fake complexity
- arbitrary Monte Carlo
- generic AI wrappers
- shallow scorecards
- recommendations without robustness checks
- methods that do not fit the problem
- formal method language used to disguise parse -> score -> report products

`Method Fit < 6`, `Method Depth < 6` for analytical products, `Method Theater Risk > 6`, or `Shallow Scoring Risk > 6` blocks `TOP_10_PUBLISH`.

## 2026-05-01: Product-025 Calibration Updates

- Distinguish Demo Pull (planned) from Demo Pull (with-asset) when demo asset is operator-gated. Stage 7 reviewer should confirm asset existence before final scoring.
- For regulated-domain consumer products (healthcare, immigration, tax, court), weight Source Authority >= 9 only when federal/government source is primary anchor. Vendor blogs cap at 5; aggregator commentary cap at 7.
- Add Prior Shape Resemblance Risk hard rule (<= 4) at Q-Gate. Operationalizes "do not anchor on prior products" as a numeric rule rather than a soft preference.
## 2026-05-03: Practice Product Calibration

Reward practice products that measure the user's real attempt, compare it against a domain-specific reference, show unit-level evidence, label uncertainty, and generate a next-practice action. Penalize products that only return a generic score, hide the analysis, use arbitrary AI judging, or add advanced methods that do not fit the discipline.

New scoring hint: `Natural Method Practice Depth` 1-10. Requires real attempt intake, discipline-specific measurement, reference comparison, confidence logic, and action-oriented feedback.
