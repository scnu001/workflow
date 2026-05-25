# Business Constraint Gate

## Purpose

A business product must model real operating constraints. Without constraints, many products become spreadsheet calculators with a prettier UI.

## Possible Constraints

- budget
- time
- cash flow
- supplier lead time
- MOQ
- storage capacity
- shelf life
- labor availability
- payment status
- legal/compliance boundary
- customer relationship risk
- seasonality
- uncertainty
- priority tradeoff

## Rules

- A business product without constraints is usually just a calculator.
- `TOP_10_PUBLISH` requires at least 2 meaningful constraints modeled or explicitly handled.
- If constraints are not implemented, document them as roadmap and downgrade launch readiness.

## Inventory Minimum

For Restock Radar-type products, require at least:

- purchase budget constraint
- lead time constraint
- MOQ constraint
- stockout risk
- slow mover / overstock concern
