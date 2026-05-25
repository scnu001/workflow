# Public Product Quality Bar

A product can be small, but it cannot be shallow.

Use this before Q-Gate and before Build Execution. A candidate that fails this bar cannot be classified as `PUBLIC_PRODUCT`.

## 1. User Persona
Who is the product for?

Bad:
- developers
- students
- creators

Good:
- solo developers deciding which GitHub repo to launch today
- AI builders estimating cost and failure risk before running a multi-agent workflow
- indie hackers mining GitHub issues to find repeated product pain points

## 2. External Pain
The product must solve a real user-facing problem, not only improve this factory internally.

Required evidence:
- repeated complaint or pain signal
- existing workaround or competitor
- reason the current workaround is insufficient
- reason an external user would care without knowing this factory exists

## 3. Complete Workflow
Must include:

```text
input -> processing -> result -> export/save/share or clear next action
```

Reject candidates that only produce a one-off answer with no next action.

## 4. Interactive Surface
At least one:
- local web app
- browser demo
- interactive CLI with multi-step flow
- dashboard
- simulator
- report generator
- visualizer

Pure one-shot CLI is not enough unless it is unusually strong.

## 5. Demo Depth
Must include:
- sample input
- sample output
- screenshot-worthy or README-worthy demo
- clear wow or usefulness moment

## 6. Non-Trivial Mechanism
At least one:
- agent pipeline
- simulation
- scoring model
- visualization
- benchmark
- dataset processing
- API integration
- browser automation
- multi-step workflow
- report generation system

For analytical products, this mechanism must also pass the Disciplinary Method Fit Gate. A product that only parses input, scores a few fields, and generates a report is not a strong public product unless that simple method is genuinely the natural fit and the output is highly actionable.

## 7. GitHub Packaging
Must include:
- clear repo name
- clear description
- topics
- README first screen
- quickstart
- examples
- license
- tests or smoke test
- security notes when relevant

## 8. 30-Minute Copy Penalty
Ask:

Could a competent developer copy 80% of this in 30 minutes?

If yes, downgrade to `INTERNAL_FACTORY_TOOL` unless it belongs to a larger product suite.

## 9. Product Depth Penalty
A frontend does not equal product depth.

Manual JSON is acceptable for demo mode, not as the main product experience unless the product is explicitly a developer config tool.

Before `PUBLIC_PRODUCT`, verify:
- core capability is implemented
- real data path exists when the product claims analytics, simulation, observability, workflow analysis, log analysis, issue mining, or behavior analysis
- input automation reduces user work
- changing config/pricing/model lists can be updated
- quantitative output labels uncertainty and assumptions
- README claims do not exceed implemented features

If these fail, use `EXPERIMENT`, `PARK`, or `NEEDS_V2_BEFORE_LAUNCH`.

## Decision
- `PASS_PUBLIC_PRODUCT_BAR`
- `DOWNGRADE_INTERNAL_FACTORY_TOOL`
- `NEEDS_PRODUCT_DISCOVERY`
- `KILL`
