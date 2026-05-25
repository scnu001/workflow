# Workflow Substance Audit Checklist

Use this before calling a product workflow-complete.

## 1. Scaffold Residue

- Completed product has no required substage files still marked `Status: NOT_STARTED`.
- Completed product has no heavy `TBD` residue in stage artifacts.
- Stage files contain evidence and decisions that shaped the product before build, not post-hoc justification.

## 2. Evidence And Method

- Stage 1 includes real source diversity and cross-audience comparison.
- Stage 2 ranks candidates with conservative robustness checks.
- Stage 3 Q-Gate names the true failure modes and carries binding mitigations forward.
- Stage 4 defines the user-ready artifact before designing UI.
- Stage 4 method architecture is specific enough that build does not guess.

## 3. Core Implementation

- Core logic is split into domain modules unless a monolith is explicitly justified.
- The product has a non-trivial method core, not only intake -> score -> report.
- The UI exposes the domain structure and method, not only upload + output.
- The main output is a user-ready artifact when the domain calls for one.

## 4. Fixtures And Tests

- Fixture matrix includes normal, edge, malformed, complex, no-issue, and source/jurisdiction variants when relevant.
- Tests cover parser, method core, output artifact, negative/no-issue case, and smoke flow.
- Product-specific smoke test proves the real data path and artifact export.

## 5. Decision

Choose one:

- `PASS_SUBSTANTIVE_WORKFLOW`
- `NEEDS_STAGE_REPAIR`
- `NEEDS_CORE_REFACTOR`
- `NEEDS_FIXTURE_MATRIX`
- `NEEDS_V2_BEFORE_LAUNCH`

