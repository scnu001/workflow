# Stage 1: Demand Discovery

## Purpose
Find specific demand signals across broad market demand pools before choosing a product category. Do not produce generic demand analysis, do not default to developer tools, and do not force non-developer ideas without evidence.

## Required Input Files
- previous stage `next-stage-brief.md`
- previous stage `stage-report.md` if needed
- `memory/scoring-calibration.md`
- relevant substage files only if more detail is needed

## Required Substages
1. `01_broad_source_scan.md` - Broad Source Scan
2. `02_pain_signal_extraction.md` - Pain Signal Extraction
3. `03_opportunity_clustering.md` - Opportunity Clustering
4. `04_cross_audience_comparison.md` - Cross-Audience Comparison
5. `05_evidence_quality_ranking.md` - Evidence Quality Ranking
6. `06_product_opportunity_framing.md` - Product Opportunity Framing
7. `07_demand_synthesis.md` - Demand Synthesis

## Required Demand Pools
Before product ideas are selected, Stage 1 must inspect multiple demand pools:

1. Developer / AI builder / technical workflow users
2. Students / international students / applicants
3. Job seekers / career planners
4. Creators / content workers / solo operators
5. Small business / freelancers
6. Personal finance / budgeting / decision-making users
7. Life admin / family admin / healthcare admin users
8. Productivity / AI tool users
9. Education / tutoring / learning users
10. Emerging niche discovered during search

The workflow does not need to choose from every pool, but it must inspect multiple pools before deciding. For each pool, collect if available:
- at least 5 pain signals
- at least 3 source references
- at least 3 candidate opportunities
- evidence quality rating
- feasibility rating
- distribution path
- likely product format

For every non-developer operational opportunity, also record:
- where the user's data lives
- what format it naturally exists in
- what operational constraints matter
- what decision the user needs to make
- what current workaround is used

If evidence is unavailable for a pool, record that clearly. Do not invent non-developer demand just to counterbalance developer-tool bias.

## Required Output Files
- all required substage files
- `raw-signal-log.md`
- `demand-bias-check.md`
- `demand-discovery-report.md`
- `competitor-matrix.md`
- `user-pain-map.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Demand Synthesis Requirements
`07_demand_synthesis.md` must read all previous Stage 1 substages and produce:
- Top 20 demand opportunities
- Top 5 strongest opportunities
- top developer opportunity vs top non-developer opportunity
- weak signals to ignore
- candidate ideas for Stage 2 scoring
- evidence quality notes

## Demand Bias Check
Stage 1 must complete `demand-bias-check.md`.

Ask:
1. Did we over-sample developer sources?
2. Did we over-weight GitHub/Hacker News because they are easy for Codex?
3. Did we ignore non-developer pain because it is harder to implement?
4. Did we choose a product mainly because it is easy to build?
5. Did we confuse GitHub publishability with actual demand?
6. Did we force a non-developer idea without enough evidence?
7. Did the winning opportunity truly have the strongest evidence?

Rules:
- If more than 60% of sources are developer sources, flag `DEV_SOURCE_BIAS`.
- If more than 70% of candidates are developer tools, require written justification.
- If the final winner is a developer tool, compare it against the top non-developer candidate.
- If the final winner is a non-developer tool, compare it against the top developer candidate.
- The winner must be justified by evidence, not category preference.

## Substage Quality Rule
Each completed substage must follow `templates/substage-report-template.md` and contain at least 500 meaningful words. Demand substages must include concrete signals, evidence types, scores, risks, and output to the next substage. If web access is unavailable, log the blocker and use available local data only. Do not fabricate external research.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` compresses the specific demand signals, candidate ideas, evidence quality, weak signals, and required scoring inputs for Stage 2.

## Failure / Blocker Behavior
If evidence is too weak, classify the stage handoff as `NEED_MORE_RESEARCH` or `KILL` rather than advancing with generic analysis. If Stage 1 evidence is overconcentrated in developer sources or any other single category, either justify the source concentration with evidence or return to broad discovery.

## Evidence-First Rule
Demand conclusions must follow Evidence Pack -> Source Log -> Analysis -> Decision. No evidence, no conclusion. Research substages must meet their source quotas or explicitly downgrade confidence and choose `NEED_MORE_EVIDENCE`, `PARK`, or `KILL`. If web access is unavailable, write `WEB_ACCESS_UNAVAILABLE` in Source Log and do not fabricate sources.
