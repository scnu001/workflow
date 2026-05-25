# Execution Protocol

## Files Are Memory

Do not rely on chat memory, model memory, or implicit context. Every important finding, score, decision, blocker, assumption, command output, and handoff must be written to Markdown.

Order of truth:

1. `products/_product-index.md`
2. current product folder
3. latest `next-stage-brief.md`
4. latest `checkpoint.md`
5. latest `stage-report.md`
6. relevant substage files
7. `memory/*.md`

## Substage Protocol

Before starting a substage:

1. Read previous substage files in the same stage.
2. Read `checkpoint.md` if it exists.
3. Read `decision-log.md` if it exists.

Before starting a new major stage:

1. Read previous stage `next-stage-brief.md`.
2. Read `stage-report.md` if more detail is needed.
3. Read individual substage files only when needed.

## Evidence-First Rule

Research, demand, scoring, Q-Gate, discovery, audit, and packaging substages must proceed:

```text
Collect evidence -> Evidence Pack -> Source Log -> Analysis -> Decision
```

No evidence, no conclusion.

Evidence Pack table:

```markdown
| ID | Source Type | Source / URL / File Path | Query or Input | Raw Observation | Extracted Signal | Reliability 1-10 | Relevance 1-10 | Used In Conclusion? |
|---|---|---|---|---|---|---:|---:|---|
```

Invalid evidence:

- generic model knowledge
- unsupported assumptions
- invented user complaints
- invented statistics
- imagined competitor weaknesses
- fake quotes
- fake search results
- filler language

If evidence is unavailable, write:

```text
Evidence unavailable. This is a hypothesis, not a finding.
```

## Analysis Structure

Analysis must separate:

- Evidence-Backed Findings
- Reasonable Inferences
- Weak Hypotheses
- Unknowns
- Implications for Product Decision
- Confidence Rating
- Decision

Every major claim must cite evidence IDs. Claims without evidence IDs belong under Weak Hypotheses.

Confidence levels:

- `HIGH`: multiple independent evidence sources, repeated signals, clear user/product implication.
- `MEDIUM`: some direct evidence, some inference required.
- `LOW`: limited evidence, weak source quality, mostly indirect signals.
- `SPECULATIVE`: no reliable evidence; not usable for build decisions.

Hard rule: a candidate cannot pass Q-Gate mainly on `LOW` or `SPECULATIVE` substages.

## Data Analysis Rule

Data-heavy substages must include:

1. Baseline Analysis
2. Robustness Check
3. Sensitivity Check
4. Error / Outlier Check
5. Interpretation
6. Decision Impact

For scoring/ranking, test:

- +20% and -20% key positive factors
- +20% and -20% key negative factors
- higher Depth Penalty
- higher 30-Minute Copy Risk
- lower Expected Star Pull
- lower Demo Pull

If baseline and robustness disagree, choose the conservative classification.

## Substance Audit Rule

File existence is not completion. Before claiming workflow completion, run:

```powershell
python scripts/audit_workflow_substance.py --strict product-XXX
```

If it finds `Status: NOT_STARTED`, heavy `TBD`, shallow tests/fixtures, one-module core risk, or no user-ready artifact, return to the relevant stage.

Product-025 is the benchmark: evidence, authority sources, method, modular architecture, fixture matrix, audit, packaging, and user-ready artifact must form one chain.

