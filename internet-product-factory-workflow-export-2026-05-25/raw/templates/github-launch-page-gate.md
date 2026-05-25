# GitHub Launch Page Gate

## Purpose

Future `PUBLIC_PRODUCT` repos must look like useful GitHub products, not technical notes. The launch page must help a visitor quickly understand what the product is, who it is for, what pain it solves, what output it creates, why it is different, and how to try it.

## Bilingual README Requirement

Every `PUBLIC_PRODUCT` must include:

- `README.md`: English default README.
- `README.zh-CN.md`: complete natural Chinese README.

Both files must use the same structure and make the same product claims. The Chinese version should read naturally, not like a partial literal translation.

Language links:

- In `README.md`: `English | 中文`
- In `README.zh-CN.md`: `中文 | English`

## README Structure Requirement

Every public product README must include:

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

## README First-Screen Gate

The first screen must answer within 10 seconds:

- What is this?
- Who is it for?
- What pain does it solve?
- What is the output?
- Why should I care?
- How can I try it?

If the first screen starts with installation details, file structure, or limitations, fail the gate.

## Star-Pull Copy Rule

Every README must include a `Why this is useful` section. It must explain the differentiated value with concrete product language.

Bad:

- This tool improves productivity.

Good:

- This turns messy invoice exports and pasted invoice text into a prioritized chase queue, client-level aging summary, and tone-specific follow-up drafts.

## GitHub Metadata Requirement

Every public product must generate:

- `github-description.md`
- `github-topics.md`
- `launch-summary.md`
- `README.md`
- `README.zh-CN.md`

`github-description.md` must contain:

- short repo description under 160 characters
- longer one-paragraph description
- 3 alternative descriptions

`github-topics.md` must contain 10-20 relevant GitHub topics. Topics must be domain-specific and product-type specific, not irrelevant trending spam.

## Limitations Rule

Limitations must be honest, concise, and grouped near the end. Do not scatter self-sabotaging caveats through the hero, problem, features, or quickstart.

Do not repeatedly weaken the product with phrases like:

- only a prototype
- not perfect
- just a simple tool
- not production ready
- does not really

If a feature is not implemented, do not claim it. If it is planned, put it under Roadmap.

## README Claim Check

Before launch, `readme-claim-check.md` must verify:

1. Every major claim maps to implemented functionality.
2. Roadmap features are labeled as roadmap.
3. Demo-only features are labeled as demo.
4. Mock features are labeled as mock.
5. Limitations are grouped near the end.
6. No overclaiming.
7. No excessive self-sabotaging caveats.
8. English and Chinese README are consistent.
9. README first screen is strong.
10. Quick Start works.

## Decision

Choose one:

- PASS_GITHUB_LAUNCH_PAGE_GATE
- NEEDS_README_REWRITE
- NEEDS_DEMO_ASSET
- NEEDS_METADATA_FIX
- NEEDS_CLAIM_FIX
- DO_NOT_SHIP
