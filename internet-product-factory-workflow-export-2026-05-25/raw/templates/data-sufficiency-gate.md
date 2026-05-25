# Data Sufficiency Gate

## Purpose

Every non-developer operational product must prove that the user naturally has the data required for the analysis, and that missing or incomplete data does not produce overconfident output.

## Required Questions

1. What data does the product require?
2. Does the user naturally have this data?
3. Is the data usually complete?
4. Which fields are required?
5. Which fields are optional?
6. Which fields can be estimated?
7. Which missing fields break the analysis?
8. How does missing data change confidence?
9. Does the product tell the user which fields are missing?
10. Does the product avoid overconfident output when data is incomplete?

## Scores

- Data Availability: 1-10
- Field Completeness: 1-10
- Data Quality Handling: 1-10
- Missing Field Robustness: 1-10

## Rules

- If required data is not naturally available, downgrade launch readiness.
- If missing fields silently produce confident output, block `TOP_10_PUBLISH`.
- If output quality depends on hidden assumptions, disclose those assumptions.

## Inventory-Specific Fields

- SKU
- product name
- current stock
- sales velocity
- historical sales window
- lead time
- MOQ
- vendor
- unit cost
- price
- on-order quantity
- stockout history if available
