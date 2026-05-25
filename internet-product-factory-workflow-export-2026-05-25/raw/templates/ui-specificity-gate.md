# UI Specificity Gate

A copied frontend shell is not enough. The UI must be designed for the product's actual workflow.

## Questions

- What is the product-specific view?
- What visualization does this product need?
- What interaction is unique to this use case?
- What would make this more than upload-button-report-output?
- Does the UI help the user understand the domain-specific problem?

## Expected Examples

- CI Failure Storyboard: failure timeline, error cluster view, rerun-vs-fix decision panel, suspected root cause section.
- OpenAPI Route Drift Radar: spec-vs-code route diff, missing route table, undocumented route table, breaking-change classification.
- Action Blast Radius: permission risk matrix, trigger risk map, secret exposure path, suggested YAML patch.
- Agent Budget Lab: scenario comparison table, cost curve, sensitivity chart, cost driver breakdown.

## Scoring Rules

- If the UI is only a generic upload + report screen, UI Specificity <= 4.
- UI Specificity <= 4 blocks TOP_10_PUBLISH.
- If the UI is reused, the product must still include domain-specific visualization or workflow interaction.

## Output

Record:

- UI Specificity score
- product-specific views
- reused-shell risk
- missing domain views
- decision: PASS / NEEDS_V2_BEFORE_LAUNCH / BUILD_INTERNAL
