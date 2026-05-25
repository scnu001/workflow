# User Friction Gate

## Principle
A strong product reduces user work. It does not ask the user to do the hard work first.

## Required Questions
- How many manual steps before first useful output?
- Does the user need to write JSON?
- Does the user need to collect data manually?
- Does the user need to find prices, token counts, failure rates, or benchmark data?
- Would a time-poor user quit before the first useful result?

## Score
- 1: almost no friction.
- 4: some setup, but templates/imports make the first result easy.
- 7: high setup burden that blocks many real users.
- 10: user must manually prepare most of the valuable data.

## Decision Rule
Friction >= 7 blocks `PUBLIC_PRODUCT` unless the product is explicitly for advanced developers and the value is exceptionally high. If value depends on data users are unlikely to prepare manually, require import or automation.

