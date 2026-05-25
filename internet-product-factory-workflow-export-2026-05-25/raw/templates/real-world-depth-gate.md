# Real-World Depth Gate

A product can have a real core mechanism and still be too shallow if it only handles toy examples.

This gate checks whether the product survives real ecosystem complexity before it can become `TOP_10_PUBLISH`.

## Required Checks

| Dimension | Score 1-10 | Evidence | Decision Impact |
| --- | ---: | --- | --- |
| Ecosystem Compatibility | TBD | variants tested | Toy-only support blocks TOP_10_PUBLISH. |
| External Data Integration | TBD | authoritative sources | Security/risk/pricing claims need external data or honest structural scope. |
| Remediation Depth | TBD | finding examples | Generic advice blocks TOP_10_PUBLISH. |
| Real Corpus Benchmark | TBD | corpus metrics | Must include realistic, complex, and large cases when relevant. |
| CI / Automation Readiness | TBD | CLI/export/CI proof | Developer tools need automation path. |
| UI Domain Specificity | TBD | UI evidence | Generic upload-report UI is penalized. |
| README Claim Honesty | TBD | claim mapping | Claims cannot exceed implementation depth. |

## Hard Rules

- Products with only toy fixtures cannot be `TOP_10_PUBLISH`.
- Products claiming security, pricing, vulnerability, market, or risk analysis must either use external authoritative data or clearly label output as structural/local/heuristic.
- Products without remediation guidance cannot be `TOP_10_PUBLISH`.
- Developer tools without CLI/export/CI path lose launch readiness.
- Generic upload-and-report UI must be penalized.
- README claims must not exceed implemented depth.

## Decision

Choose one:

- PASS_REAL_WORLD_DEPTH_GATE
- NEEDS_REAL_CORPUS
- NEEDS_EXTERNAL_DATA
- NEEDS_REMEDIATION_DEPTH
- NEEDS_CI_AUTOMATION
- NEEDS_V2_BEFORE_LAUNCH
