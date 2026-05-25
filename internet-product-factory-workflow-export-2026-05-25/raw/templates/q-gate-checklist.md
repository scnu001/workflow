# Q-Gate Checklist

Q-Gate must output only one:
- `CONTINUE`
- `PIVOT`
- `PAUSE`
- `KILL`
- `BUILD_INTERNAL_ONLY`
- `NEEDS_V2_BEFORE_LAUNCH`

## Candidate
- Product:
- Classification entering Q-Gate:
- Launch slot decision entering Q-Gate:

## Hard Questions
| # | Question | Yes/No | Evidence |
| --- | --- | --- | --- |
| 1 | Is the user pain strong enough? | TBD | TBD |
| 2 | Is the user persona specific? | TBD | TBD |
| 3 | Can the value be explained in one sentence? | TBD | TBD |
| 4 | Would a stranger understand the repo within 10 seconds? | TBD | TBD |
| 5 | Would a stranger star the repo after seeing the README first screen? | TBD | TBD |
| 6 | Is there a screenshot-worthy demo moment? | TBD | TBD |
| 7 | Is this more than a thin wrapper around a prompt/checklist? | TBD | TBD |
| 8 | Does the product have a complete user journey? | TBD | TBD |
| 9 | Is it useful if nobody reads the README and only runs the product? | TBD | TBD |
| 10 | Could someone copy 80% of it in 30 minutes? | TBD | TBD |
| 11 | Is the GitHub title clear? | TBD | TBD |
| 12 | Are topics obvious? | TBD | TBD |
| 13 | Is there any legal/security/API/data risk? | TBD | TBD |
| 14 | Does this deserve one of the limited GitHub release slots? | TBD | TBD |
| 15 | Is the core capability actually implemented? | TBD | TBD |
| 16 | Is this more than a frontend calculator? | TBD | TBD |
| 17 | Can the user get value without manually preparing complex JSON? | TBD | TBD |
| 18 | Is there a real data import path? | TBD | TBD |
| 19 | Are key assumptions configurable? | TBD | TBD |
| 20 | Can users update pricing/config/model lists if they change? | TBD | TBD |
| 21 | Does the product reduce user work, or merely reformat user-provided work? | TBD | TBD |
| 22 | Is first useful output achievable within reasonable effort? | TBD | TBD |
| 23 | Would a real target user use this twice? | TBD | TBD |
| 24 | Is this V1 launchable, or only a prototype that needs V2? | TBD | TBD |
| 25 | Is the product more than a reused frontend shell? | TBD | TBD |
| 26 | Is the backend more than a shallow rule scanner? | TBD | TBD |
| 27 | Is the core mechanism non-trivial? | TBD | TBD |
| 28 | Are there multiple realistic fixtures? | TBD | TBD |
| 29 | Are edge cases tested? | TBD | TBD |
| 30 | Is the output actionable enough? | TBD | TBD |
| 31 | Is this merely a toy analyzer with polished packaging? | TBD | TBD |
| 32 | Would a serious developer trust this output? | TBD | TBD |
| 33 | What makes this product hard to replicate in one afternoon? | TBD | TBD |
| 34 | Should this be NEEDS_V2_BEFORE_LAUNCH? | TBD | TBD |
| 35 | Does the product support real-world ecosystem variants? | TBD | TBD |
| 36 | Is the product tested beyond toy fixtures? | TBD | TBD |
| 37 | Does security/risk/vulnerability/pricing/market analysis use authoritative external data? | TBD | TBD |
| 38 | If no external data is used, is the output labeled structural/local/heuristic? | TBD | TBD |
| 39 | Are findings remediable with concrete next actions? | TBD | TBD |
| 40 | Was a real corpus benchmark recorded? | TBD | TBD |
| 41 | Does the tool have CLI/export/CI automation readiness? | TBD | TBD |
| 42 | Does the UI show domain-specific views? | TBD | TBD |
| 43 | Does README claim honesty match implementation depth? | TBD | TBD |
| 44 | Did broad demand discovery inspect multiple demand pools before selection? | TBD | TBD |
| 45 | If the winner is a developer tool, did it beat the top non-developer candidate on evidence? | TBD | TBD |
| 46 | If the winner is non-developer, did it beat the top developer candidate on evidence? | TBD | TBD |
| 47 | Is the winner free of unresolved GitHub Bias Risk? | TBD | TBD |
| 48 | Is the winner free of unresolved Buildability Bias Risk? | TBD | TBD |
| 49 | Is category overconcentration justified by evidence rather than source convenience? | TBD | TBD |
| 50 | Is this more than a spreadsheet analyzer? | TBD | TBD |
| 51 | Does it model real business constraints? | TBD | TBD |
| 52 | Does it reduce real operating work? | TBD | TBD |
| 53 | Are required fields realistic? | TBD | TBD |
| 54 | Does it handle missing data honestly? | TBD | TBD |
| 55 | Does it tell the user what to do next? | TBD | TBD |
| 56 | Does it support source-system exports or flexible mapping? | TBD | TBD |
| 57 | Does it include realistic messy samples? | TBD | TBD |
| 58 | Does it support what-if or sensitivity analysis? | TBD | TBD |
| 59 | Would the target user use this instead of a spreadsheet? | TBD | TBD |
| 60 | What discipline or analytical tradition does this problem belong to? | TBD | TBD |
| 61 | Does the chosen method naturally fit the problem? | TBD | TBD |
| 62 | Is the analytical core deeper than simple thresholds or generic scoring? | TBD | TBD |
| 63 | Are unnecessary or artificial methods explicitly rejected? | TBD | TBD |
| 64 | Does the product handle uncertainty when uncertainty affects the decision? | TBD | TBD |
| 65 | Are assumptions challenged or sensitivity-tested? | TBD | TBD |
| 66 | For recommendation products, does it explain what would flip the recommendation? | TBD | TBD |
| 67 | Is this method theater or fake complexity? | TBD | TBD |

