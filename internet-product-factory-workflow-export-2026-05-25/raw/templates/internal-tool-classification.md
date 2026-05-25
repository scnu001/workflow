# Internal Tool Classification

`INTERNAL_FACTORY_TOOL` means:

A tool that improves this product factory but does not deserve a standalone GitHub public repo.

## Default Internal Tool Types
- checklist tools
- simple analyzers
- README optimizers
- config checkers
- `.env` sync tools
- log summarizers
- thin wrappers around prompts
- small one-file CLI utilities
- simple parsers
- basic scoring scripts

## Previous Failed Batch Examples
- LaunchLint
- LaunchSlot Ranker
- Repo About Optimizer
- README FirstScreen
- EnvExample Sync
- CI Fail Digest

These should be kept under `internal-tools/` if useful. They should not be counted as public products.

## Internal Tool Record
- Name:
- Purpose:
- Which workflow stage it supports:
- Input:
- Output:
- Run command:
- Maintenance owner:
- Whether it can be upgraded into a `PUBLIC_PRODUCT`:
- Upgrade path if applicable:

## Upgrade Examples

### Issue Signal Miner
Internal version:
- parses issues and summarizes repeated pain points

Public product version:
- Demand Signal Engine
- local web app
- input GitHub repo / keyword / exported issues
- clustering
- pain map
- opportunity ranking
- exportable report
- README demo

### Agent Cost Forecast
Internal version:
- estimates token/API cost

Public product version:
- AI Workflow Cost Simulator
- visual workflow builder or structured config
- retry/failure simulation
- model comparison
- cost/time/risk dashboard
- exportable report

### PromptShield Lite
Internal version:
- scans prompts for obvious risks

Public product version:
- Prompt Security Scanner
- upload/paste agent instructions
- detect injection, secret exfiltration, unsafe tool access
- risk score
- fix suggestions
- report export
