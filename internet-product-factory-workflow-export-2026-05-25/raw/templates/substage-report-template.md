# Substage: [Name]

- Stage:
- Substage file:
- Substage type: context / research / data_analysis / build / audit / packaging / reflection
- Status: NOT_STARTED / BLOCKED / COMPLETE / LEGACY_RECLASSIFIED
- Timestamp:

## 1. Objective

Explain the specific question this substage answers.

## 2. Why This Matters

Explain why this substage matters for the product decision.

## 3. Method

Explain what sources, files, data, signals, commands, or reasoning were used.

If web access is unavailable, write `WEB_ACCESS_UNAVAILABLE` in Source Log.

## 4. Evidence Pack

No evidence, no conclusion.

If evidence is unavailable, write:

`Evidence unavailable. This is a hypothesis, not a finding.`

| ID | Source Type | Source / URL / File Path | Query or Input | Raw Observation | Extracted Signal | Reliability 1-10 | Relevance 1-10 | Used In Conclusion? |
|---|---|---|---|---|---|---:|---:|---|
| E1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | No |

Valid source types include web search result, opened webpage, GitHub issue, GitHub repo, Reddit thread, Hacker News thread, Product Hunt page, app review, Chrome extension review, competitor pricing page, documentation page, local file, user-provided file, dataset, API response, benchmark result, terminal output, smoke test result, and manual product inspection.

Invalid evidence includes generic model knowledge, unsupported assumptions, invented user complaints, invented statistics, imagined competitor weaknesses, vague trend claims, fake quotes, fake search results, and filler language.

## 5. Source Log

### Queries Attempted

- TBD

### Sources Opened

- TBD

### Sources Rejected

- TBD

### Access Failures

- TBD

### Evidence Gaps

- TBD

### Claims That Must Remain Hypotheses

- TBD

## 6. Analysis

Every major claim must reference evidence IDs from the Evidence Pack. Unsupported claims belong under Weak Hypotheses.

### Evidence-Backed Findings

- TBD

### Reasonable Inferences

- TBD

### Weak Hypotheses

- TBD

### Unknowns

- TBD

### Implications for Product Decision

- TBD

### Data Analysis Checks

Use this section for data-heavy substages. If not applicable, say why.

#### Baseline Analysis

- Data source:
- Sample size:
- Variables used:
- Assumptions:
- Formula or scoring method:
- Baseline result:
- Interpretation:

#### Robustness Check

- Alternative or conservative check:
- Did the conclusion survive assumption changes:

#### Sensitivity Check

- +20% / -20% key positive factors:
- +20% / -20% key negative factors:
- Higher Depth Penalty:
- Higher 30-Minute Copy Risk:
- Lower Expected Star Pull:
- Lower Demo Pull:

#### Error / Outlier Check

- Duplicate sources:
- Duplicated signals:
- Low-quality sources:
- Outlier scores:
- Over-weighted single source:
- Unsupported high scores:
- Missing evidence IDs:
- Missing confidence rating:

#### Decision Impact

- TBD

## 7. Scores

Use 1-10 scores where applicable.

| Dimension | Score 1-10 | Evidence IDs | Notes |
| --- | ---: | --- | --- |
| Signal Strength | TBD | TBD | TBD |
| User Pain | TBD | TBD | TBD |
| Urgency | TBD | TBD | TBD |
| Specificity | TBD | TBD | TBD |
| Demo Potential | TBD | TBD | TBD |
| Distribution Potential | TBD | TBD | TBD |
| Monetization Potential | TBD | TBD | TBD |
| Build Feasibility | TBD | TBD | TBD |
| Differentiation | TBD | TBD | TBD |
| Copy Risk | TBD | TBD | TBD |
| Trust / Compliance Risk | TBD | TBD | TBD |
| Disciplinary Method Fit | TBD | TBD | Natural method fit; < 6 blocks TOP_10_PUBLISH. |
| Method Depth | TBD | TBD | Analytical products with < 6 cannot be TOP_10_PUBLISH. |
| Uncertainty Handling | TBD | TBD | Required when uncertainty affects decisions. |
| Assumption Challenge | TBD | TBD | Required when assumptions drive recommendations. |
| Multi-Perspective Reasoning | TBD | TBD | Required for complex judgment/tradeoff products. |
| Method Theater Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |
| Shallow Scoring Risk | TBD | TBD | > 6 blocks TOP_10_PUBLISH. |

## 8. Risks / Weak Points

List what may be misleading, weak, unverified, overestimated, or risky.

## 9. Output to Next Substage

Write the exact useful inputs that the next substage should carry forward.

## 10. Confidence Rating

Choose one:
- HIGH
- MEDIUM
- LOW
- SPECULATIVE

Rules:
- HIGH requires multiple independent evidence sources, specific repeated signals, and clear product implication.
- MEDIUM allows direct evidence with some inference.
- LOW means limited or indirect evidence.
- SPECULATIVE means no reliable evidence and must not drive build decisions.

## 11. Decision

Choose one:
- CONTINUE
- NEED_MORE_EVIDENCE
- WEAK_SIGNAL
- PARK
- PIVOT
- KILL

## 12. Minimum Quality Check

Confirm when marking COMPLETE:
- At least 500 meaningful words
- No generic filler
- Evidence Pack completed before Analysis
- Source Log completed
- Analysis references evidence IDs
- Confidence rating included
- Scores included where applicable
- Risks included
- Next-step output included
- Data-heavy substages include baseline, robustness, sensitivity, and error/outlier checks
