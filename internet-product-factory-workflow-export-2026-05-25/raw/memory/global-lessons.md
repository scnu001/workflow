# Global Lessons

Last updated: 2026-04-27

## 2026-05-03: Product-025 Execution Discipline Lesson

Product-025 exposed the biggest gap in my own execution: the workflow itself is not a quality guarantee. It only works when the agent treats it as a mandatory design system, not as a checklist to satisfy after the fact. Product-025 was stronger because it completed the full chain: broad evidence -> method fit -> modular architecture -> fixture matrix -> audit -> packaging. Earlier products often reached a runnable local app faster, but reached it by compressing or lightly filling the evidence and method stages.

The quality difference was not mainly caused by model capability. It came from execution discipline. Product-025 did not pick the easiest safe topic; it picked a higher-pain, higher-risk, higher-authority opportunity and then used the workflow gates to shape a deeper implementation. It anchored demand on federal and policy sources, designed a closed taxonomy plus decision-tree mechanism, generated a user-ready artifact, and tested the mechanism against a matrix of scenarios.

My failure mode to correct: entering build too early, treating `Status: NOT_STARTED` scaffold files as harmless background noise, satisfying validator structure instead of completing substantive reasoning, and shipping products whose value is mostly a dashboard/report rather than a real-world artifact the user can act on.

New rule: a product cannot be called workflow-complete just because the required files exist. Before final completion, run a substance audit that checks for scaffold residue, incomplete stage reasoning, one-module core implementation, shallow fixture/test depth, and whether the output is merely a report instead of a decision-moving artifact.

## product-001: LaunchLint
- The workflow can produce a real product, not only documents.
- Indexing scripts must tolerate markdown indentation.
    - Stage 8 should check both GitHub tooling and GitHub authentication before promising upload.
    - Once `gh` is installed and authenticated, the workflow can create and push a public product repo directly from Stage 8.
    - GitHub About metadata matters for stars and discovery. Stage 8 must set a clear description and relevant topics before considering a repo launched.
- Blocker logging kept the run moving without hiding failure.

## Portfolio Constraint
- The factory can potentially produce around 100 small projects per day, but the publishing policy caps GitHub pushes at 10 repos/day.
- This makes GitHub slots scarce. Stage 2 must behave like portfolio selection.
- "Easy to build" is not enough. A public repo must earn its slot through expected user value, distribution leverage, differentiation, and upside.
- Low-depth utilities can still be built as internal tools, workflow tests, or bundled infrastructure, but should not crowd out higher-upside public launches.

## Daily Batch 2026-04-27
- The factory successfully produced and published 10 GitHub repos in one day: product-001 through product-010.
- GitHub metadata must be part of the launch definition, not a later cleanup step: description, topics, README first screen, license, security file, examples, tests, and launch posts.
- The batch loop works technically, but the products are still mostly small CLI utilities. Future batches should reserve slots for higher-upside products with visible demos, stronger distribution hooks, or monetization paths.
- Secret hygiene worked: the user-provided NVIDIA NIM key was not written to disk; only generic environment variable placeholders are allowed.
- The product index needed a fallback parser for Q-Gate decisions because stage files may record the decision under a heading instead of a bullet field.
- User review rejected the batch as too low-value for public GitHub inventory. The repos were deleted from GitHub and retained locally only as workflow evidence.

## Public Product Quality Failure - 2026-04-27
Summary: The factory successfully generated runnable tools, but failed the public-product quality bar. The 10 generated CLI tools were technically complete but mostly shallow internal utilities. They did not deserve standalone GitHub public release slots.

Lesson: Technical completion is not product completion.

New rule: Checklist/analyzer/parser/config checker/README optimizer/log summarizer/.env sync/small one-file CLI tools are `INTERNAL_FACTORY_TOOL` by default.

Public products require:
- external user pain
- complete workflow
- demo depth
- non-trivial mechanism
- strong GitHub packaging
- expected star pull
- low 30-minute copy risk

## Substage State Machine Principle - 2026-04-27
Technical completion is not enough. Classification gates are not enough. A workflow stage is not complete unless its reasoning is decomposed into concrete substage evidence files.

New principle:

Files are memory. Substages create evidence. Stage reports synthesize evidence. Next-stage briefs carry compressed context forward.

