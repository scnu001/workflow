# Output Actionability Gate

A product report must be actionable. Generic advice is not enough.

## Required For Each Finding

- specific location
- exact affected file / field / line if possible
- severity
- confidence
- explanation
- recommended fix
- false-positive note if relevant
- next action
- optional patch/diff if possible

## Scoring

| Dimension | Score 1-10 | Evidence |
| --- | ---: | --- |
| Location specificity | TBD | TBD |
| Fix specificity | TBD | TBD |
| Confidence clarity | TBD | TBD |
| False-positive handling | TBD | TBD |
| Patch/diff usefulness | TBD | TBD |
| Next-action clarity | TBD | TBD |

## Hard Rules

- If output only says "high risk" or "fix this" without precise action, Output Actionability <= 4.
- TOP_10_PUBLISH requires Output Actionability >= 6.
- README examples must show real report depth, not only a summary card.

## Decision

Choose one:

- PASS_OUTPUT_ACTIONABILITY_GATE
- NEEDS_MORE_SPECIFIC_FINDINGS
- NEEDS_PATCH_OR_LOCATION_DETAIL
- NEEDS_V2_BEFORE_LAUNCH
