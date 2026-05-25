# Stage Machine Reference

Canonical source: `scripts/workflow_schema.py`.

This reference is a human-readable summary. If this file and the schema disagree, use the schema.

## Base Stage Files

Every stage must include:

- `stage-report.md`
- `checkpoint.md`
- `prompt-log.md`
- `decision-log.md`
- `next-stage-brief.md`

The next stage reads `next-stage-brief.md` first.

## Stage 0: `00_context`

Goal: frame the product/opportunity without building.

Substages:

- `01_product_boundary.md`
- `02_user_persona_assumptions.md`
- `03_public_vs_internal_boundary.md`
- `04_technical_constraints.md`
- `05_success_definition.md`

Key artifact: `project-context.md`.

## Stage 1: `01_demand_discovery`

Goal: broad evidence-first demand discovery across multiple demand pools before idea selection.

Substages:

- `01_broad_source_scan.md`
- `02_pain_signal_extraction.md`
- `03_opportunity_clustering.md`
- `04_cross_audience_comparison.md`
- `05_evidence_quality_ranking.md`
- `06_product_opportunity_framing.md`
- `07_demand_synthesis.md`

Required artifacts:

- `demand-discovery-report.md`
- `competitor-matrix.md`
- `user-pain-map.md`
- `raw-signal-log.md`
- `demand-bias-check.md`

Demand synthesis must produce Top 20 opportunities, Top 5 strongest opportunities, top developer vs top non-developer comparison, weak signals to ignore, candidate ideas for Stage 2, and evidence quality notes.

## Stage 2: `02_demand_scoring`

Goal: score launch slots strictly and classify every candidate.

Substages:

- `01_user_pain_scoring.md`
- `02_demo_pull_scoring.md`
- `03_expected_star_pull_scoring.md`
- `04_build_maintenance_cost_scoring.md`
- `05_differentiation_copy_risk_scoring.md`
- `06_monetization_distribution_scoring.md`
- `07_final_launch_slot_ranking.md`

Required artifacts:

- `demand-scorecard.md`
- `opportunity-ranking.md`
- `batch-shortlist.md`
- `launch-slot-ranking.md`
- `classification-table.md`

Stage 2 must include product-depth, implementation-depth, real-world-depth, business-depth, demand-bias, and method-fit scoring when applicable.

## Stage 3: `03_q_gate`

Goal: prevent weak or shallow ideas from reaching build.

Substages:

- `01_public_product_bar_check.md`
- `02_github_visitor_test.md`
- `03_30_minute_copy_test.md`
- `04_risk_compliance_check.md`
- `05_kill_continue_decision.md`

Required artifacts:

- `q-gate-report.md`
- `pre-mortem.md`

Allowed decisions: `CONTINUE`, `PIVOT`, `PAUSE`, `KILL`, `BUILD_INTERNAL_ONLY`, `NEEDS_V2_BEFORE_LAUNCH`.

## Stage 4: `04_product_discovery`

Goal: turn a passed opportunity into a concrete product concept without inventing new demand.

Substages:

- `01_persona_refinement.md`
- `02_use_case_map.md`
- `03_opportunity_solution_tree.md`
- `04_core_workflow_design.md`
- `05_assumption_map.md`
- `06_mvp_direction.md`

Required artifacts include:

- `product-discovery.md`
- `assumption-map.md`
- `opportunity-solution-tree.md`
- `method-fit-map.md`
- `analytical-core-design.md`
- `uncertainty-and-assumption-map.md`
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

Not every artifact is equally relevant to every product, but completed public products must address applicable gates explicitly.

## Stage 5: `05_mvp_specification`

Goal: make implementation unambiguous.

Substages:

- `01_prd.md`
- `02_user_stories.md`
- `03_ux_page_or_cli_structure.md`
- `04_data_model.md`
- `05_api_and_nim_integration_plan.md`
- `06_acceptance_criteria.md`
- `07_test_plan.md`

Required artifacts:

- `mvp-prd.md`
- `technical-spec.md`
- `acceptance-criteria.md`

Stage 5 must include core capability, real data path, input automation, configuration freshness, uncertainty, fixture depth, method core, anti-shallow rules, and tests.

