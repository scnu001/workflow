# Demand Bias Check

Use this template at the end of Stage 1 Demand Discovery and reference it again during Stage 2 Launch Slot Scoring.

## Principle

Do not preselect the audience.

Do not default to developer tools.

Do not force non-developer products.

Start from broad market demand discovery, then select the strongest opportunity based on evidence quality, pain intensity, feasibility, distribution, demo potential, and product depth.

Developer tools are allowed if they truly win the evidence comparison. If the final shortlist is dominated by developer tools, the workflow must explain why the evidence for developer tools is stronger than other categories.

## Required Demand Pools

Inspect multiple pools before product ideas are selected:

| Demand Pool | Sources Checked | Pain Signals | Candidate Opportunities | Evidence Quality | Feasibility | Distribution Path | Likely Product Format |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| Developer / AI builder / technical workflow users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Students / international students / applicants | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Job seekers / career planners | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Creators / content workers / solo operators | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Small business / freelancers | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Personal finance / budgeting / decision-making users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Life admin / family admin / healthcare admin users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Productivity / AI tool users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Education / tutoring / learning users | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Emerging niche discovered during search | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

For each pool, collect at least 5 pain signals, 3 source references, and 3 candidate opportunities if available. If evidence is unavailable, record the gap instead of inventing signals.

## Bias Questions

1. Did we over-sample developer sources?
2. Did we over-weight GitHub/Hacker News because they are easy for Codex?
3. Did we ignore non-developer pain because it is harder to implement?
4. Did we choose a product mainly because it is easy to build?
5. Did we confuse GitHub publishability with actual demand?
6. Did we force a non-developer idea without enough evidence?
7. Did the winning opportunity truly have the strongest evidence?

## Bias Flags

- `DEV_SOURCE_BIAS`: more than 60% of sources are developer sources.
- `DEV_CANDIDATE_OVERCONCENTRATION`: more than 70% of candidates are developer tools.
- `GITHUB_BIAS_RISK`: candidate wins mainly because it fits GitHub packaging.
- `BUILDABILITY_BIAS_RISK`: candidate wins mainly because it is easy for Codex to build.
- `FORCED_NON_DEV_RISK`: non-developer candidate is selected despite weaker evidence.
- `CATEGORY_OVERCONCENTRATION_RISK`: shortlist is dominated by one audience without evidence justification.

## Demand Bias Gates

- Broad Demand Discovery:
- Demand Bias Check:
- Developer Tool Bias Check:
- Cross-Audience Comparison:
- Category-Neutral Product Selection:

## Cross-Audience Comparison

If the final winner is a developer tool, compare it against the top non-developer candidate.

If the final winner is a non-developer tool, compare it against the top developer candidate.

| Candidate | Audience / Pool | Evidence Strength | Pain Intensity | Feasibility | Distribution | Demo Potential | Product Depth | Bias Risk | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Winner | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Top developer alternative | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Top non-developer alternative | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Selection Justification

- Why this audience/problem won:
- What evidence supports it:
- What competing opportunities were rejected:
- Why developer-tool bias or non-developer bias did not decide the outcome:
- Why this is not merely the easiest thing for Codex to build:
- Why this deserves to proceed to Product Discovery:

## Decision

Choose one:

- `PASS_BIAS_CHECK`
- `DEV_SOURCE_BIAS_NEEDS_JUSTIFICATION`
- `CATEGORY_OVERCONCENTRATION_NEEDS_RESEARCH`
- `NEED_MORE_EVIDENCE`
- `PARK`
- `KILL`
