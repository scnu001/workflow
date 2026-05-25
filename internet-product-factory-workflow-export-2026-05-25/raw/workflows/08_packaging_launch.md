# Stage 8: Packaging / Marketing / Launch

## Purpose
Make the GitHub asset understandable, product-oriented, bilingual, honest, and star-worthy.

Stage 8 is not allowed to produce a README that reads like a technical note. A good GitHub launch page must quickly explain what the product is, who it is for, what pain it solves, why existing/manual/traditional approaches are worse, what is different, how to try it quickly, what the output looks like, and why it is worth starring.

## Required Input Files
- Stage 7 `next-stage-brief.md`
- `audit-report.md`
- `fix-plan.md`
- product README and demo files

## Required Substages
1. `01_positioning_star_pull_angle.md` - Positioning and Star-Pull Angle
2. `02_readme_first_screen.md` - README First Screen
3. `03_problem_differentiation_copy.md` - Problem and Differentiation Copy
4. `04_demo_screenshot_gif_plan.md` - Demo / Screenshot / GIF Plan
5. `05_quick_start_example_output.md` - Quick Start and Example Output
6. `06_github_description_topics.md` - GitHub Description and Topics
7. `07_english_readme.md` - English README
8. `08_chinese_readme.md` - Chinese README
9. `09_readme_claim_check.md` - README Claim Check
10. `10_launch_summary.md` - Launch Summary

## Required Output Files
- all required substage files
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
- `distribution-plan.md`
- `bilingual-github-release-plan.md`
- `readme-claim-check.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## GitHub Launch Page Gate
Every `PUBLIC_PRODUCT` must pass the GitHub Launch Page Gate before launch.

Required:
- English README: `README.md`
- Chinese README: `README.zh-CN.md`
- strong first screen
- clear repo description
- strong GitHub topics
- screenshot/GIF plan or demo-output visual
- demo instructions
- sample input/output
- honest but not self-sabotaging limitations section
- README claim check

A technically runnable product is not enough. The GitHub page must sell the product clearly without overclaiming.

## Bilingual README Requirement
Every public product must include:
- `README.md`: English default README.
- `README.zh-CN.md`: complete natural Chinese README.

Both versions must be complete and must contain the same structure and product claims. The Chinese README should read naturally, not like an awkward literal translation.

Language links:
- In `README.md`: `English | 中文`
- In `README.zh-CN.md`: `中文 | English`

## README Structure Requirement
Every public product README must follow this structure:

1. Hero Section
2. Problem
3. Why Existing Approaches Are Not Enough
4. What This Project Does
5. Key Features
6. Demo / Screenshots
7. Quick Start
8. Example Input / Output
9. Use Cases
10. How It Works
11. Project Structure
12. Roadmap
13. Limitations
14. License
15. Language / Chinese version link

The hero must include the product name, one-line positioning, 3 short value bullets, screenshot/GIF if available, and quick demo command or local URL.

## README First-Screen Gate
The first screen must answer within 10 seconds:

1. What is this?
2. Who is it for?
3. What pain does it solve?
4. What is the output?
5. Why should I care?
6. How can I try it?

If the first screen starts with installation details, file structure, or limitations, fail the gate.

## Star-Pull Copy Rule
Every README must include a `Why this is useful` section.

It must explain the product's differentiated value with concrete wording. Generic claims such as "helps productivity" are not enough.

## Limitations Rule
Do not scatter limitations throughout README.

Do not repeatedly weaken the product with phrases like:
- only a prototype
- not perfect
- limited
- just a simple tool
- not production ready
- does not really

Instead:
- describe what the product does clearly
- keep claims honest
- place constraints in one `Limitations` section near the end
- place future work in `Roadmap`

The README should be honest, but not self-sabotaging.

## GitHub Metadata Requirement
For every `PUBLIC_PRODUCT`, generate:
- `github-description.md`
- `github-topics.md`
- `launch-summary.md`
- `README.md`
- `README.zh-CN.md`

`github-description.md` must contain:
1. short repo description under 160 characters
2. longer one-paragraph description
3. 3 alternative descriptions

`github-topics.md` must contain:
- 10-20 GitHub topics
- no irrelevant trending spam
- domain-specific keywords
- product-type keywords

## Substage Quality Rule
Each completed packaging substage must follow `templates/substage-report-template.md`, contain at least 500 meaningful words, and show how the packaging improves comprehension, demo pull, distribution, or expected star pull.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` lists the final launch package, risks, secret-scan status, and whether launch happened.

