# Parallel Line Operating Brief

Use this when a second AI agent starts a parallel product line.

## Mission

Run one complete product through the `internet-product-factory` state machine without relying on chat history.

The goal is not to generate many products. The goal is one product with real demand evidence, natural method depth, implementation substance, realistic fixtures, audit discipline, and launch-ready packaging.

## Startup

1. Open `E:/aipro/internet-product-factory`.
2. Read `products/_product-index.md`.
3. Read this export package's `START_HERE.md`.
4. Read `raw/AGENTS.md`.
5. Read `raw/scripts/workflow_schema.py`.
6. Choose the next unused product ID. Do not edit another active product folder.
7. Run `python scripts/create_product_folder.py product-XXX`.

## Operating Rules

- Files are memory.
- Every stage ends with `next-stage-brief.md`.
- Every stage reads the previous `next-stage-brief.md` first.
- Every completed substage needs evidence, source log, analysis, scores, risks, confidence, and decision.
- Do not invent sources.
- Do not build if Q-Gate fails.
- Do not publish without explicit user approval.
- Do not initialize git at the factory root unless explicitly asked.

## Product Selection

Stage 1 must inspect broad demand pools. Do not default to developer tools. Do not force non-developer tools. Let evidence win.

If a developer tool wins, compare it against the strongest non-developer candidate.

If a non-developer tool wins, compare it against the strongest developer candidate.

## Build Discipline

Before build, Stage 4 and Stage 5 must define:

- final user-ready artifact
- core capability
- natural method fit
- real input path
- implementation depth
- fixture plan
- test plan
- README claim boundaries

During build, do not settle for upload -> score -> generic report unless the domain genuinely only needs that and all depth gates pass.

## Final Validation

Run:

```powershell
python scripts/validate_stage_files.py
python scripts/validate_meaningful_substage.py
python scripts/audit_workflow_substance.py --strict product-XXX
```

Also run product tests/smoke tests and secret scan before any launch.

