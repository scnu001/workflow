from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Substage:
    file: str
    name: str
    objective: str
    kind: str = "context"
    source_quota: str = "No fixed source quota. Still record evidence, sources, analysis, confidence, and decision."
    requires_data_analysis: bool = False
    min_confidence_for_public: str = "MEDIUM"
    min_evidence_rows: int = 0
    min_source_types: int = 0


@dataclass(frozen=True)
class Stage:
    folder: str
    name: str
    substages: tuple[Substage, ...]
    artifacts: tuple[str, ...]


BASE_STAGE_FILES = (
    "stage-report.md",
    "checkpoint.md",
    "prompt-log.md",
    "decision-log.md",
    "next-stage-brief.md",
)

REQUIRED_SUBSTAGE_HEADINGS = (
    "# Substage:",
    "## 1. Objective",
    "## 2. Why This Matters",
    "## 3. Method",
    "## 4. Evidence Pack",
    "## 5. Source Log",
    "## 6. Analysis",
    "## 7. Scores",
    "## 8. Risks / Weak Points",
    "## 9. Output to Next Substage",
    "## 10. Confidence Rating",
    "## 11. Decision",
    "## 12. Minimum Quality Check",
)

EVIDENCE_TABLE_HEADER = "| ID | Source Type | Source / URL / File Path | Query or Input | Raw Observation | Extracted Signal | Reliability 1-10 | Relevance 1-10 | Used In Conclusion? |"

ANALYSIS_HEADINGS = (
    "### Evidence-Backed Findings",
    "### Reasonable Inferences",
    "### Weak Hypotheses",
    "### Unknowns",
    "### Implications for Product Decision",
)

DATA_ANALYSIS_HEADINGS = (
    "### Baseline Analysis",
    "### Robustness Check",
    "### Sensitivity Check",
    "### Error / Outlier Check",
    "### Interpretation",
    "### Decision Impact",
)

CONFIDENCE_LEVELS = ("HIGH", "MEDIUM", "LOW", "SPECULATIVE")

Q_GATE_DECISIONS = (
    "CONTINUE",
    "PIVOT",
    "PAUSE",
    "KILL",
    "BUILD_INTERNAL_ONLY",
    "NEEDS_V2_BEFORE_LAUNCH",
    "UNDECIDED",
)

PRODUCT_DEPTH_SCORE_TERMS = (
    "Core Capability Completeness",
    "Input Automation Depth",
    "User Friction",
    "Real Data Path Strength",
    "Configuration Freshness",
    "Estimation Accuracy",
    "Integration Potential",
    "Frontend Calculator Risk",
)

PRODUCT_DEPTH_GATE_TERMS = (
    "Core Capability Gate",
    "Input Automation Gate",
    "User Friction Gate",
    "Configuration Freshness Gate",
    "Real Data Path Gate",
    "Accuracy / Estimation Quality Gate",
    "Frontend Calculator Trap Rule",
)

IMPLEMENTATION_DEPTH_SCORE_TERMS = (
    "Core Logic Depth",
    "UI Specificity",
    "Parser/Data Depth",
    "Edge Case Coverage",
    "Test Depth",
    "Output Actionability",
    "Non-Trivial Mechanism Depth",
    "Scaffold Reuse Risk",
    "Toy Implementation Risk",
)

IMPLEMENTATION_DEPTH_GATE_TERMS = (
    "Implementation Depth Gate",
    "UI Specificity Gate",
    "Core Mechanism Requirement",
    "Fixture and Edge Case Depth",
    "Output Actionability Gate",
)

REAL_WORLD_DEPTH_SCORE_TERMS = (
    "Ecosystem Compatibility",
    "External Data Integration",
    "Remediation Depth",
    "Real Corpus Benchmark",
    "CI / Automation Readiness",
    "UI Domain Specificity",
    "README Claim Honesty",
)

REAL_WORLD_DEPTH_GATE_TERMS = (
    "Real-World Depth Gate",
    "Ecosystem Compatibility Gate",
    "External Data Integration Gate",
    "Remediation Depth Gate",
    "Real Corpus Benchmark Gate",
    "CI / Automation Readiness Gate",
    "README Claim Honesty Gate",
)

GITHUB_LAUNCH_PAGE_GATE_TERMS = (
    "GitHub Launch Page Gate",
    "Bilingual README Requirement",
    "README Structure Requirement",
    "README First-Screen Gate",
    "Star-Pull Copy Rule",
    "GitHub Metadata Requirement",
    "README Claim Check",
)