## Stage 6: `06_build_execution`

Goal: build one high-value product and record implementation evidence.

Substages:

- `01_scaffold_log.md`
- `02_core_logic_log.md`
- `03_ui_or_cli_surface_log.md`
- `04_example_data_log.md`
- `05_nim_or_mock_integration_log.md`
- `06_smoke_test_log.md`
- `07_readme_draft_log.md`

Required artifacts include:

- `build-log.md`
- `run-instructions.md`
- `build-depth-checklist.md`
- `core-logic-depth-report.md`
- `fixture-test-report.md`
- `real-corpus-benchmark-report.md`
- `ci-automation-readiness-report.md`
- `remediation-depth-report.md`
- `data-quality-report.md`
- `missing-field-report.md`
- `business-fixture-report.md`
- `what-if-simulation-report.md`
- `business-constraint-report.md`
- `method-implementation-report.md`

Build logs must distinguish real user features, demo-only features, mock features, and incomplete V2 features.

## Stage 7: `07_multi_agent_audit`

Goal: run independent reviewer perspectives before packaging/ship.

Substages:

- `01_product_reviewer.md`
- `02_engineering_reviewer.md`
- `03_security_reviewer.md`
- `04_growth_reviewer.md`
- `05_skeptical_student_user.md`
- `06_middle_aged_nontechnical_user.md`
- `07_time_poor_professional.md`
- `08_github_visitor.md`
- `09_implementation_depth_reviewer.md`
- `10_real_world_depth_reviewer.md`
- `11_github_readme_reviewer.md`
- `12_business_workflow_reviewer.md`
- `13_method_problem_fit_reviewer.md`

Required artifacts:

- `audit-report.md`
- `subagent-feedback.md`
- `fix-plan.md`
- `ship-or-not.md`

If a relevant specialist reviewer returns `NEEDS_V2_BEFORE_LAUNCH`, `ship-or-not.md` cannot be `SHIP`.

## Stage 8: `08_packaging_launch`

Goal: create a bilingual, honest, star-worthy GitHub launch package.

Substages:

- `01_positioning_star_pull_angle.md`
- `02_readme_first_screen.md`
- `03_problem_differentiation_copy.md`
- `04_demo_screenshot_gif_plan.md`
- `05_quick_start_example_output.md`
- `06_github_description_topics.md`
- `07_english_readme.md`
- `08_chinese_readme.md`
- `09_readme_claim_check.md`
- `10_launch_summary.md`

Required artifacts include:

- `README.md`
- `README.zh-CN.md`
- `launch-summary.md`
- `readme-final.md`
- `readme-final-zh-CN.md`
- `github-description.md`
- `github-description-zh-CN.md`
- `github-topics.md`
- `launch-posts.md`
- `launch-posts-zh-CN.md`
- `seo-keywords.md`
- `poster-brief.md`
- `poster-image-brief.md`
- `distribution-plan.md`
- `demo-instructions.md`
- `bilingual-github-release-plan.md`
- `readme-claim-check.md`

## Stage 9: `09_post_launch_feedback`

Goal: record launch metrics or local-only status.

Substages:

- `01_metrics_collection.md`
- `02_issue_feedback_review.md`
- `03_distribution_feedback_review.md`
- `04_user_comment_synthesis.md`
- `05_continue_pivot_kill_decision.md`

Artifacts:

- `feedback-summary.md`
- `metrics-summary.md`
- `continue-pivot-kill.md`

If no launch happened, record `NOT_LAUNCHED_LOCAL_ONLY` and explain why.

## Stage 10: `10_reflection_memory`

Goal: make the next run smarter.

Substages:

- `01_what_worked.md`
- `02_what_failed.md`
- `03_overbuilt_underbuilt.md`
- `04_signal_quality_review.md`
- `05_scoring_calibration_update.md`
- `06_pattern_memory_update.md`

Artifacts:

- `reflection.md`
- `memory-update.md`

Update `memory/global-lessons.md`, `memory/product-patterns.md`, `memory/scoring-calibration.md`, and optional success/audit memory files.

