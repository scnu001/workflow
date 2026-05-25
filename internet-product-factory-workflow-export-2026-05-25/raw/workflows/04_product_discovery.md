# Stage 4: Product Discovery

## Purpose
Turn a passed opportunity into a concrete product concept without inventing new demand unrelated to Stages 1-2.

## Required Input Files
- Stage 3 `next-stage-brief.md`
- Stage 2 `classification-table.md`
- Stage 1 demand synthesis if needed

## Required Substages
1. `01_persona_refinement.md` - Persona Refinement
2. `02_use_case_map.md` - Use-Case Map
3. `03_opportunity_solution_tree.md` - Opportunity-Solution Tree
4. `04_core_workflow_design.md` - Core Workflow Design
5. `05_assumption_map.md` - Assumption Map
6. `06_mvp_direction.md` - MVP Direction

## Required Output Files
- all required substage files
- `product-discovery.md`
- `assumption-map.md`
- `opportunity-solution-tree.md`
- `core-capability-design.md`
- `input-automation-map.md`
- `core-mechanism-design.md`
- `ui-specificity-design.md`
- `fixture-plan.md`
- `real-world-depth-design.md`
- `ecosystem-compatibility-plan.md`
- `external-data-integration-plan.md`
- `real-corpus-benchmark-plan.md`
- `business-workflow-map.md`
- `data-sufficiency-map.md`
- `constraint-map.md`
- `source-system-map.md`
- `method-fit-map.md`
- `analytical-core-design.md`
- `uncertainty-and-assumption-map.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Substage Quality Rule
Each completed product-discovery substage must follow `templates/substage-report-template.md`, contain at least 500 meaningful words, and connect back to the approved demand and Q-Gate evidence.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` defines the persona, use case, core workflow, assumptions, MVP direction, rejected ideas, and exact requirements for MVP Specification.

## Artifact-First Product Design Rule
Before designing the UI, define the final user-ready artifact the product should help create.

Examples of strong artifacts:
- regulation-cited letter
- evidence packet
- filing checklist
- calendar/deadline file
- patch or diff
- decision record
- appeal or response draft
- prioritized purchase/order/vendor action plan

A dashboard or Markdown report can be useful, but it is not automatically the product. If the real user needs a letter, packet, patch, calendar, filing, or decision record, Stage 4 must design that artifact explicitly before Stage 6 begins.

## Failure / Blocker Behavior
If the concept drifts from original demand, return to Stage 1 or Stage 2 instead of inventing a new product silently.

## Evidence-First Rule
Product discovery must use previous evidence IDs and must place unsupported design ideas under Weak Hypotheses. Do not invent new demand. Every major concept decision must trace back to evidence or be marked as a hypothesis.

## Core Capability Requirement
Create `core-capability-design.md`. It must define:
- core capability
- why it is non-trivial
- what data it requires
- how data enters the product
- what can be automated
- what is manual only in demo mode
- what would make the product shallow
- minimum acceptable V1 capability
- V2 upgrade path

## Input Automation Requirement
Create `input-automation-map.md`. It must define:
- ideal input path
- acceptable V1 input path
- unacceptable shallow input path
- import options
- automation options
- friction risks

Manual JSON alone is a demo path, not a strong main product path, unless the product is explicitly a developer config tool.

## Implementation Depth Design Requirements
Create `core-mechanism-design.md`. It must define:
- non-trivial mechanism
- why it is deeper than keyword matching
- what data structures are needed
- what algorithms, parsers, or rules are needed
- what edge cases matter
- what would make the product toy-level

Create `ui-specificity-design.md`. It must define:
- product-specific UI views
- domain-specific visualizations
- interaction beyond upload + report
- what frontend elements must not be generic
- why any reused shell is justified

Create `fixture-plan.md`. It must define:
- at least 3 realistic sample inputs
- at least 5 edge cases
- at least 1 malformed input case
- at least 1 complex input case
- at least 1 negative / no-issue case if relevant

## Real-World Depth Design Requirements
Create `real-world-depth-design.md`, `ecosystem-compatibility-plan.md`, `external-data-integration-plan.md`, and `real-corpus-benchmark-plan.md`.

These files must define:
- real-world variants that must be supported
- unsupported variants and honest scope
- external authoritative data needed for security, risk, vulnerability, pricing, market, or package claims
- remediation expectations
- realistic, complex, and large benchmark corpus
- metrics to record: node count, edge count, runtime, findings count, false-positive concerns

## Business Workflow Depth Design Requirements
For non-developer operational products, create:
- `business-workflow-map.md`
- `data-sufficiency-map.md`
- `constraint-map.md`
- `source-system-map.md`

`business-workflow-map.md` must explain:
- current manual workflow
- where data comes from
- what decisions are made
- what bottlenecks exist
- what output would reduce work

`data-sufficiency-map.md` must explain:
- required fields
- optional fields
- missing-field behavior
- confidence downgrade logic

`constraint-map.md` must explain:
- budget/time/cash/supplier/legal/operational constraints
- which constraints V1 handles
- which constraints are roadmap

`source-system-map.md` must explain:
- likely source systems
- export formats
- mapping/preset needs

## Disciplinary Method Fit Requirements
Create `method-fit-map.md`. It must define:
- natural discipline or method family
- methods that fit
- methods that do not fit
- why the chosen method is not artificial
- minimum serious method core
- shallow failure mode
- over-engineering failure mode
- how the method improves user decisions

Create `analytical-core-design.md`. It must define:
- core analytical mechanism
- user inputs
- inferred parameters
- model, scoring, simulation, parser, or rule logic
- output interpretation
- what makes it better than simple threshold scoring

Create `uncertainty-and-assumption-map.md`. It must define:
- uncertain inputs
- assumptions
- confidence logic
- sensitivity checks
- assumption challenge mechanism
- what would flip the decision

Do not add Monte Carlo, multi-agent debate, optimization, AI classification, graph analysis, or other advanced methods unless they naturally fit the problem. No method theater.

## Substantive Completion Rule
Do not mark Stage 4 complete while major discovery artifacts still contain `TBD`, generic claims, or scaffold text. Before handoff, the stage must explain how the evidence shaped the artifact, method architecture, fixture plan, and risk mitigations.
