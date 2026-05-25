# Realistic Business Fixture Gate

## Purpose

Business test data must reflect realistic messiness, not clean toy rows.

## Minimum For Public Product

- at least 20 realistic rows/items/cases if table-based
- multiple user types or client/vendor/customer groups if relevant
- missing fields
- malformed values
- edge cases
- no-action cases
- high-priority cases
- low-priority cases
- conflicting priorities

## Inventory Fixture Requirements

- 30+ SKUs if possible
- multiple vendors
- slow movers
- fast movers
- high margin / low margin items
- low stock high velocity items
- high stock slow velocity items
- missing lead time
- missing vendor
- on-order quantity
- large MOQ
- perishables if supported
- budget-limited scenario

## Rules

- Toy samples block `TOP_10_PUBLISH`.
- Happy-path-only business samples block `SHIP`.