Every completed substage must contain specific findings, evidence or signal descriptions, scores where applicable, risks, output to the next substage, and an explicit decision. If the evidence is weak or unavailable, the correct behavior is to record the blocker, not to fill the file with generic analysis.

## Evidence-First Rule - 2026-04-27
A long report is not evidence. A model-generated essay is not research. A single calculation is not analysis. A product decision requires evidence, baseline analysis, robustness checks, and conservative classification.

No evidence, no conclusion. No robustness, no ranking. No demo, no public product.

Every research-heavy substage must write an Evidence Pack, Source Log, Analysis, and Decision in that order. Major claims in analysis must cite evidence IDs. If evidence is unavailable, write: `Evidence unavailable. This is a hypothesis, not a finding.`

## 2026-04-27 - First Evidence-First State-Machine Product Run

Product-011 proved that the hardened workflow can select and build one deeper local product instead of ten shallow tools. Agent Budget Lab was chosen because the evidence connected AI agent cost, retry, attribution, and model-routing pain to a demoable local web app. Technical completion was paired with evidence logs, source logs, Q-Gate, audit, packaging, and memory. New lesson: a product can pass local build only when evidence, simulation depth, and packaging move together.

## 2026-04-27 - Product-011 Depth Failure Lesson

The factory fixed shallow CLI generation, but product-011 revealed a new failure mode: a product can have a frontend, backend, README, smoke test, sample JSON, and demo while still being shallow. Agent Budget Lab found a real demand, but the implementation downgraded the idea into a manual JSON calculator. The user still had to provide token counts, prices, failure rates, and structured workflow assumptions manually.

New rule: future workflow runs must check core capability, input automation, real data path, configuration freshness, estimation accuracy, and user friction before launch. A frontend does not equal product depth. A strong product reduces user work, not asks the user to do the work first.

## 2026-04-27 - Product-011 V2 Repair Lesson

Agent Budget Lab was repaired by moving the product's center of gravity from manual assumptions to imported evidence. The product now supports JSONL/JSON/CSV trace import, field detection, workflow extraction, custom pricing import, pricing freshness metadata, measured-vs-estimated uncertainty labels, robustness/sensitivity scenarios, report export, and mock/NIM advice.

New lesson: if a product idea is strong but implementation depth is weak, do not abandon it too early. Repair the core capability first. A strong V2 should remove user work, automate data entry where possible, and make uncertainty explicit.

## 2026-04-27 - Bilingual GitHub Packaging Lesson

Public GitHub launches should support an English primary asset and a Chinese documentation branch when the target audience includes Chinese readers. Branch localization should change descriptive materials, not product behavior. README clarity matters in both languages: each version must explain what the product does, what pain it solves, how to run it, what is implemented, and what is not claimed.

## 2026-04-27 - Browser AI Reviewer Preference

The user wants the logged-in ChatGPT web account in the Codex in-app browser to be used as an external AI reviewer for early product workflow stages. Preferred division of labor:
- Browser ChatGPT: demand research prompts, product research, product discovery, lightweight evaluation, launch copy review, external reviewer perspectives, and simple reasoning tasks.
- Local Codex: code writing, repo construction, file edits, tests, local validation, packaging mechanics, and workflow record maintenance.
- Local Python/scripts: quantitative calculations, robustness checks, validation scripts, trace parsing, and repeatable computation.

Default behavior: for ordinary product-research prompts, external reviewer prompts, and non-secret workflow context, Codex may submit prompts to the logged-in ChatGPT web UI without asking every time. All prompt/response handoff must still be written to Markdown files. The browser AI output is model advice, not evidence by itself, unless it cites verifiable sources that are separately logged.

Boundary retained: do not send passwords, MFA codes, raw API keys, payment credentials, destructive account actions, or public sharing/permission changes without explicit action-time confirmation.



## Product-012 Lesson - Agent Rules Risk Radar

A second product can pass the product-depth repair rule when it scans real local data instead of asking users to manually describe risk. Agent Rules Risk Radar uses a local folder path, line-level findings, masked evidence, and Markdown/JSON reports. The next calibration issue is not frontend depth; it is false-positive control and integration depth such as SARIF, CI, and GitHub URL import.


## Product-012 Lesson - Agent Rules Risk Radar

A second product can pass the product-depth repair rule when it scans real local data instead of asking users to manually describe risk. Agent Rules Risk Radar uses a local folder path, line-level findings, masked evidence, and Markdown/JSON reports. The next calibration issue is not frontend depth; it is false-positive control and integration depth such as SARIF, CI, and GitHub URL import.


