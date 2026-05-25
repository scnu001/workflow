# Input Automation Gate

## Principle
Manual JSON is acceptable for demo mode, but not sufficient as the main product experience unless the product is explicitly a developer config tool.

## Score
- 1-2: user manually writes complex JSON or enters all important numbers.
- 3-5: user uploads simple CSV/JSON and the product validates schema.
- 6-7: product imports real logs/traces/exports, auto-detects fields, or estimates missing values.
- 8-9: product integrates with existing tools/APIs and auto-generates structured inputs.
- 10: product observes or captures workflow data automatically through SDK/proxy/plugin/GitHub Action.

## Required Questions
- How does user data enter the system?
- Does the user need to know token counts, prices, failure rates, or internal parameters?
- What is demo-only input?
- What is the real input path?

## Decision Rule
If Input Automation Score <= 3, the product cannot be `TOP_10_PUBLISH`. If the product depends on structured input and score <= 3, Q-Gate must return `PIVOT` or `NEEDS_V2_BEFORE_LAUNCH`.

