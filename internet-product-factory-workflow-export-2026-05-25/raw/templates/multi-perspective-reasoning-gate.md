# Multi-Perspective Reasoning Gate

## Applies To

Use this gate for products involving judgment, planning, prioritization, strategy, risk, life decisions, business decisions, or tradeoffs.

Not every product needs eight agents. But complex judgment products need more than one-pass scoring.

## Acceptable Multi-Perspective Mechanisms

At least one of the following must be present when recommendations depend on judgment or tradeoffs:

- multiple analytical perspectives
- user-adjustable weights
- scenario analysis
- devil's advocate critique
- sensitivity analysis
- confidence scoring
- assumption review
- final synthesis layer

## Required Questions

1. What perspectives could disagree about the recommendation?
2. Which assumptions drive the top recommendation?
3. What would flip the recommendation?
4. Does the user get to adjust weights, scenarios, thresholds, or priorities?
5. Does the product distinguish evidence-backed findings from weak hypotheses?
6. Does the final synthesis explain confidence and uncertainty?

## Hard Rules

- If the product makes recommendations, it must explain what assumptions would flip the recommendation.
- If the recommendation only survives under optimistic assumptions, downgrade confidence.
- If the product claims decision support but provides only one-pass scoring, classify it as `NEEDS_V2_BEFORE_LAUNCH` unless the decision is genuinely simple.

