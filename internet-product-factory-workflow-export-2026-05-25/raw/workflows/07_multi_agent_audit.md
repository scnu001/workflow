# Stage 7: Multi-Agent Audit

## Purpose
Audit the product through separate reviewer files before launch.

## Required Input Files
- Stage 6 `next-stage-brief.md`
- `build-log.md`
- `run-instructions.md`
- product implementation files
- `templates/audit-report-template.md`

## Required Substages
1. `01_product_reviewer.md` - Product Reviewer
2. `02_engineering_reviewer.md` - Engineering Reviewer
3. `03_security_reviewer.md` - Security Reviewer
4. `04_growth_reviewer.md` - Growth Reviewer
5. `05_skeptical_student_user.md` - Skeptical Student User
6. `06_middle_aged_nontechnical_user.md` - Middle-Aged Nontechnical User
7. `07_time_poor_professional.md` - Time-Poor Professional
8. `08_github_visitor.md` - GitHub Visitor
9. `09_implementation_depth_reviewer.md` - Implementation Depth Reviewer
10. `10_real_world_depth_reviewer.md` - Real-World Depth Reviewer
11. `11_github_readme_reviewer.md` - GitHub README Reviewer
12. `12_business_workflow_reviewer.md` - Business Workflow Reviewer
13. `13_method_problem_fit_reviewer.md` - Method-Problem Fit Reviewer

## Required Output Files
- all required reviewer files
- `audit-report.md`
- `subagent-feedback.md`
- `fix-plan.md`
- `ship-or-not.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Required Reviewer Scores
- Usefulness
- Clarity
- Trust
- Ease of use
- Differentiation
- Build quality
- Launch readiness
- Demo pull
- Expected star pull
- 30-minute copy risk

## Substage Quality Rule
Each completed reviewer file must follow `templates/substage-report-template.md`, contain at least 500 meaningful words, and include concrete scores, evidence, risks, and decision.

## Handoff Rule
The stage is incomplete until `audit-report.md` synthesizes all reviewer files and `next-stage-brief.md` states whether Packaging may proceed.

## Failure / Blocker Behavior
If the GitHub Visitor would not understand or star the repo from the README first screen, do not ship.

## Evidence-First Rule
Audit substages must cite product files, terminal outputs, prior evidence IDs, or manual inspection evidence. Reviewer opinions without evidence are weak hypotheses. Low-confidence audit results cannot justify shipping.

## Product Depth Audit Questions
Every reviewer must answer:
- Is this just a calculator with a UI?
- Is the main input burden too high?
- Is the product doing work for the user, or asking the user to do the work?
- Is the core capability real or only implied by README?
- Would the target user trust the output?
- What is missing before public launch?

GitHub Visitor must also answer whether the README overstates the product, whether the demo is impressive after seeing the actual workflow, whether they would star it if it only accepts hand-written JSON, and whether this is a V1 product or a prototype.

If at least 3 reviewers identify frontend calculator risk, `ship-or-not.md` must return `NEEDS_V2_BEFORE_LAUNCH`.

## Implementation Depth Reviewer
The Implementation Depth Reviewer must inspect:
- core logic depth
- modular method architecture, including whether the core is collapsed into a single large analyzer file
- whether analyzer is mostly regex or keyword matching
- whether frontend is mostly copied shell
- whether tests are shallow
- whether output is actionable
- whether the output is a user-ready artifact or only a dashboard/report
- whether product deserves public launch

If the Implementation Depth Reviewer says `NEEDS_V2_BEFORE_LAUNCH`, `ship-or-not.md` cannot be `SHIP`.

## Workflow Substance Reviewer
Stage 7 must also check whether the workflow was substantively completed, not merely structurally completed.

Required checks:
- Do any required substages still say `Status: NOT_STARTED`?
- Do stage artifacts still contain heavy `TBD` scaffold residue?
- Did Stage 1-5 decisions clearly shape the build?
- Does the product resemble the last 3 products too closely in shape?
- Is it just another intake -> score -> dashboard/report product?
- Does the product produce a user-ready artifact when the domain calls for one?
- Does `python scripts/audit_workflow_substance.py --strict product-XXX` pass?

If the workflow substance audit fails, `ship-or-not.md` must return `NEEDS_STAGE_REPAIR`, `NEEDS_CORE_REFACTOR`, `NEEDS_FIXTURE_MATRIX`, or `NEEDS_V2_BEFORE_LAUNCH` instead of `SHIP`.

## Real-World Depth Reviewer
The Real-World Depth Reviewer must inspect:
- ecosystem compatibility
- external authoritative data usage or honest structural scope
- remediation depth
- real corpus benchmark
- CLI/export/CI automation readiness
- UI domain specificity
- README claim honesty

If the reviewer says toy-only, no remediation, no automation path, or overclaimed security/risk analysis, `ship-or-not.md` cannot be `TOP_10_PUBLISH`.

## GitHub README Reviewer
The GitHub README Reviewer must inspect the final GitHub launch page, not just the product implementation.

It must answer:
- Would I understand the project in 10 seconds?
- Would I keep reading?
- Would I star it?
- Is the first screen strong?
- Is the README too technical too early?
- Are limitations scattered too much?
- Are the product claims honest?
- Are screenshots/GIFs missing?
- Is the Chinese README natural?
- Is the English README professional?

Required evidence:
- `README.md`
- `README.zh-CN.md`
- `github-description.md`
- `github-topics.md`
- `demo-instructions.md`
- `readme-claim-check.md`
- screenshot/GIF or demo-output plan

If the GitHub README Reviewer fails the README, `ship-or-not.md` cannot be `SHIP`.

## Business Workflow Reviewer
For non-developer operational products, the Business Workflow Reviewer must ask:
- Is this just a spreadsheet with a web UI?
- Does it reflect real business operations?
- Are constraints modeled?
- Is the input realistic?
- Are outputs actionable?
- Would a small business actually use this?
- What would make this more useful than Excel?

Required evidence:
- `business-workflow-map.md`
- `data-sufficiency-map.md`
- `constraint-map.md`
- `source-system-map.md`
- `data-quality-report.md`
- `missing-field-report.md`
- `business-fixture-report.md`
- `what-if-simulation-report.md`
- README and sample outputs

If the Business Workflow Reviewer fails the product, `ship-or-not.md` cannot be `SHIP`.

## Method-Problem Fit Reviewer
The Method-Problem Fit Reviewer must inspect:
- whether the analytical method naturally fits the problem
- whether the method is deep enough for the product claim
- whether the product contains fake complexity or method theater
- whether it is just simple scoring with fancy wording
- whether assumptions are challenged
- whether uncertainty is handled
- whether a domain-aware user would respect the analysis

Required evidence:
- `method-fit-map.md`
- `analytical-core-design.md`
- `uncertainty-and-assumption-map.md`
- `method-implementation-report.md`
- implementation files
- tests and fixtures
- README claim check

If the Method-Problem Fit Reviewer fails, `ship-or-not.md` cannot be `SHIP`.
