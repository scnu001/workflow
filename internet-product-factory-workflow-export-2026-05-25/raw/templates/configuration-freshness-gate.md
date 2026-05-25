# Configuration Freshness Gate

## Principle
Products that depend on changing external data must not hide stale hardcoded assumptions.

## Applies To
- model prices
- API limits
- exchange rates
- benchmark data
- public datasets
- laws, compliance rules, or external standards
- model lists and provider capabilities

## Required Support
At least one:
- user-editable config file
- importable pricing/config table
- external source update mechanism
- clearly documented update path
- versioned default config
- fallback custom override

## Decision Rule
Hardcoded model price tables are not enough. If prices, limits, or external rules can change and users cannot update them, downgrade launch readiness.

