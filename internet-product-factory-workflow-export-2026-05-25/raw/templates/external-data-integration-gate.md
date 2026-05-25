# External Data Integration Gate

If a product claims security, pricing, vulnerability, market, or risk analysis, it must identify whether it uses authoritative external data.

## Required Questions

- What external data does the product claim to reason about?
- Is an authoritative source integrated?
- Is the data fresh enough?
- Can the user update/import the data?
- If no external data is used, is the README honest about structural/local/heuristic scope?

## Dependency Tool Examples

- npm audit
- OSV
- GitHub Advisory Database
- npm package metadata
- deprecation information
- release dates
- maintainer/package provenance

## Hard Rule

Do not call a structural analyzer a vulnerability scanner unless it uses vulnerability/advisory data.