## Failure / Blocker Behavior
If the GitHub Visitor would not understand the repo in 10 seconds, do not ship. If a secret is detected, stop launch and record the incident.

## Evidence-First Rule
Packaging claims must cite comparable repos, README examples, topic/tag examples, search/SEO evidence, product files, or audit evidence. No evidence, no star-pull claim. No demo, no public product.

## README Claim Check
Create `readme-claim-check.md`. Every major README claim must map to implemented functionality, a product file, a command output, or an audit finding.

Rules:
- Future roadmap must be labeled as roadmap.
- Demo-only features must be labeled as demo.
- Mock advisor must be labeled as mock if no real API is used.
- Limitations must be grouped near the end.
- No excessive self-sabotaging caveats.
- English and Chinese README must be consistent.
- README first screen must be strong.
- Quick Start must work.
- If the product only supports manual JSON simulation, README must say so clearly.
- Do not call a product observability, budget guard, trace analyzer, automatic monitor, importer, or integration unless those features exist.

## README Depth Honesty Check
Packaging must not hide a shallow implementation behind polished copy.

Rules:
- Do not overclaim advanced analysis if implementation is shallow.
- Do not imply deep AI, algorithmic, parser, graph, or security analysis if it is only rule-based.
- Label static rules clearly as static rules.
- Label sample-only support clearly as sample/demo.
- Roadmap features must be labeled as roadmap.
- If a reused frontend shell is used, README must make the domain-specific capability clear without implying unimplemented depth.

## Real-World Depth Packaging Check
README and launch copy must state:
- supported ecosystem variants
- unsupported or roadmap variants
- whether external authoritative data is used
- whether output is vulnerability/security/risk intelligence or structural/local/heuristic analysis
- benchmark/corpus scope
- automation/CI/export path
- remediation depth and next actions

Do not call a structural analyzer a vulnerability scanner unless vulnerability/advisory data is integrated.

## Business Workflow Packaging Check
For non-developer operational products, README must:
- clearly state supported input sources
- avoid pretending CSV means all exports work
- explain what assumptions are used
- show sample output
- include limitations near the end
- avoid overclaiming automation/integration

If source-system presets or integrations are roadmap, label them as roadmap. Do not imply Shopify, Square, QuickBooks, Xero, Stripe, PayPal, Etsy, WooCommerce, or Excel support unless the implemented mapping/import path actually supports that source.

## Method Explanation Honesty Check
README must explain the analytical method clearly, but must not overclaim method sophistication.

Required:
- state what method the product uses
- explain why that method fits the problem
- state important assumptions
- explain how uncertainty or confidence is handled when relevant
- explain what the method does not do in `Limitations` near the end
- label roadmap methods as roadmap

Forbidden:
- Do not claim `AI-powered`, `Monte Carlo`, `multi-agent`, `optimization`, `forecasting`, `vulnerability scanning`, or advanced analysis unless actually implemented.
- Do not use formal method language to make simple threshold scoring sound deeper than it is.
- Do not hide shallow scoring behind polished README copy.

## Bilingual GitHub Release Rule
Create `bilingual-github-release-plan.md` before launch.

Default release shape:
- `main` or default branch: English `README.md` and English GitHub packaging are the primary public product asset.
- `zh-CN` branch: Chinese README and Chinese launch copy for GitHub visitors who prefer Chinese.
- Product code, app UI, tests, examples, env vars, API names, and sample data schemas stay unchanged unless the user explicitly asks to localize the product itself.

Required bilingual artifacts:
- `readme-final.md`: English final README.
- `readme-final-zh-CN.md`: Chinese final README or Chinese branch README source.
- `github-description.md`: English repo About description. GitHub descriptions are repo-level, not branch-level.
- `github-description-zh-CN.md`: Chinese description copy for branch docs or a separate Chinese repo if explicitly requested.
- `launch-posts.md`: English launch posts.
- `launch-posts-zh-CN.md`: Chinese launch posts.

Before GitHub upload:
- Confirm branch plan.
- Confirm repo visibility.
- Confirm no secrets appear in files.
- Confirm README claims match implemented features in both languages.
- Do not push without explicit user approval for the public upload.
