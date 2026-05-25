# Method Depth Gate

## Scorecard

| Dimension | Score 1-10 | Evidence | Notes |
| --- | ---: | --- | --- |
| Method Fit | TBD | TBD | Does the method naturally match the problem? |
| Method Depth | TBD | TBD | Is the method more than simple thresholds or generic scoring? |
| Uncertainty Handling | TBD | TBD | Are uncertain inputs, estimates, and confidence explained? |
| Assumption Challenge | TBD | TBD | Are important assumptions challenged or stress-tested? |
| Cross-Validation | TBD | TBD | Are outputs checked through alternate evidence, scenarios, or tests? |
| Decision Impact | TBD | TBD | Does the method materially improve what the user decides or does next? |

## Hard Rules

- Method Fit < 6 blocks `TOP_10_PUBLISH`.
- Method Depth < 6 blocks `TOP_10_PUBLISH` for analytical products.
- If the product only uses simple thresholds and generic scoring, it cannot be a strong `PUBLIC_PRODUCT`.
- If an advanced method is added but does not naturally fit the problem, downgrade Method Fit.
- If uncertainty matters but is ignored, downgrade launch readiness.
- If assumptions drive the conclusion but are never challenged, downgrade launch readiness.

## Failure Modes

- Simple threshold scoring wrapped in formal language.
- Arbitrary Monte Carlo when the problem is deterministic.
- A generic AI wrapper pretending to be domain analysis.
- A scorecard whose weights are never justified or sensitivity-tested.
- Recommendations without confidence, caveats, or assumption-flip analysis.

