# Frontend Calculator Trap Check

## Exact Rule
A product with a frontend can still be shallow.

A product is shallow if it mainly:
- asks the user to manually enter all important values
- runs a deterministic formula
- outputs a formatted report
- has no real import path
- has no automation
- has no adaptive logic
- has no non-trivial data processing
- has no robust validation
- has no real-world integration path

## Decision Rule
If this is true, classify as `EXPERIMENT`, `INTERNAL_FACTORY_TOOL`, or `NEEDS_V2_BEFORE_LAUNCH`. Do not classify it as `TOP_10_PUBLISH`.

