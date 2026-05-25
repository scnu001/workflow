# Stage 10: Reflection / Memory Update

## Purpose
Update memory so the next run becomes smarter.

## Required Input Files
- Stage 9 `next-stage-brief.md`
- all prior stage briefs as needed
- `memory/*.md`

## Required Substages
1. `01_what_worked.md` - What Worked
2. `02_what_failed.md` - What Failed
3. `03_overbuilt_underbuilt.md` - Overbuilt / Underbuilt Review
4. `04_signal_quality_review.md` - Signal Quality Review
5. `05_scoring_calibration_update.md` - Scoring Calibration Update
6. `06_pattern_memory_update.md` - Pattern Memory Update

## Required Output Files
- all required substage files
- `reflection.md`
- `memory-update.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Memory Files To Update
- `memory/global-lessons.md`
- `memory/product-patterns.md`
- `memory/failed-ideas.md`
- `memory/successful-patterns.md` if it exists
- `memory/audit-feedback-memory.md` if it exists
- `memory/scoring-calibration.md`

## Substage Quality Rule
Each completed reflection substage must follow `templates/substage-report-template.md`, contain at least 500 meaningful words, and cite specific files, decisions, signals, scores, and outcomes.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` records final memory updates, scoring changes, pattern changes, and instructions for the next product run.

## Failure / Blocker Behavior
If memory cannot be updated, mark the checkpoint blocked. Do not claim the product run has ended.

## Evidence-First Rule
Reflection must cite substage files, evidence IDs, decisions, scores, terminal outputs, or launch metrics. Do not convert vibes into lessons. If a lesson only appears after generic analysis but fails under evidence, downgrade it.

## Implementation Depth Reflection Rule
Reflection must explicitly record whether the product suffered from any of these failure modes:
- reused frontend shell without product-specific UI
- shallow rule scanner backend
- keyword/regex-only logic
- one toy sample
- happy-path-only smoke test
- generic Markdown output
- no non-trivial mechanism
- no edge-case coverage
- no output actionability

If any of these appear, update `memory/scoring-calibration.md` and classify the product as `NEEDS_V2_BEFORE_LAUNCH`, `BUILD_INTERNAL`, or a partial success rather than a full public-product success.
