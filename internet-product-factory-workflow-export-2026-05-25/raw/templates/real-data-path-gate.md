# Real Data Path Gate

## Principle
Sample JSON alone is demo data, not real data support.

## Required For
Any product claiming to analyze workflows, logs, agents, costs, users, issues, reviews, repos, or behavior.

## Acceptable Real Data Paths
- upload JSONL trace
- upload CSV export
- upload log file
- import LangSmith / Langfuse / Helicone / OpenAI / LiteLLM style export
- parse GitHub issues
- parse real README or repo metadata
- parse browser/exported history
- connect to an API
- run local instrumentation
- SDK, proxy, plugin, or GitHub Action

## Decision Rule
If no real data path exists, classify as `EXPERIMENT` or `NEEDS_V2_BEFORE_LAUNCH`. If the core promise depends on real data, fake/sample-only input cannot pass Q-Gate.

