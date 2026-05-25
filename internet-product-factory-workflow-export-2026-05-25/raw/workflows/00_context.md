# Stage 0: Context Setup

## Purpose
Frame what kind of product or opportunity is being evaluated. Do not build anything in this stage.

## Required Input Files
- `products/_product-index.md`
- relevant `memory/*.md`
- user-provided constraints

## Required Substages
1. `01_product_boundary.md` - Product Boundary
2. `02_user_persona_assumptions.md` - User Persona Assumptions
3. `03_public_vs_internal_boundary.md` - Public vs Internal Boundary
4. `04_technical_constraints.md` - Technical Constraints
5. `05_success_definition.md` - Success Definition

## Required Output Files
- all required substage files
- `project-context.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Substage Quality Rule
Each completed substage must follow `templates/substage-report-template.md` and contain at least 500 meaningful words. Generic filler does not count. If evidence is unavailable, record the blocker instead of inventing context.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` summarizes the boundary, assumptions, constraints, success definition, open questions, and exact required inputs for Stage 1.

## Failure / Blocker Behavior
If the product boundary, user persona, or public-vs-internal boundary is unclear, mark the checkpoint as blocked and do not advance to demand discovery.

## Evidence-First Rule
Substage conclusions must follow Evidence Pack -> Source Log -> Analysis -> Decision. If evidence is unavailable, write `Evidence unavailable. This is a hypothesis, not a finding.` Stage synthesis must cite substage files or evidence IDs and must not introduce unsupported claims.
