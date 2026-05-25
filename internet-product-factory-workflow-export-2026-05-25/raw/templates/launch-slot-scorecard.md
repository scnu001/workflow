# Launch Slot Scorecard

Use this scorecard for every candidate before Q-Gate.

## Classification
- Candidate:
- Proposed classification: `PUBLIC_PRODUCT` / `INTERNAL_FACTORY_TOOL` / `EXPERIMENT` / `PARK` / `KILL`
- Slot decision: `TOP_10_PUBLISH` / `BUILD_DEEPLY_FIRST` / `BUILD_INTERNAL` / `EXPERIMENT` / `PARK` / `KILL`

## Formula
```text
Launch Slot Value =
(User Pain * Buyer Value * Distribution Leverage * Differentiation * Demo Pull * Compound Asset Value * Monetization Optionality)
/
(Build Cost * Maintenance Cost * Competition Density * Trust/Compliance Risk * Launch Slot Opportunity Cost)
```

## Score Table
| Dimension | Score 1-10 | Evidence |
| --- | ---: | --- |
| User Pain | TBD | TBD |
| Buyer Value | TBD | TBD |
| Distribution Leverage | TBD | TBD |
| Differentiation | TBD | TBD |
| Demo Pull | TBD | TBD |
| Compound Asset Value | TBD | TBD |
| Monetization Optionality | TBD | TBD |
| Expected Star Pull | TBD | TBD |
| Distribution Specificity | TBD | TBD |
| Revenue/Lead Path | TBD | TBD |
| Build Cost | TBD | TBD |
| Maintenance Cost | TBD | TBD |
| Competition Density | TBD | TBD |
| Trust/Compliance Risk | TBD | TBD |
| Launch Slot Opportunity Cost | TBD | TBD |
| Depth Penalty | TBD | TBD |
| 30-Minute Copy Risk | TBD | TBD |
| Core Capability Completeness | TBD | TBD |
| Input Automation Depth | TBD | TBD |
| User Friction | TBD | TBD |
| Real Data Path Strength | TBD | TBD |
| Configuration Freshness | TBD | TBD |
| Estimation Accuracy | TBD | TBD |
| Integration Potential | TBD | TBD |
| Frontend Calculator Risk | TBD | TBD |
| Core Logic Depth | TBD | TBD |
| UI Specificity | TBD | TBD |
| Parser/Data Depth | TBD | TBD |
| Edge Case Coverage | TBD | TBD |
| Test Depth | TBD | TBD |
| Output Actionability | TBD | TBD |
| Non-Trivial Mechanism Depth | TBD | TBD |
| Scaffold Reuse Risk | TBD | TBD |
| Toy Implementation Risk | TBD | TBD |
| Ecosystem Compatibility | TBD | TBD |
| External Data Integration | TBD | TBD |
| Remediation Depth | TBD | TBD |
| Real Corpus Benchmark | TBD | TBD |
| CI / Automation Readiness | TBD | TBD |
| UI Domain Specificity | TBD | TBD |
| README Claim Honesty | TBD | TBD |
| Evidence Breadth Score | TBD | TBD |
| Cross-Audience Strength Score | TBD | TBD |
| Source Diversity Score | TBD | TBD |
| Demand Specificity Score | TBD | TBD |
| Buildability Bias Risk | TBD | TBD |
| GitHub Bias Risk | TBD | TBD |
| Category Overconcentration Risk | TBD | TBD |
| Data Sufficiency Score | TBD | TBD |
| Business Constraint Depth | TBD | TBD |
| Operational Actionability | TBD | TBD |
| Source-System Fit | TBD | TBD |
| What-if Depth | TBD | TBD |
| Realistic Fixture Depth | TBD | TBD |
| Business Workflow Depth | TBD | TBD |
| Spreadsheet Trap Risk | TBD | TBD |
| Disciplinary Method Fit | TBD | TBD |
| Method Depth | TBD | TBD |
| Analytical Originality | TBD | TBD |
| Uncertainty Handling | TBD | TBD |
| Assumption Challenge | TBD | TBD |
| Multi-Perspective Reasoning | TBD | TBD |
| Method Theater Risk | TBD | TBD |
| Shallow Scoring Risk | TBD | TBD |

