# Audit Report Template

## Summary
- Product:
- Classification:
- Audit decision: Ship / Fix then ship / Do not ship / Downgrade internal

## Persona Scores
| Persona | Usefulness | Clarity | Trust | Ease of use | Differentiation | Build quality | Launch readiness | Demo pull | Expected star pull | 30-minute copy risk | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Product Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Engineering Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Security Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Growth Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Skeptical Student User | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Middle-Aged Nontechnical User | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Time-Poor Professional | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GitHub Visitor | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Implementation Depth Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Real-World Depth Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GitHub README Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Business Workflow Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Method-Problem Fit Reviewer | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Hard Audit Rules
- If GitHub Visitor would not understand the product from the README first screen, do not ship.
- If GitHub Visitor would not plausibly star it, do not ship.
- If 30-minute copy risk is high, downgrade to `INTERNAL_FACTORY_TOOL`.
- If the product has no visible demo moment, return to Product Discovery.
- If secret handling is unsafe, stop launch.
- If Implementation Depth Reviewer returns `NEEDS_V2_BEFORE_LAUNCH`, do not ship.
- If the frontend is mostly a copied shell and the core is mostly shallow keyword/regex rules, do not ship as `TOP_10_PUBLISH`.
- If GitHub README Reviewer fails the first screen, bilingual copy, claim honesty, demo evidence, or star-pull clarity, do not ship.
- If Business Workflow Reviewer says the product is only a spreadsheet with a web UI, do not ship.
- If a non-developer operational product lacks constraints, data sufficiency checks, realistic messy fixtures, or actionable next steps, do not ship as `TOP_10_PUBLISH`.
- If Method-Problem Fit Reviewer fails the product, do not ship.
- If the method is fake complexity or the product is simple scoring with fancy wording, do not ship as `TOP_10_PUBLISH`.
- If assumptions drive recommendations but are not challenged, downgrade launch readiness.

## Implementation Depth Review
- Core logic depth:
- Mostly regex/keyword matching?
- Copied shell risk:
- Test depth:
- Fixture depth:
- Output is actionable?
- Deserves public launch?
- Decision:

## Real-World Depth Review
- Ecosystem compatibility:
- External data integration:
- Remediation depth:
- Real corpus benchmark:
- CI / automation readiness:
- UI domain specificity:
- README claim honesty:
- Decision:

## GitHub README Review
- Understandable in 10 seconds?
- Would keep reading?
- Would star?
- First screen strong?
- Too technical too early?
- Limitations scattered?
- Claims honest?
- Screenshot/GIF plan present?
- Chinese README natural?
- English README professional?
- Decision:

## Business Workflow Review
- Spreadsheet-with-web-UI risk:
- Real business operations represented:
- Constraints modeled:
- Input/source-system realism:
- Missing-field/data quality handling:
- Operational actionability:
- What-if or sensitivity depth:
- Realistic messy fixture depth:
- More useful than Excel?
- Decision:

## Method-Problem Fit Review
- Natural discipline / method family:
- Method naturally fits the problem?
- Method depth:
- Fake complexity / method theater risk:
- Simple scoring with fancy wording?
- Assumptions challenged?
- Uncertainty handled?
- Would a domain-aware user respect this analysis?
- Decision:

## Top Strengths
- TBD

## Top Weaknesses
- TBD

## Must-Fix Issues
- TBD

## Nice-To-Have Issues
- TBD

## Ship Decision
Ship / Fix then ship / Do not ship / Downgrade internal
