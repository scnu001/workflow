# Core Mechanism Requirement

Every PUBLIC_PRODUCT must have at least one non-trivial mechanism.

## Valid Mechanisms

- AST parser
- schema diff engine
- dependency graph
- permission graph
- attack path analysis
- timeline reconstruction
- flaky failure probability
- auto-fix patch generation
- benchmark suite
- sensitivity analysis
- trace/log import
- model routing simulation
- confidence scoring
- risk propagation model
- interactive scenario simulator
- SDK/proxy/plugin/GitHub Action
- multi-file project analysis
- configurable rule engine with real rules
- regression tests over multiple fixtures

## Invalid As Sole Mechanism

- keyword search
- simple regex matching
- static checklist
- one prompt
- one formula
- manually entered JSON calculator
- generic Markdown report generator
- sample-only demo

## Hard Rule

If no non-trivial mechanism exists, classify as EXPERIMENT, BUILD_INTERNAL, or NEEDS_V2_BEFORE_LAUNCH.

## Required Output

- mechanism name
- implemented files
- data structures
- algorithms/parsers/rules
- fixtures and tests
- what would make the product toy-level
- decision