GITHUB_README_REQUIRED_SECTIONS = (
    "Hero Section",
    "Problem",
    "Why Existing Approaches Are Not Enough",
    "What This Project Does",
    "Key Features",
    "Demo / Screenshots",
    "Quick Start",
    "Example Input / Output",
    "Use Cases",
    "How It Works",
    "Project Structure",
    "Roadmap",
    "Limitations",
    "License",
)

DEMAND_BIAS_SCORE_TERMS = (
    "Evidence Breadth Score",
    "Cross-Audience Strength Score",
    "Source Diversity Score",
    "Demand Specificity Score",
    "Buildability Bias Risk",
    "GitHub Bias Risk",
    "Category Overconcentration Risk",
)

DEMAND_BIAS_GATE_TERMS = (
    "Broad Demand Discovery",
    "Demand Bias Check",
    "Developer Tool Bias Check",
    "Cross-Audience Comparison",
    "Category-Neutral Product Selection",
)

BUSINESS_WORKFLOW_SCORE_TERMS = (
    "Data Sufficiency Score",
    "Business Constraint Depth",
    "Operational Actionability",
    "Source-System Fit",
    "What-if Depth",
    "Realistic Fixture Depth",
    "Business Workflow Depth",
    "Spreadsheet Trap Risk",
)

BUSINESS_WORKFLOW_GATE_TERMS = (
    "Business Workflow Depth Gate",
    "Data Sufficiency Gate",
    "Business Constraint Gate",
    "Source-System Preset Gate",
    "Operational Actionability Gate",
    "What-if / Constraint Simulation Gate",
    "Realistic Business Fixture Gate",
)

METHOD_FIT_SCORE_TERMS = (
    "Disciplinary Method Fit",
    "Method Depth",
    "Analytical Originality",
    "Uncertainty Handling",
    "Assumption Challenge",
    "Multi-Perspective Reasoning",
    "Method Theater Risk",
    "Shallow Scoring Risk",
)

METHOD_FIT_GATE_TERMS = (
    "Disciplinary Method Fit Gate",
    "Method Depth Gate",
    "Multi-Perspective Reasoning Gate",
    "Method Theater Risk",
    "Shallow Scoring Risk",
)

NEXT_STAGE_BRIEF_HEADINGS = (
    "# Next Stage Brief",
    "## 1. Stage Completed",
    "## 2. Source Files Read",
    "## 3. Most Important Findings",
    "## 4. Candidate Ideas / Decisions",
    "## 5. Scores / Rankings",
    "## 6. Rejected or Downgraded Items",
    "## 7. Risks and Blockers",
    "## 8. Required Inputs for Next Stage",
    "## 9. Open Questions",
    "## 10. Handoff Decision",
)