## Product-012 Lesson - Agent Rules Risk Radar

A second product can pass the product-depth repair rule when it scans real local data instead of asking users to manually describe risk. Agent Rules Risk Radar uses a local folder path, line-level findings, masked evidence, and Markdown/JSON reports. The next calibration issue is not frontend depth; it is false-positive control and integration depth such as SARIF, CI, and GitHub URL import.
## 2026-04-28: Product-015 Action Blast Radius

Action Blast Radius is a stronger pattern than manual calculators because it reads real local workflow files instead of asking users to prepare structured JSON. The useful shape is: real data path -> deterministic extraction -> risk map -> concrete fixes -> Markdown/README-ready report. The main caution is to scope claims honestly when mature tools already exist; position as a readable blast-radius explainer, not a full replacement for static analyzers.

## 2026-04-28: Reused Shell + Shallow Backend Failure Mode

The factory fixed shallow CLI generation and manual JSON calculator risk, but the latest batch exposed another failure mode: a product may have a frontend, backend, README, samples, smoke tests, and GitHub packaging while still being toy-level. The pattern is reused frontend shell, similar backend structure, a small rule-based analyzer, toy sample data, happy-path-only tests, and generic Markdown output. Similar architecture is acceptable, but each product must now pass implementation depth, UI specificity, core mechanism, fixture depth, and output actionability gates before it can be treated as a strong `PUBLIC_PRODUCT` or `TOP_10_PUBLISH`.

New principle: a product can reuse a scaffold, but it cannot reuse the same shallow soul.

## 2026-04-28: Product-016 Real-World Depth Gap

Product-016 was better than earlier products because it used real `package-lock.json` input, dependency graph construction, path tracing, hotspot scoring, duplicate-version aggregation, install-script detection, and multiple fixtures. But it exposed another workflow gap: a product can have a real core mechanism and still be too shallow for top-tier publication if it only handles toy ecosystem examples and lacks real-world compatibility, external authoritative data, remediation depth, real corpus benchmarks, and CI automation readiness.

New rule: before `TOP_10_PUBLISH`, products must pass the Real-World Depth Gate. A dependency/security/risk product must either integrate authoritative external data such as OSV, GitHub Advisory, npm audit, package metadata, or deprecation info, or clearly label output as structural/local/heuristic. Toy fixtures are not enough. Developer tools need automation/export paths. README claims must match implementation depth.

## 2026-04-28: Demand Discovery Bias Correction

The factory became biased toward developer tools because Codex operates inside code repositories, GitHub publishing rewards developer-facing projects, and the easiest evidence sources were GitHub, Hacker News, and devtool pain. The fix is not to ban developer tools and not to force consumer, student, finance, or small-business tools.

New principle: do not preselect the audience. Start from broad evidence-first demand discovery across multiple demand pools, then select the strongest opportunity based on evidence quality, pain intensity, feasibility, distribution, demo potential, and product depth. Developer tools are allowed when they truly win the comparison, but if the shortlist is developer-heavy the workflow must explain why that evidence is stronger than non-developer alternatives.

## 2026-04-28: Product-017 Broad Demand Run

Product-017 validated the broad-demand workflow by selecting a non-developer opportunity without forcing one. Invoice Chase Desk won because small business and freelancer late-payment signals were stronger than the developer-tool alternative on external pain, buyer value, and source diversity. The product was built locally but not pushed to GitHub. Lesson: broad discovery can move the factory outside developer tools when evidence supports it, while still preserving product-depth gates.

## 2026-04-28: GitHub Presentation Packaging Gap

The factory can now build runnable products, but GitHub presentation is still a separate quality gate. README files were at risk of reading like technical notes instead of product landing pages. A public repo visitor needs to understand the product quickly: what it is, who it is for, what pain it solves, what output it creates, why existing approaches are worse, how to try it, and why it is worth starring.

New rule: future `PUBLIC_PRODUCT` repos require bilingual README files, strong first-screen positioning, clear differentiation, demo/output examples, GitHub metadata, and limitations grouped near the end. The README must be honest without self-sabotaging. Roadmap features stay in Roadmap, demo-only features are labeled as demo, mock features are labeled as mock, and every major claim must map to implemented functionality.

## 2026-04-28: Product-018 Restock Radar

Restock Radar confirms the broad-demand workflow can select a non-developer product without forcing the category. A strong small-business pattern is: operational CSV/POS export -> flexible mapping -> domain-specific calculations -> prioritized action board -> Markdown/JSON report. The product was published to GitHub with English main branch and Chinese `zh-CN` branch. Next improvement: add broader real-corpus fixtures and optional Shopify/Square presets.

## 2026-04-28: Business Workflow Depth Gate

Restock Radar improved over earlier products because CSV/POS export input was more natural for inventory planning and its core mechanism included reorder logic, safety stock, ABC/XYZ classification, vendor boards, and sensitivity analysis. However, it revealed a new workflow requirement: non-developer business products must not stop at CSV analysis. They must model real business constraints, data sufficiency, source-system fit, operational actions, what-if scenarios, and realistic messy inputs.

New rule: a business product must reduce real operating work. It is not enough to import a CSV, calculate a score, show a dashboard, generate a report, or write generic recommendations. Future operational products must answer what to do next, what to do first, why, under what constraint, with what risk, and what changes if assumptions change.

## 2026-04-28: Product-019 Chargeback Evidence Desk

Product-019 applied the Business Workflow Depth Gate to a non-developer payment-dispute workflow. The stronger pattern was not "chargeback CSV analyzer"; it was local dispute intake -> normalized review -> deadline/evidence scoring -> reason-specific missing-evidence queue -> packet draft. This shows business products can stay local-first while still modeling real operating constraints: deadline, amount at risk, source system, evidence sufficiency, review confidence, and platform scope.

Lesson: a business workflow product becomes more valuable when it tells the user what to do next and why, while clearly labeling uncertainty and not overclaiming legal, API, or OCR capabilities.

## 2026-04-30: Disciplinary Method Fit Gate

The user-created AI Decision Engine is stronger than many factory-generated products because it has a real method architecture: dynamic decision framework generation, user-reviewed weights and scenarios, multiple specialized agents, official data research, community sentiment research, Monte Carlo simulation, utility ranking, sensitivity analysis, devil's advocate challenge, long-term forecasting, final synthesis, and process review.

New lesson: future products must not stop at surface workflow, input parsing, light scoring, and report generation. When a product is analytical, it needs a natural method core that fits the problem. Monte Carlo is valuable for decisions, risk, forecasts, uncertainty, and scenario analysis, but it is method theater for deterministic deadline checks unless uncertainty modeling changes the user's decision.

New rule: before `TOP_10_PUBLISH`, analytical products must pass Disciplinary Method Fit, Method Depth, and Multi-Perspective Reasoning gates. No method theater. No fake complexity. No shallow scoring disguised as analysis.

## 2026-05-01: Product-025 — High-Stakes One-Time Paperwork Shape

Product-025 (Medical-Bill Remedy Workbench) proved that a non-developer / non-CSV product can clear the public-product bar when it (a) is anchored on federal-source authority (CMS.gov, KFF, peer-reviewed academic), (b) implements a closed-taxonomy rules engine + decision-tree mechanism, (c) outputs a generated artifact (regulation-cited letter) rather than a dashboard, and (d) propagates confidence labels end-to-end. All 13 audit reviewers approved; 0 / 13 returned NEEDS_V2_BEFORE_LAUNCH.

New lesson: the operator's "don't anchor on prior products" instruction can be operationalized as a Q-Gate hard rule (Prior Shape Resemblance Risk ≤ 4). This catches relabeled prior shapes even when they would otherwise score well.

New lesson: for regulated-domain consumer products (healthcare, immigration, court self-help, tax), federal-source authority is the highest-value evidence type. Stage 1 source-budget rule should bias toward federal sources for these domains; Stage 2 should weight Source Authority ≥ 9 only when federal is the primary anchor.
## 2026-05-03: Product-026 Natural Method Lesson

Product-026 showed that a product can escape the factory's prior report/dashboard pattern by choosing a natural method core. For Japanese pitch accent practice, the right depth was not Monte Carlo, multi-agent debate, or a generic LLM tutor. It was local signal processing, mora-level segmentation, pitch-pattern comparison, confidence labels, and a practice action plan.

Future education and practice products should identify the smallest meaningful user attempt, measure it directly, expose domain-specific evidence, and turn feedback into the next drill. If the product only returns a generic score or hides the evidence, it should be downgraded even if the UI looks polished.
