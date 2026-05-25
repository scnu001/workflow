# Gates And Scoring Reference

Use conservative classification. If a baseline score says publish but a depth gate fails, downgrade.

## Public Product Minimum Bar

Requires:

- clear persona
- clear external pain
- complete user journey
- interactive surface
- visible demo moment
- sample input/output
- non-trivial core mechanism
- GitHub positioning
- strong README first screen
- quickstart
- tests or smoke test
- low 30-minute copy risk

Thin tools default to `INTERNAL_FACTORY_TOOL`: checklist tools, simple analyzers, README optimizers, config checkers, `.env` sync, log summarizers, prompt wrappers, one-file CLIs, simple parsers, basic scoring scripts.

## Broad Demand Discovery / Bias

Do not preselect audience. Inspect multiple demand pools. Developer tools are allowed only when they win on evidence.

Score:

- Evidence Breadth Score
- Cross-Audience Strength Score
- Source Diversity Score
- Demand Specificity Score
- Buildability Bias Risk
- GitHub Bias Risk
- Category Overconcentration Risk

Rules:

- More than 60% developer sources: flag `DEV_SOURCE_BIAS`.
- More than 70% developer candidates: require written justification.
- Final winner must compare against top opposite-category candidate.
- Do not choose products only because they are easy to build or easy to publish on GitHub.

## Product Depth Gates

Score:

- Core Capability Completeness
- Input Automation Depth
- User Friction
- Real Data Path Strength
- Configuration Freshness
- Estimation Accuracy
- Integration Potential
- Frontend Calculator Risk

Rules:

- Core Capability Completeness < 7 blocks `TOP_10_PUBLISH`.
- Input Automation Depth <= 3 blocks `TOP_10_PUBLISH`.
- Input Automation Depth < 5 blocks `TOP_10_PUBLISH` unless explicitly justified.
- Real Data Path Strength < 5 blocks analytics/simulator/observability products.
- User Friction > 7 blocks `PUBLIC_PRODUCT` unless value is exceptional.
- Frontend Calculator Risk > 6 forces `PIVOT` or `NEEDS_V2_BEFORE_LAUNCH`.
- Manual JSON as the only main input blocks strong public launch unless the product is explicitly a developer config tool.

## Implementation Depth Gates

Score:

- Core Logic Depth
- UI Specificity
- Parser/Data Depth
- Edge Case Coverage
- Test Depth
- Output Actionability
- Non-Trivial Mechanism Depth
- Scaffold Reuse Risk
- Toy Implementation Risk

Rules:

- Core Logic Depth < 5 blocks `PUBLIC_PRODUCT`.
- Core Logic Depth < 7 blocks `TOP_10_PUBLISH`.
- UI Specificity < 5 blocks `TOP_10_PUBLISH`.
- Test Depth < 5 blocks `TOP_10_PUBLISH`.
- Output Actionability < 6 blocks `TOP_10_PUBLISH`.
- Non-Trivial Mechanism Depth < 6 blocks `TOP_10_PUBLISH`.
- Toy Implementation Risk > 6 blocks `TOP_10_PUBLISH`.
- If core logic is mostly keyword/regex/if-statements, require AST, graph analysis, auto-fix, benchmark, real imports, confidence scoring, configurable rules, or regression tests over multiple fixtures.

## Real-World Depth Gates

Check:

- Ecosystem Compatibility
- External Data Integration
- Remediation Depth
- Real Corpus Benchmark
- CI / Automation Readiness
- UI Domain Specificity
- README Claim Honesty

Rules:

- Toy-only fixtures block `TOP_10_PUBLISH`.
- Security/risk/vulnerability/pricing/market claims need authoritative external data or must be labeled structural/local/heuristic.
- Developer tools need CLI/export/CI path.
- Generic upload-report UI is penalized.
- README claims cannot exceed implementation depth.

## Business Workflow Depth Gates

Score:

- Data Sufficiency Score
- Business Constraint Depth
- Operational Actionability
- Source-System Fit
- What-if Depth
- Realistic Fixture Depth
- Business Workflow Depth
- Spreadsheet Trap Risk

Rules:

- Spreadsheet Trap Risk > 6 blocks `TOP_10_PUBLISH`.
- Business Constraint Depth < 5 blocks `TOP_10_PUBLISH` for operational products.
- Operational Actionability < 6 blocks `TOP_10_PUBLISH`.
- Data Sufficiency Score < 6 requires fix before ship or `NEEDS_V2_BEFORE_LAUNCH`.
- Missing fields must produce confidence downgrade and warnings, not confident output.

## Disciplinary Method Fit Gates

Score:

- Disciplinary Method Fit
- Method Depth
- Analytical Originality
- Uncertainty Handling
- Assumption Challenge
- Multi-Perspective Reasoning
- Method Theater Risk
- Shallow Scoring Risk

Rules:

- Method Fit < 6 blocks `TOP_10_PUBLISH`.
- Method Depth < 6 blocks analytical `TOP_10_PUBLISH`.
- Method Theater Risk > 6 blocks `TOP_10_PUBLISH`.
- Shallow Scoring Risk > 6 blocks `TOP_10_PUBLISH`.
- Do not force Monte Carlo, multi-agent debate, AI wrappers, or optimization when the domain does not naturally require them.

## Q-Gate

Allowed outputs:

- `CONTINUE`
- `PIVOT`
- `PAUSE`
- `KILL`
- `BUILD_INTERNAL_ONLY`
- `NEEDS_V2_BEFORE_LAUNCH`

If `KILL`, write to `memory/failed-ideas.md` and stop build.

If `BUILD_INTERNAL_ONLY`, route to `internal-tools/`.

If `NEEDS_V2_BEFORE_LAUNCH`, preserve the idea but do not publish as a strong public product.