STAGES = (
    Stage(
        folder="00_context",
        name="Context Setup",
        substages=(
            Substage("01_product_boundary.md", "Product Boundary", "Frame what kind of product or opportunity is being evaluated."),
            Substage("02_user_persona_assumptions.md", "User Persona Assumptions", "Define the initial target users and the assumptions behind them."),
            Substage("03_public_vs_internal_boundary.md", "Public vs Internal Boundary", "Separate possible public-product value from internal factory usefulness."),
            Substage("04_technical_constraints.md", "Technical Constraints", "Record technical, API, NIM, security, time, and deployment constraints."),
            Substage("05_success_definition.md", "Success Definition", "Define what evidence would make this product worth continuing."),
        ),
        artifacts=("project-context.md",),
    ),
    Stage(
        folder="01_demand_discovery",
        name="Demand Discovery",
        substages=(
            Substage("01_broad_source_scan.md", "Broad Source Scan", "Scan multiple demand pools before any product ideas are selected.", "research", "Inspect multiple demand pools: developer/AI builder, students/applicants, job seekers, creators/solo operators, small business/freelancers, personal finance/decision-making, life/family/healthcare admin, productivity/AI tool users, education/tutoring/learning, and emerging niches. For each pool, collect up to 5 pain signals, 3 source references, 3 candidate opportunities, evidence quality, feasibility, distribution path, and likely product format when available.", min_evidence_rows=20, min_source_types=3),
            Substage("02_pain_signal_extraction.md", "Pain Signal Extraction", "Extract raw pains from sources without generating product ideas yet.", "research", "Record raw pain signals by demand pool. Do not turn pains into products until clustering. If fewer than 5 signals are available for a pool, record the evidence gap instead of inventing demand.", min_evidence_rows=20, min_source_types=3),
            Substage("03_opportunity_clustering.md", "Opportunity Clustering", "Cluster pain signals by problem, not by preselected audience label.", "data_analysis", "Use Stage 1 evidence IDs. Allow cross-audience clusters and record which signals support each cluster.", True),
            Substage("04_cross_audience_comparison.md", "Cross-Audience Comparison", "Compare developer and non-developer opportunities before selection.", "data_analysis", "Compare top developer, student, career, creator, small-business, finance, life-admin, productivity, and education clusters when evidence exists. If one category dominates, explain evidence reasons and source-mix risks.", True),
            Substage("05_evidence_quality_ranking.md", "Evidence Quality Ranking", "Rank clusters by source strength, repetition, urgency, specificity, and willingness to act.", "data_analysis", "Use baseline ranking, robustness check excluding overrepresented source types, sensitivity checks, and conservative downgrade rules.", True),
            Substage("06_product_opportunity_framing.md", "Product Opportunity Framing", "Convert only strongest pain clusters into product opportunities.", "data_analysis", "Frame opportunities only after evidence ranking. Include why each opportunity is not merely the easiest thing for Codex to build.", True),
            Substage("07_demand_synthesis.md", "Demand Synthesis", "Produce final evidence-based opportunity shortlist without category preference.", "data_analysis", "Use all Stage 1 evidence. Produce Top 20 demand opportunities, Top 5 strongest opportunities, top developer vs top non-developer comparison, weak signals to ignore, and evidence quality notes.", True),
        ),
        artifacts=("demand-discovery-report.md", "competitor-matrix.md", "user-pain-map.md", "raw-signal-log.md", "demand-bias-check.md"),
    ),
    Stage(
        folder="02_demand_scoring",
        name="Launch Slot Scoring",
        substages=(
            Substage("01_user_pain_scoring.md", "User Pain Scoring", "Score pain intensity, urgency, and specificity.", "data_analysis", "Use demand evidence IDs from Stage 1.", True),
            Substage("02_demo_pull_scoring.md", "Demo Pull Scoring", "Score whether the product can create a visible demo moment.", "data_analysis", "Use demo evidence and product-surface evidence IDs.", True),
            Substage("03_expected_star_pull_scoring.md", "Expected Star Pull Scoring", "Score whether a GitHub visitor would understand and star the repo.", "data_analysis", "Use GitHub/repo/distribution evidence IDs.", True),
            Substage("04_build_maintenance_cost_scoring.md", "Build / Maintenance Cost Scoring", "Score implementation cost, maintenance cost, and operational burden.", "data_analysis", "Use implementation complexity evidence and comparable-product evidence IDs.", True),
            Substage("05_differentiation_copy_risk_scoring.md", "Differentiation / 30-Minute Copy Risk Scoring", "Score differentiation, depth penalty, and copy risk.", "data_analysis", "Use competitor and comparable-product evidence IDs.", True),
            Substage("06_monetization_distribution_scoring.md", "Monetization / Distribution Scoring", "Score distribution specificity, buyer value, and revenue path.", "data_analysis", "Use pricing, monetization, and channel evidence IDs.", True),
            Substage("07_final_launch_slot_ranking.md", "Final Launch Slot Ranking", "Classify every candidate and select the strongest public-product candidate.", "data_analysis", "Use all Stage 2 scoring evidence.", True),
        ),
        artifacts=("demand-scorecard.md", "opportunity-ranking.md", "batch-shortlist.md", "launch-slot-ranking.md", "classification-table.md"),
    ),
    Stage(
        folder="03_q_gate",
        name="Q-Gate / Kill-or-Continue",
        substages=(
            Substage("01_public_product_bar_check.md", "Public Product Bar Check", "Verify the candidate meets the public-product minimum bar.", "data_analysis", "Use Stage 1-2 evidence IDs and public-product bar checks.", True),
            Substage("02_github_visitor_test.md", "GitHub Visitor Test", "Test whether a stranger would understand and star the repo quickly.", "data_analysis", "Use README/GitHub/distribution evidence IDs.", True),
            Substage("03_30_minute_copy_test.md", "30-Minute Copy Test", "Assess whether a competent developer could copy most of it quickly.", "data_analysis", "Use competitor/comparable-product evidence IDs.", True),
            Substage("04_risk_compliance_check.md", "Risk / Compliance Check", "Assess legal, security, API, data, and secret-handling risks.", "data_analysis", "Use risk evidence, local files, and API/security constraints.", True),
            Substage("05_kill_continue_decision.md", "Kill / Continue Decision", "Choose CONTINUE, PIVOT, PAUSE, KILL, or BUILD_INTERNAL_ONLY.", "data_analysis", "Use all Q-Gate evidence and choose the conservative decision.", True),
        ),
        artifacts=("q-gate-report.md", "pre-mortem.md"),
    ),
    Stage(
        folder="04_product_discovery",
        name="Product Discovery",
        substages=(
            Substage("01_persona_refinement.md", "Persona Refinement", "Tighten the user persona using prior demand evidence.", "research", "Use Stage 1-3 evidence IDs; no new persona claims without source."),
            Substage("02_use_case_map.md", "Use-Case Map", "Map specific use cases and user jobs.", "research", "Use evidence-backed use cases from prior substages."),
            Substage("03_opportunity_solution_tree.md", "Opportunity-Solution Tree", "Connect opportunities, solutions, assumptions, and experiments.", "data_analysis", "Use prior evidence IDs and assumption scoring.", True),
            Substage("04_core_workflow_design.md", "Core Workflow Design", "Define the input-processing-result-next-action workflow.", "data_analysis", "Use user-journey evidence and demo evidence.", True),
            Substage("05_assumption_map.md", "Assumption Map", "List and prioritize product, demand, and technical assumptions.", "data_analysis", "Use prior evidence and classify unsupported items as hypotheses.", True),
            Substage("06_mvp_direction.md", "MVP Direction", "Choose the narrow MVP direction that preserves public-product depth.", "data_analysis", "Use prior product-discovery evidence and conservative decision rules.", True),
        ),
        artifacts=(
            "product-discovery.md",
            "assumption-map.md",
            "opportunity-solution-tree.md",
            "method-fit-map.md",
            "analytical-core-design.md",
            "uncertainty-and-assumption-map.md",
            "core-capability-design.md",
            "input-automation-map.md",
            "core-mechanism-design.md",
            "ui-specificity-design.md",
            "fixture-plan.md",
            "real-world-depth-design.md",
            "ecosystem-compatibility-plan.md",
            "external-data-integration-plan.md",
            "real-corpus-benchmark-plan.md",
            "business-workflow-map.md",
            "data-sufficiency-map.md",
            "constraint-map.md",
            "source-system-map.md",
        ),
    ),
    Stage(
        folder="05_mvp_specification",
        name="MVP Specification",
        substages=(
            Substage("01_prd.md", "PRD", "Define the product requirements and non-goals."),
            Substage("02_user_stories.md", "User Stories", "Define user stories and acceptance-oriented behavior."),
            Substage("03_ux_page_or_cli_structure.md", "UX / Page / CLI Structure", "Define the interactive product surface and user flow."),
            Substage("04_data_model.md", "Data Model", "Define data structures, files, inputs, outputs, and persistence."),
            Substage("05_api_and_nim_integration_plan.md", "API and NIM Integration Plan", "Define API/NIM usage, mock mode, and secret-safe behavior."),
            Substage("06_acceptance_criteria.md", "Acceptance Criteria", "Define build-verifiable acceptance criteria."),
            Substage("07_test_plan.md", "Test Plan", "Define smoke, unit, user-perspective, mock, and optional real-API tests."),
        ),
        artifacts=("mvp-prd.md", "technical-spec.md", "acceptance-criteria.md"),
    ),
    Stage(
        folder="06_build_execution",
        name="Build Execution",
        substages=(
            Substage("01_scaffold_log.md", "Scaffold Log", "Record project structure, setup, and initial files created."),
            Substage("02_core_logic_log.md", "Core Logic Log", "Record core mechanism implementation and rationale."),
            Substage("03_ui_or_cli_surface_log.md", "UI or CLI Surface Log", "Record user-facing surface implementation."),
            Substage("04_example_data_log.md", "Example Data Log", "Record sample data, fixtures, and expected outputs."),
            Substage("05_nim_or_mock_integration_log.md", "NIM or Mock Integration Log", "Record AI/API integration, mock mode, and secret-safe behavior."),
            Substage("06_smoke_test_log.md", "Smoke Test Log", "Record commands run, results, failures, and blockers."),
            Substage("07_readme_draft_log.md", "README Draft Log", "Record README first screen, quickstart, and demo instructions."),
        ),
        artifacts=(
            "build-log.md",
            "run-instructions.md",
            "build-depth-checklist.md",
            "core-logic-depth-report.md",
            "fixture-test-report.md",
            "real-corpus-benchmark-report.md",
            "ci-automation-readiness-report.md",
            "remediation-depth-report.md",
            "data-quality-report.md",
            "missing-field-report.md",
            "business-fixture-report.md",
            "what-if-simulation-report.md",
            "business-constraint-report.md",
            "method-implementation-report.md",
        ),
    ),
    Stage(
        folder="07_multi_agent_audit",
        name="Multi-Agent Audit",
        substages=(
            Substage("01_product_reviewer.md", "Product Reviewer", "Audit whether the product solves the original external demand.", "audit", "Use product files, build outputs, and prior evidence IDs."),
            Substage("02_engineering_reviewer.md", "Engineering Reviewer", "Audit code quality, maintainability, and repo structure.", "audit", "Use local files and terminal/test outputs."),
            Substage("03_security_reviewer.md", "Security Reviewer", "Audit secrets, injection, privacy, dependency, and API risks.", "audit", "Use local files, secret scans, dependency checks, and NIM/API constraints."),
            Substage("04_growth_reviewer.md", "Growth Reviewer", "Audit positioning, launch path, CTA, and distribution.", "audit", "Use packaging evidence and distribution source IDs."),
            Substage("05_skeptical_student_user.md", "Skeptical Student User", "Audit clarity and usefulness for a skeptical younger user.", "audit", "Use product surface and README evidence."),
            Substage("06_middle_aged_nontechnical_user.md", "Middle-Aged Nontechnical User", "Audit trust, clarity, and confusion points.", "audit", "Use product surface and README evidence."),
            Substage("07_time_poor_professional.md", "Time-Poor Professional", "Audit whether the product saves time quickly.", "audit", "Use workflow timing and user journey evidence."),
            Substage("08_github_visitor.md", "GitHub Visitor", "Audit README first screen, repo credibility, and star-worthiness.", "audit", "Use README, demo, topics, and comparable repo evidence."),
            Substage("09_implementation_depth_reviewer.md", "Implementation Depth Reviewer", "Audit core logic depth, UI specificity, fixture depth, edge-case coverage, and whether the product deserves public launch.", "audit", "Use source code, tests, fixtures, UI files, build reports, and implementation-depth artifacts."),
            Substage("10_real_world_depth_reviewer.md", "Real-World Depth Reviewer", "Audit ecosystem compatibility, external data integration, real corpus benchmark, remediation depth, automation readiness, and README claim honesty.", "audit", "Use implementation files, benchmark reports, CI/export evidence, README claims, and real-world depth artifacts."),
            Substage("11_github_readme_reviewer.md", "GitHub README Reviewer", "Audit whether the bilingual GitHub README package explains the product within 10 seconds and is worth starring.", "audit", "Use README.md, README.zh-CN.md, screenshots/GIF plan, demo instructions, GitHub metadata, claim check, and comparable repo evidence."),
            Substage("12_business_workflow_reviewer.md", "Business Workflow Reviewer", "Audit whether a non-developer operational product models real operating constraints and reduces business work rather than becoming a spreadsheet with a web UI.", "audit", "Use business workflow maps, source-system maps, data quality reports, fixtures, README, and product outputs."),
            Substage("13_method_problem_fit_reviewer.md", "Method-Problem Fit Reviewer", "Audit whether the analytical method naturally fits the problem, handles uncertainty, challenges assumptions, and avoids shallow scoring or method theater.", "audit", "Use method-fit map, analytical-core design, uncertainty map, method implementation report, tests, outputs, README, and domain evidence."),
        ),
        artifacts=("audit-report.md", "subagent-feedback.md", "fix-plan.md", "ship-or-not.md"),
    ),
    Stage(
        folder="08_packaging_launch",
        name="Packaging / Marketing / Launch",
        substages=(
            Substage("01_positioning_star_pull_angle.md", "Positioning and Star-Pull Angle", "Define product positioning, target visitor, differentiated value, and why the repo deserves a star.", "packaging", "Use product evidence, audit evidence, and comparable repo positioning patterns."),
            Substage("02_readme_first_screen.md", "README First Screen", "Make the first screen answer what the product is, who it is for, what pain it solves, what output it creates, why it matters, and how to try it.", "packaging", "Use at least 5 README first-screen examples when available.", min_evidence_rows=5, min_source_types=1),
            Substage("03_problem_differentiation_copy.md", "Problem and Differentiation Copy", "Write clear problem, why existing approaches are not enough, and why this product is useful without generic fluff.", "packaging", "Use demand evidence, product evidence, and comparable alternatives."),
            Substage("04_demo_screenshot_gif_plan.md", "Demo / Screenshot / GIF Plan", "Define the visual proof: screenshot, GIF, terminal demo, before/after, or sample output image.", "packaging", "Use product UI, sample output, smoke-test evidence, and screenshot/GIF feasibility."),
            Substage("05_quick_start_example_output.md", "Quick Start and Example Output", "Define the shortest working demo command, local URL, sample input, generated output, and output location.", "packaging", "Use actual run instructions, sample files, and smoke-test outputs."),
            Substage("06_github_description_topics.md", "GitHub Description and Topics", "Define repo description under 160 characters, longer description, alternatives, and 10-20 specific topics.", "packaging", "Use at least 10 comparable repos and 5 topic/tag examples when available.", min_evidence_rows=10, min_source_types=1),
            Substage("07_english_readme.md", "English README", "Draft the complete English README.md using the required product-page structure.", "packaging", "Use Stage 8 copy files, product evidence, and claim-check mapping."),
            Substage("08_chinese_readme.md", "Chinese README", "Draft the complete natural Chinese README.zh-CN.md with the same structure and product claims as the English README.", "packaging", "Use English README, product evidence, and Chinese launch copy."),
            Substage("09_readme_claim_check.md", "README Claim Check", "Verify every major README claim maps to implemented functionality and that limitations are honest but not self-sabotaging.", "packaging", "Use README drafts, product files, tests, roadmap, and audit evidence."),
            Substage("10_launch_summary.md", "Launch Summary", "Summarize the final launch package, GitHub metadata, demo assets, language surfaces, and launch decision.", "packaging", "Use all Stage 8 substages and Stage 7 audit decision."),
        ),
        artifacts=("README.md", "README.zh-CN.md", "launch-summary.md", "readme-final.md", "readme-final-zh-CN.md", "landing-page-copy.md", "github-description.md", "github-description-zh-CN.md", "github-topics.md", "launch-posts.md", "launch-posts-zh-CN.md", "seo-keywords.md", "poster-brief.md", "poster-image-brief.md", "distribution-plan.md", "demo-instructions.md", "bilingual-github-release-plan.md", "readme-claim-check.md"),
    ),
    Stage(
        folder="09_post_launch_feedback",
        name="Post-Launch Feedback",
        substages=(
            Substage("01_metrics_collection.md", "Metrics Collection", "Collect launch metrics or record why launch did not happen."),
            Substage("02_issue_feedback_review.md", "Issue Feedback Review", "Review GitHub issues and support-like feedback."),
            Substage("03_distribution_feedback_review.md", "Distribution Feedback Review", "Review channel feedback and launch response."),
            Substage("04_user_comment_synthesis.md", "User Comment Synthesis", "Synthesize user comments, objections, and requests."),
            Substage("05_continue_pivot_kill_decision.md", "Continue / Pivot / Kill Decision", "Decide whether to continue, pivot, pause, or kill."),
        ),
        artifacts=("feedback-summary.md", "metrics-summary.md", "continue-pivot-kill.md"),
    ),
    Stage(
        folder="10_reflection_memory",
        name="Reflection / Memory Update",
        substages=(
            Substage("01_what_worked.md", "What Worked", "Record what worked in demand, build, audit, packaging, and launch."),
            Substage("02_what_failed.md", "What Failed", "Record failures, false assumptions, and blockers."),
            Substage("03_overbuilt_underbuilt.md", "Overbuilt / Underbuilt Review", "Assess overbuild and underbuild."),
            Substage("04_signal_quality_review.md", "Signal Quality Review", "Review which demand and launch signals were reliable or misleading."),
            Substage("05_scoring_calibration_update.md", "Scoring Calibration Update", "Update scoring rules based on outcomes."),
            Substage("06_pattern_memory_update.md", "Pattern Memory Update", "Update reusable product and workflow patterns."),
        ),
        artifacts=("reflection.md", "memory-update.md"),
    ),
)
