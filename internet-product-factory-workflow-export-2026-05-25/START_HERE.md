# Internet Product Factory Export - Start Here

Generated: 2026-05-25

This folder is a portable handoff package for the `internet-product-factory` workflow.

It is designed for another AI agent to run a second product line without relying on the original chat history.

## What This Package Contains

- `factory-workflow-handoff-2026-05-25.md`: complete operating handoff.
- `parallel-line-operating-brief-2026-05-25.md`: short startup instructions for another agent.
- `EXPORT_MANIFEST.md`: file list and usage notes.
- `skill/internet-product-factory-workflow/`: installable Codex Skill version.
- `raw/`: exact source files copied from the current repository.

## Fast Start For Another AI

1. Work inside `E:/aipro/internet-product-factory`.
2. Read `raw/AGENTS.md`.
3. Read `factory-workflow-handoff-2026-05-25.md`.
4. Read `raw/scripts/workflow_schema.py`.
5. Read `raw/memory/global-lessons.md`, `raw/memory/scoring-calibration.md`, and `raw/memory/product-patterns.md`.
6. Open `products/_product-index.md` in the live repo and reserve the next unused product ID.
7. Run the workflow stage-by-stage. Use Markdown files as memory.

## Critical Principle

The workflow is not a checklist. It is a forcing function for product depth:

```text
Evidence -> Method fit -> Architecture -> Fixtures -> Tests -> Audit -> Packaging -> Memory
```

If an agent only creates files and passes validators, the product can still be shallow. The workflow is complete only when the reasoning and implementation substance are complete.

