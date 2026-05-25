# README Claim Check

## Purpose
Packaging must not overclaim.

## GitHub Launch Page Gate

Verify:

- English README exists.
- Chinese README exists.
- Strong first screen explains what, who, pain, output, why care, and how to try.
- Repo description is clear and under 160 characters.
- GitHub topics are specific and relevant.
- Screenshot/GIF plan or demo-output visual exists.
- Demo instructions are runnable.
- Sample input/output is included.
- Limitations are grouped near the end.
- README claim check is complete before launch.

## Claim Mapping
| README Claim | Implemented? | Evidence File / Command | Demo Only? | Roadmap? | Revision Needed |
| --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD |

## Rules
- Every major README claim must map to implemented functionality.
- Future roadmap must be labeled as roadmap.
- Demo-only features must be labeled as demo.
- Mock advisor must be labeled as mock if no real API is used.
- Do not call the product observability, budget guard, trace analyzer, importer, or automatic monitor unless those features exist.
- Do not call a structural analyzer a vulnerability scanner unless vulnerability/advisory data is integrated.
- Limitations must be honest but grouped near the end.
- Do not scatter self-sabotaging caveats through the hero, problem, key features, or quickstart.
- English and Chinese README files must contain the same structure and the same product claims.
- The Chinese README must read naturally, not like a partial literal translation.
- Quick Start must be verified against actual commands.

## README Structure Requirement

Both README files must include:

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

## First-Screen Gate

The first screen must answer within 10 seconds:

- What is this?
- Who is it for?
- What pain does it solve?
- What output does it create?
- Why should a visitor care?
- How can it be tried quickly?

If installation, file structure, or limitations come before value, fail the gate.

## Decision

Choose one:

- PASS_README_CLAIM_CHECK
- NEEDS_CLAIM_FIX
- NEEDS_BILINGUAL_REWRITE
- NEEDS_DEMO_ASSET
- DO_NOT_SHIP
