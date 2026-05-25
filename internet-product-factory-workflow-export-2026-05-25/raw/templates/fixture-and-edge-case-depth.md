# Fixture And Edge Case Depth

One toy sample file is not enough. A happy-path smoke test alone is not enough.

## Minimum For PUBLIC_PRODUCT

- at least 3 realistic sample inputs
- at least 5 edge cases
- at least 1 malformed input case
- at least 1 complex input case
- at least 1 negative / no-issue case if relevant

## Tests Must Cover

- normal case
- edge case
- malformed case
- empty input or missing field
- complex case
- no-issue case if relevant

## Fixture Table

| Fixture | Type | Realism | Expected Behavior | Test Command | Result |
| --- | --- | --- | --- | --- | --- |
| TBD | normal | TBD | TBD | TBD | TBD |
| TBD | edge | TBD | TBD | TBD | TBD |
| TBD | malformed | TBD | TBD | TBD | TBD |
| TBD | complex | TBD | TBD | TBD | TBD |
| TBD | no-issue | TBD | TBD | TBD | TBD |

## Rules

- If tests only prove the app starts, product cannot be TOP_10_PUBLISH.
- If the product has fewer than 3 realistic samples, downgrade launch readiness.
- If edge cases are undocumented, use NEEDS_V2_BEFORE_LAUNCH.
