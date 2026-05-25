# Build Depth Checklist

## Critical Checks
- Core capability implemented?
- Real data path implemented?
- Custom config implemented?
- Sample data included?
- Input validation implemented?
- Uncertainty handled?
- Robustness/sensitivity implemented?
- Smoke test covers real-data path?
- README does not overclaim?
- Core logic is not toy-level?
- Frontend is not only relabeled shell?
- Multiple fixtures exist?
- Edge cases are tested?
- Output includes specific actionable findings?

## Feature Type Classification
- Demo-only features
- Real user features
- Mock features
- Incomplete V2 features

## Decision Rule
If any critical item is missing, do not mark build as launch-ready. If the idea is good but implementation is too shallow, use `NEEDS_V2_BEFORE_LAUNCH`.

## Implementation Depth Checklist
- Core Logic Depth:
- Parser / Data Understanding Depth:
- Edge Case Coverage:
- Output Actionability:
- Test Depth:
- UI Specificity:
- Integration / Automation Depth:
- Non-Trivial Mechanism Depth:

If the implementation is mostly keyword matching, regex matching, or shallow if-statements, record the additional mechanism that makes it launchable.
