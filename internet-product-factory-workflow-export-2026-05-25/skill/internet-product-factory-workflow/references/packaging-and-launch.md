# Packaging And Launch Reference

Stage 8 makes the product understandable, honest, bilingual, and star-worthy.

## Required Public Product Files

- `README.md`
- `README.zh-CN.md`
- `github-description.md`
- `github-topics.md`
- `launch-summary.md`
- `demo-instructions.md`
- `readme-claim-check.md`
- `bilingual-github-release-plan.md`

## README Structure

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
15. Language link

The first screen must answer:

- What is this?
- Who is it for?
- What pain does it solve?
- What output does it create?
- Why should I care?
- How can I try it?

If the README starts with installation, file structure, or limitations, fail the first-screen gate.

## Bilingual Rule

`README.md` is the English default.

`README.zh-CN.md` is the complete natural Chinese version.

Both must contain the same structure and claims. Do not make the Chinese version a partial machine-looking translation.

Default GitHub release plan:

- `main`: English primary public asset.
- `zh-CN`: Chinese documentation branch.
- Product code, app UI, tests, examples, env vars, API names, and schemas stay unchanged unless the user explicitly asks to localize the app itself.

## GitHub Metadata

`github-description.md` must contain:

- repo description under 160 characters
- one-paragraph long description
- three alternative descriptions

`github-topics.md` must contain 10-20 relevant topics with domain keywords and product-type keywords. No trending spam.

## README Claim Check

`readme-claim-check.md` must verify:

1. Every major claim maps to implemented functionality.
2. Roadmap features are labeled roadmap.
3. Demo-only features are labeled demo.
4. Mock features are labeled mock.
5. Limitations are grouped near the end.
6. No overclaiming.
7. No excessive self-sabotaging caveats.
8. English and Chinese README are consistent.
9. First screen is strong.
10. Quick Start works.

## Honest But Not Self-Sabotaging

Do not scatter limitations throughout the README.

Avoid repeated phrases like:

- only a prototype
- not perfect
- limited
- just a simple tool
- not production ready

Instead:

- state what the product does clearly
- keep claims honest
- put constraints in one `Limitations` section near the end
- put future work in `Roadmap`

## Launch Safety

Before pushing:

- Run tests and smoke tests.
- Run secret scan for `nvapi--`.
- Confirm no `.env` or real API key is committed.
- Confirm README claims match implemented features.
- Confirm branch plan and repo visibility.
- Push only after explicit user approval.

