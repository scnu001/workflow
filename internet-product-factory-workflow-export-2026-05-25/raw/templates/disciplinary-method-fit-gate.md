# Disciplinary Method Fit Gate

## Principle

A product should have a natural analytical method core.

Do not add advanced methods randomly. Monte Carlo is natural for decisions, risk, uncertainty, forecasts, and scenario analysis. It is usually not natural for simple invoice chasing, deadline calculation, or deterministic record triage unless uncertainty modeling truly changes the user's decision.

No method theater. No fake complexity. No shallow scoring disguised as analysis.

## Required Questions

Every product must answer:

1. What discipline or analytical tradition does this problem belong to?
2. What methods naturally fit this problem?
3. Which methods are unnecessary or artificial?
4. What is the minimum serious method core for this product?
5. What would make this product shallow?
6. What would make this product over-engineered?
7. How does the chosen method improve user decisions?
8. How will uncertainty be handled?
9. How will assumptions be challenged?
10. How will the product avoid giving overconfident conclusions?

## Method Fit Examples

Decision products may naturally use multi-criteria decision analysis, utility functions, scenario analysis, Monte Carlo simulation, sensitivity analysis, devil's advocate review, or multi-perspective debate.

Inventory products may naturally use reorder point, safety stock, lead-time demand, EOQ when relevant, budget-constrained purchasing, and sensitivity to demand or supplier delay.

Subscription audit products may naturally use recurring pattern detection, merchant normalization, cadence inference, confidence scoring, and user confirmation loops.

Dependency products may naturally use graph traversal, centrality or fan-in, blast radius, dependency path explanation, and vulnerability/advisory integration if claiming security.

Return deadline products may naturally use policy rule matching, deadline basis detection, confidence scoring, evidence checklists, and reminder/calendar workflow.

## Decision Rule

If the chosen method does not naturally fit the product problem, downgrade Method Fit.

If no serious method core exists, classify the candidate as `EXPERIMENT`, `BUILD_INTERNAL`, `PARK`, or `NEEDS_V2_BEFORE_LAUNCH`.

