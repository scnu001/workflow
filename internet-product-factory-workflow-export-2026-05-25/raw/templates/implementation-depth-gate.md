# Implementation Depth Gate

A reused scaffold is allowed. A shallow core is not allowed.

This gate asks whether the implementation deserves public launch, not whether the app merely runs.

## Required Scores

| Dimension | Score 1-10 | Evidence | Decision Impact |
| --- | ---: | --- | --- |
| Core Logic Depth | TBD | files/tests | Core Logic Depth < 5 blocks PUBLIC_PRODUCT; < 7 blocks TOP_10_PUBLISH. |
| Parser / Data Understanding Depth | TBD | parser/data model | Low score means the product may only reformat obvious input. |
| Edge Case Coverage | TBD | fixtures/tests | Missing edge cases blocks TOP_10_PUBLISH. |
| Output Actionability | TBD | report examples | Output Actionability < 6 blocks TOP_10_PUBLISH. |
| Test Depth | TBD | test commands | Test Depth < 5 blocks TOP_10_PUBLISH. |
| UI Specificity | TBD | UI screenshots/files | UI Specificity < 5 blocks TOP_10_PUBLISH. |
| Integration / Automation Depth | TBD | import/API/SDK/plugin | Low score requires conservative classification. |
| Non-Trivial Mechanism Depth | TBD | mechanism design | Non-Trivial Mechanism Depth < 6 blocks TOP_10_PUBLISH. |

## Scoring Guide

1-2: toy implementation, few if-statements, simple keyword matching, one sample file, generic report.

3-4: basic rule engine, limited parser, few examples, happy-path tests only.

5-6: structured parser, multiple examples, basic edge cases, meaningful report, some configuration.

7-8: real parser or algorithm, non-trivial data model, edge-case handling, multiple real-like samples, robust tests, actionable output.

9-10: integration, automation, benchmark, plugin, SDK, graph, auto-fix, or advanced analysis with strong real-world applicability.

## Hard Rules

- Frontend is not product depth.
- Smoke test is not product depth.
- README polish is not product depth.
- A static rule scanner is not automatically a public product.
- If the core logic is mostly keyword matching, regex matching, or shallow if-statements, the product cannot be TOP_10_PUBLISH unless it also includes additional depth such as AST parsing, graph analysis, auto-fix, benchmark, real imports, configurable rules, or confidence scoring.

## Decision

Choose one:

- PASS_IMPLEMENTATION_DEPTH_GATE
- NEEDS_V2_BEFORE_LAUNCH
- BUILD_INTERNAL
- EXPERIMENT
- KILL
