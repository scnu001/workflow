# CI Automation Readiness Gate

Developer tools should fit developer workflows.

## Acceptable Automation Paths

- CLI `--ci` mode
- JSON export
- Markdown export
- SARIF export
- GitHub Actions example
- exit-code threshold
- config file
- machine-readable report

## Required Questions

- Can this run in CI?
- Can downstream tools consume the output?
- Can a failing threshold be configured?
- Is local interactive UI optional rather than required?

## Hard Rule

Developer tools without CLI/export/CI path lose launch readiness.