## Hard Rules
- If Demo Pull < 7, cannot be `TOP_10_PUBLISH`.
- If Expected Star Pull < 7, cannot be `TOP_10_PUBLISH`.
- If Depth Penalty > 6, cannot be `TOP_10_PUBLISH`.
- If 30-Minute Copy Risk > 6, cannot be `TOP_10_PUBLISH`.
- If no complete user journey, cannot be `PUBLIC_PRODUCT`.
- If only a checklist/analyzer/parser/config checker, default to `BUILD_INTERNAL`.
- If no distribution channel, `PARK` or `KILL`.
- If no visible demo moment, return to Product Discovery before Build.
- If Core Capability Completeness < 7, cannot be `TOP_10_PUBLISH`.
- If Input Automation Depth < 5, cannot be `TOP_10_PUBLISH` unless explicitly justified.
- If Real Data Path Strength < 5, analytics/simulator/observability products cannot be `TOP_10_PUBLISH`.
- If User Friction > 7, block strong `PUBLIC_PRODUCT` unless value is exceptional.
- If Frontend Calculator Risk > 6, return `PIVOT` or `NEEDS_V2_BEFORE_LAUNCH`.
- If Core Logic Depth < 5, cannot be `PUBLIC_PRODUCT`.
- If Core Logic Depth < 7, cannot be `TOP_10_PUBLISH`.
- If UI Specificity < 5, cannot be `TOP_10_PUBLISH`.
- If Test Depth < 5, cannot be `TOP_10_PUBLISH`.
- If Output Actionability < 6, cannot be `TOP_10_PUBLISH`.
- If Non-Trivial Mechanism Depth < 6, cannot be `TOP_10_PUBLISH`.
- If Toy Implementation Risk > 6, cannot be `TOP_10_PUBLISH`.
- If Scaffold Reuse Risk > 7, require stronger core mechanism evidence.
- A candidate must not win only because it is easier to build.
- A candidate must not win only because it fits GitHub better.
- If Buildability Bias Risk is high, downgrade confidence.
- If GitHub Bias Risk is high, compare against the top non-developer candidate.
- If Category Overconcentration Risk is high, require written evidence-based justification.
- If Spreadsheet Trap Risk > 6, cannot be `TOP_10_PUBLISH`.
- If Business Constraint Depth < 5, operational products cannot be `TOP_10_PUBLISH`.
- If Operational Actionability < 6, cannot be `TOP_10_PUBLISH`.
- If Data Sufficiency Score < 6, require `FIX_BEFORE_SHIP` or `NEEDS_V2_BEFORE_LAUNCH`.
- If a business product is only CSV -> score -> dashboard/report, downgrade it.
- If Method Fit < 6, cannot be `TOP_10_PUBLISH`.
- If Method Depth < 6, analytical products cannot be `TOP_10_PUBLISH`.
- If Shallow Scoring Risk > 6, cannot be `TOP_10_PUBLISH`.
- If Method Theater Risk > 6, cannot be `TOP_10_PUBLISH`.
- If uncertainty matters but is ignored, downgrade launch readiness.
- If assumptions drive recommendations but are never challenged, downgrade launch readiness.
- If the product only parses input, scores a few fields, and generates a report, it cannot be a strong `PUBLIC_PRODUCT`.

## Decision Output
One of:
- `TOP_10_PUBLISH`
- `BUILD_DEEPLY_FIRST`
- `BUILD_INTERNAL`
- `EXPERIMENT`
- `PARK`
- `KILL`

## Rationale
- Why this score is justified:
- Why this deserves or does not deserve a public GitHub slot:
- What evidence would change the decision:

## Product Depth Gates
- Core Capability Gate:
- Input Automation Gate:
- User Friction Gate:
- Configuration Freshness Gate:
- Real Data Path Gate:
- Accuracy / Estimation Quality Gate:
- Frontend Calculator Trap Rule:

## Implementation Depth Gates
- Implementation Depth Gate:
- UI Specificity Gate:
- Core Mechanism Requirement:
- Fixture and Edge Case Depth:
- Output Actionability Gate:

## Real-World Depth Gates
- Real-World Depth Gate:
- Ecosystem Compatibility Gate:
- External Data Integration Gate:
- Remediation Depth Gate:
- Real Corpus Benchmark Gate:
- CI / Automation Readiness Gate:
- README Claim Honesty Gate:

## Demand Bias Gates
- Broad Demand Discovery:
- Demand Bias Check:
- Developer Tool Bias Check:
- Cross-Audience Comparison:
- Category-Neutral Product Selection:

## Business Workflow Depth Gates
- Business Workflow Depth Gate:
- Data Sufficiency Gate:
- Business Constraint Gate:
- Source-System Preset Gate:
- Operational Actionability Gate:
- What-if / Constraint Simulation Gate:
- Realistic Business Fixture Gate:

## Disciplinary Method Fit Gates
- Disciplinary Method Fit Gate:
- Method Depth Gate:
- Multi-Perspective Reasoning Gate:
- Natural discipline / method family:
- Methods that fit:
- Methods that do not fit:
- Assumption challenge:
- What would flip the recommendation:

## Product Selection Justification
- Why this audience/problem won:
- What evidence supports it:
- What competing opportunities were rejected:
- Why developer-tool bias or non-developer bias did not decide the outcome:
- Why this is not merely the easiest thing for Codex to build:
- Why this deserves to proceed to Product Discovery:

## Evidence-First Analysis Requirements
Every major score must cite evidence IDs from substage Evidence Packs.

## Baseline Analysis
- Data source:
- Sample size:
- Variables used:
- Assumptions:
- Formula or scoring method:
- Baseline ranking:
- Interpretation:

## Robustness Check
- Alternative weighting scheme:
- Conservative assumptions:
- Excluding low-reliability evidence:
- Whether the top ranking changed:

## Sensitivity Check
- +20% and -20% key positive factors:
- +20% and -20% key negative factors:
- Higher Depth Penalty:
- Higher 30-Minute Copy Risk:
- Lower Expected Star Pull:
- Lower Demo Pull:

## Error / Outlier Check
- duplicate sources:
- duplicated signals:
- fake-looking evidence:
- low-quality sources:
- outlier scores:
- over-weighted single source:
- unsupported high scores:
- inconsistent classifications:
- missing source IDs:
- missing confidence rating:

## Conservative Decision Rule
If baseline and robustness disagree, choose the more conservative classification. A candidate cannot become `PUBLIC_PRODUCT` if its ranking depends on one fragile assumption.