## Decision Rules
- If questions 1-8 are not clearly yes, do not continue.
- If question 10 is yes, downgrade to `INTERNAL_FACTORY_TOOL` unless it is part of a larger suite.
- If no demo moment exists, `PIVOT` or `KILL`.
- If the product is only internally useful, classify as `INTERNAL_FACTORY_TOOL`.
- If risk is high and cannot be mitigated, `KILL`.
- If the idea is good but implementation lacks core capability depth, real data path, input automation, configuration freshness, or estimation quality, return `NEEDS_V2_BEFORE_LAUNCH`.
- If the product is mainly a frontend calculator, return `PIVOT` or `NEEDS_V2_BEFORE_LAUNCH`.
- If the product is mainly a reused shell plus simple keyword/regex rules, return `PIVOT`, `BUILD_INTERNAL_ONLY`, or `NEEDS_V2_BEFORE_LAUNCH`.
- If no non-trivial mechanism exists, do not continue to public launch.
- If realistic fixtures and edge cases are missing, do not mark as `TOP_10_PUBLISH`.
- If only toy fixtures exist, do not mark as `TOP_10_PUBLISH`.
- If external authoritative data is absent, label security/risk/vulnerability/pricing/market outputs as structural/local/heuristic.
- If remediation guidance is generic, do not mark as `TOP_10_PUBLISH`.
- If developer tools lack CLI/export/CI automation, downgrade launch readiness.
- If developer-source overconcentration is unresolved, do not continue without more broad discovery.
- If the winner only wins because it is easy for Codex to build or easy to publish on GitHub, return `PAUSE`, `PIVOT`, or `KILL`.
- If a non-developer idea is forced without stronger evidence than alternatives, return `NEED_MORE_EVIDENCE`, `PARK`, or `KILL`.
- If a non-developer operational product is mainly CSV -> score -> dashboard/report, return `PIVOT`, `NEEDS_V2_BEFORE_LAUNCH`, or `KILL`.
- If Spreadsheet Trap Risk > 6, do not mark as `TOP_10_PUBLISH`.
- If Business Constraint Depth < 5, operational products cannot be `TOP_10_PUBLISH`.
- If Operational Actionability < 6, do not mark as `TOP_10_PUBLISH`.
- If required fields are not naturally available or missing fields silently produce confident output, return `NEEDS_V2_BEFORE_LAUNCH`.
- If no realistic messy fixture or no what-if/sensitivity path exists for a decision-support product, downgrade launch readiness.
- If Method Fit < 6, do not mark as `TOP_10_PUBLISH`.
- If Method Depth < 6 for an analytical product, do not mark as `TOP_10_PUBLISH`.
- If Shallow Scoring Risk > 6 or Method Theater Risk > 6, return `PIVOT`, `NEEDS_V2_BEFORE_LAUNCH`, or `KILL`.
- If recommendations depend on assumptions but the product does not challenge them or explain what would flip the recommendation, do not continue to public launch.

## Output
- Q-Gate decision:
- Classification after Q-Gate:
- Required next action:
- Files to update:
