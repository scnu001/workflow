# Product Patterns

Last updated: 2026-04-27

## 2026-05-03: Authority-Grounded Artifact Workbench Pattern

Strong high-stakes consumer products can win when they combine authoritative sources, a closed taxonomy, a decision tree, confidence propagation, generated user artifacts, and deadline/action tracking. The reference shape is Product-025: Medical-Bill Remedy Workbench.

Pattern:
- anchor demand and method on high-authority sources such as federal agencies, regulators, courts, statute/regulation pages, authoritative nonprofits, or peer-reviewed research
- parse user documents into structured facts with confidence labels
- classify those facts against a closed taxonomy
- apply a decision tree or jurisdiction/policy overlay
- produce a user-ready artifact such as a letter, appeal, packet, complaint, response, calendar, patch, or filing checklist
- include deadlines, evidence requirements, limitations, and referral/disclaimer language
- test against a fixture matrix that includes normal, edge, malformed, complex, negative/no-issue, and jurisdiction/source variants

Applies to: medical bills, immigration paperwork, tax notices, insurance appeals, benefit denials, small claims, landlord/tenant notices, warranty disputes, school appeals, and other high-stakes one-time paperwork.

Weak version to avoid: generic LLM letter drafter, generic checklist, shallow parser, or dashboard/report that does not include citations, confidence labels, rule logic, fixture coverage, and a concrete user artifact.

## Useful Pattern
Local-first developer CLI products are a strong fit for this factory because they can be researched, built, tested, audited, and packaged in one session.

## Calibration Warning
Local-first CLI products can be too easy. They are excellent for internal tooling and workflow validation, but many are not valuable enough to consume scarce public GitHub launch slots.

## Product Shape
- No external API for v1.
- Markdown report output.
- Self-audit as demo.
- GitHub-first packaging.
- GitHub metadata packaging: clear About description plus topics for category, language, use case, and audience.

## Higher-Value Product Pattern
Prefer public launches that combine:
- a painful, specific user problem
- a visible demo or benchmark
- a differentiated angle
- a clear GitHub-star reason
- a future monetization or lead-capture path
- reusable compound value for the factory

## Daily Batch Pattern
The 2026-04-27 batch showed that local-first Python CLIs are excellent for speed, testability, and repo polish. They are weaker on perceived depth unless the repo has one of these:
- a benchmark or measurable score
- a practical security/cost/compliance angle
- a recognizable platform keyword such as GitHub Actions, NIM, environment variables, or prompt injection
- a direct connection to a painful daily developer workflow

Future products should aim for "small but consequential" rather than merely "small and shippable."

## Public Product Pattern
Prefer products with:
- local web app or strong interactive surface
- visible before/after demo
- sample input and output
- non-trivial mechanism such as simulation, clustering, agent pipeline, benchmark, visualization, API integration, or report generation system
- external persona and pain
- expected star pull from README first screen

Downgrade thin standalone tools to `INTERNAL_FACTORY_TOOL` unless they are part of a larger product suite.

## Evidence Pattern For High-Quality Public Products
High-quality public products usually require:
- real demand evidence
- explicit scoring
- a visible demo moment
- complete workflow
- non-trivial mechanism
- GitHub packaging
- audit before launch

These should be proven through substage evidence files, not inferred from a single broad report.

## Pattern: Local Cost/Risk Simulator For AI Workflows

Strong public-product pattern: external user pain, numeric scenario engine, visible dashboard, sample input/output, exportable report, and optional AI advisor with mock mode. Avoid reducing this pattern to a one-shot token calculator; the value is workflow-level success-adjusted cost and retry sensitivity.

## Pattern: Strong Analytics / Simulator Product

Strong analytics and simulator products usually require:
- real data import
- configurable assumptions
- uncertainty handling
- robustness/sensitivity analysis
- low-friction first result
- clear distinction between demo mode and real mode

Weak version: manual JSON -> deterministic formula -> formatted report. Strong version: real data path -> automatic parsing/extraction/estimation -> configurable assumptions -> uncertainty-aware recommendations -> exportable report.

## Pattern: Repairing A Shallow But Promising Product

When the idea is valuable but the first build is too shallow, improve the core product mechanism instead of generating a new product. The repair sequence should be:
- identify the implied core capability
- replace manual sample input with a real data path
- add import/parsing/validation
- add user-editable configuration
- separate measured values from estimates
- add robustness and sensitivity checks
- update README claims so packaging matches implemented behavior
- rerun smoke tests against the real-data path

Product-011 is the reference repair example: Agent Budget Lab moved from manual workflow JSON calculator to local trace-import budget lab.

## Pattern: Bilingual GitHub Packaging

For public products, use English as the default GitHub asset and Chinese as a separate documentation branch when the user wants Chinese-facing launch material. The product code should remain unchanged across language branches unless product localization is explicitly requested.

Recommended shape:
- `main`: English README, English repo description, English launch copy, English-first GitHub discovery.
- `zh-CN`: Chinese README and Chinese GitHub-facing explanatory markdown.
- Shared across branches: app code, tests, sample schemas, API names, env vars, commands, and behavior.

GitHub repo description and topics are repository-level, so they cannot vary by branch. Keep repo-level metadata English by default unless the user explicitly wants Chinese metadata or a separate Chinese repo.

## Pattern: Browser AI As External Reviewer

Use the logged-in ChatGPT web UI as an external reviewer for non-build stages when the user wants model diversity or a stronger product-research pass. Keep the local factory file-driven:
- write prompt to Markdown
- send prompt through the browser UI
- capture response back into Markdown
- synthesize locally from the file
- never let browser chat history become the source of truth

Use a new browser chat when the task needs isolation, a clean product-review context, or a different stage. Continue the same browser chat when the follow-up depends on the prior browser answer and the MD record names that dependency.



## Pattern: Agent-Readable File Security Scanner

Strong version: scan real local repository files such as AGENTS.md, CLAUDE.md, Cursor rules, MCP configs, and workflow files; produce line-level findings, masked evidence, confidence, recommendations, and exportable reports. Weak version: paste a prompt into a text box and ask an LLM whether it looks risky.


## Pattern: Agent-Readable File Security Scanner

Strong version: scan real local repository files such as AGENTS.md, CLAUDE.md, Cursor rules, MCP configs, and workflow files; produce line-level findings, masked evidence, confidence, recommendations, and exportable reports. Weak version: paste a prompt into a text box and ask an LLM whether it looks risky.


## Pattern: Agent-Readable File Security Scanner

Strong version: scan real local repository files such as AGENTS.md, CLAUDE.md, Cursor rules, MCP configs, and workflow files; produce line-level findings, masked evidence, confidence, recommendations, and exportable reports. Weak version: paste a prompt into a text box and ask an LLM whether it looks risky.


## Pattern: Local CI Failure Storyboard

Strong CI products need real log import, failure taxonomy, timeline, rerun guidance, fix plan, and scoped local-first claims. Weak CI products only summarize pasted logs.


## Pattern: Local CI Failure Storyboard

Strong CI products need real log import, failure taxonomy, timeline, rerun guidance, fix plan, and scoped local-first claims. Weak CI products only summarize pasted logs.


## Pattern: Spec-vs-Code Drift Radar

A crowded diff market can still yield a public product if the wedge checks two real artifact types that competitors do not center. OpenAPI Route Drift Radar compares OpenAPI specs to backend route files instead of cloning spec-to-spec diff tools.
## 2026-04-28: Local Security Explainer Pattern

Promising GitHub-adjacent public products can be small when they import real repository files and convert confusing configuration into a concrete action report. A strong v1 pattern is local-only scan, visible risk score, categorized findings, direct evidence, concrete remediation, sample repo, smoke test, and honest scope against mature competitors.

## 2026-04-28: Strong Implementation Pattern

Strong products require at least one deep mechanism: real parser, graph model, timeline model, simulation model, sensitivity analysis, auto-fix patch, real import path, benchmark suite, SDK/proxy/plugin, domain-specific visualization, configurable rules, or multiple realistic fixtures. The product-specific UI should expose the actual domain structure: timeline for CI failures, route diff for API drift, permission/trigger matrix for Actions security, cost curve for budget simulation, or equivalent domain view. A generic upload/report shell is only acceptable when the core mechanism is clearly strong.

## 2026-04-28: Real-World Depth Pattern

Strong developer products need ecosystem compatibility, external data honesty, remediation depth, real corpus benchmarks, automation readiness, domain-specific UI, and README claim honesty. For dependency tools, strong patterns include support for multiple lockfile versions, workspaces/monorepos, dev/prod/optional/peer dependencies, overrides/resolutions, large lockfiles, advisory-data integration, direct dependency blame, override suggestions, CI mode, JSON/Markdown/SARIF exports, and benchmark evidence on realistic projects.

## 2026-04-28: Category-Neutral Demand Discovery Pattern

Strong product selection begins with broad demand pools rather than a preselected audience. The factory should inspect developer/AI builder, student/applicant, job seeker, creator, small business, personal finance, life-admin, productivity/AI tool, education, and emerging niche demand before framing product opportunities.

Developer products remain valid when they win on evidence quality, repeated pain, feasibility, distribution, demo potential, and product depth. Non-developer products remain valid when evidence supports them; they should not be forced to satisfy a quota. The strongest pattern is category-neutral selection: compare the top developer candidate against the top non-developer candidate and explain why the winner earned the slot.

## 2026-04-28: Receivables Triage Pattern

Product-017 shows a useful non-developer local-first pattern: import a CSV export from an existing business workflow, convert raw rows into a prioritized action queue, and export a report the user can act on immediately. Strong elements include real data path, domain-specific UI, risk scoring, client aggregation, copy-ready next actions, and honest scope. Weakness before public launch: needs richer real corpus, screenshots, and optional integrations if positioned beyond local triage.

## 2026-04-28: Product-Style GitHub README Pattern

Strong public repos need a README that behaves like a compact product landing page. The first screen should communicate product name, one-line positioning, 3 concrete value bullets, demo/screenshot cue, and a quick way to try it. The body should explain the pain, why existing/manual approaches are not enough, the input -> processing -> output workflow, concrete features, demo/output examples, use cases, how it works, roadmap, and limitations near the end.

For this factory, every public product should ship with both `README.md` and `README.zh-CN.md`. The Chinese version should be complete and natural, not a partial literal translation. GitHub description, topics, launch summary, and README claim check are part of the product package, not optional polish.

## 2026-04-28: Inventory Reorder Desk Pattern

Small-business inventory products become meaningfully useful when they move beyond "low stock" and calculate reorder point, safety stock, stockout timing, MOQ-adjusted order quantity, vendor grouping, and slow-mover avoidance. Strong V1 shape: flexible CSV export import, realistic 20+ SKU fixture, vendor purchase board, risk lanes, action-specific report, and honest roadmap for live Shopify/Square/QuickBooks integrations.

## 2026-04-28: Strong Business Workflow Product Pattern

Strong business workflow products usually include:
- natural input path
- source-system awareness
- data sufficiency checks
- missing-field confidence downgrade
- operational constraints
- actionable next steps
- realistic fixtures
- what-if analysis
- honest README claims

Weak version: CSV/XLSX -> score -> dashboard/report -> generic advice. Strong version: natural export or manual intake -> flexible mapping -> data quality review -> constraint-aware decision model -> prioritized action board -> what-if/sensitivity -> copyable/exportable next steps.

## 2026-04-28: Chargeback Evidence Desk Pattern

Strong payment-dispute products need source-system aware intake, deadline triage, reason-specific evidence requirements, missing-evidence detection, confidence labels, and a packet-style output. Avoid claiming legal advice, guaranteed win probability, direct processor integration, or OCR unless actually implemented.

## 2026-04-30: Method-Architecture Product Pattern

Strong analytical products usually have a method architecture that naturally fits the problem:
- decision products: multi-criteria decision analysis, utility ranking, scenarios, uncertainty, sensitivity analysis, devil's advocate challenge, and synthesis
- inventory products: reorder point, safety stock, lead-time demand, budget constraints, and supplier-delay sensitivity
- subscription audit products: recurring pattern detection, merchant normalization, cadence inference, confidence scoring, and user confirmation
- dependency products: graph traversal, centrality, blast radius, path explanation, and advisory integration if claiming security
- deadline/return products: policy rule matching, deadline basis detection, confidence scoring, evidence checklist, and reminder workflow

Weak version: parse input -> score fields -> generate Markdown. Strong version: choose the right method family -> expose assumptions -> test uncertainty -> challenge recommendations -> produce a decision-impacting output. Do not add Monte Carlo, multi-agent debate, or optimization unless the problem naturally calls for it.

## 2026-05-01: High-Stakes One-Time Paperwork Workbench Pattern

A workbench that takes a single high-stakes document (medical bill, RFE, small-claims complaint, insurance appeal, immigration form) the user does once, classifies it against a closed authoritative taxonomy, applies a regulatory decision tree, applies state/jurisdiction overlays, and assembles a regulation-cited generated artifact (letter, response, complaint). Strong elements: closed taxonomy, decision-tree branches with citations, fact-extracted templated drafting, confidence-label propagation, deadline calculator with .ics export, drafting-aid disclaimer + advocate referral. Weak version (avoid): generic LLM wrapper that drafts a letter without rules engine, without citations, without reconciliation.

## 2026-05-01: Confidence-Label Propagation Pattern

For products with heuristic parsing + rules + drafting, propagate a Confidence enum (HIGH / MEDIUM / LOW) from parser -> match -> finding -> letter via a `weakest()` helper. This prevents silent confident output when input is partial or OCR-fragile. Applies to any pipeline that touches user-paste content with structural extraction.

## 2026-05-01: Mock-by-Default LLM Polish Pattern

For deterministic products that can optionally benefit from LLM polish, implement a polish path that returns input unchanged when env vars are unset (mock mode), lazy-imports the LLM SDK, and silently falls back to mock on any error / timeout / missing dependency. The deterministic output must stand alone. This satisfies AGENTS.md NIM rules naturally and avoids method-theater dependence on LLM quality.
## 2026-05-03: Natural Method Practice Workbench Pattern

Product-026 showed a useful education-product shape: when the domain is skill practice, depth should come from the discipline's natural method, not arbitrary AI complexity. Japanese Pitch Accent Practice Workbench used local audio signal processing, mora-level segmentation, pitch-accent pattern comparison, confidence labels, corrective hints, and a practice action plan. This is stronger than a generic "upload audio -> score -> report" product because the learner sees the domain-specific evidence needed to improve the next attempt.

Reusable pattern: identify the skill's smallest meaningful practice unit; measure the user's actual attempt; compare against a domain-specific reference model; expose the comparison visually at the unit level; label confidence; generate the next practice action.

Weak version warning: a practice product is shallow if it only accepts manually typed scores, returns a generic grade, hides the evidence, or uses method theater unrelated to the skill.
