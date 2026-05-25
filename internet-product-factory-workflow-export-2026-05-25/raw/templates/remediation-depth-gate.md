# Remediation Depth Gate

Findings must help the user act.

## Required For Each Finding

- affected path
- exact file / field / node / route / dependency if possible
- severity
- confidence
- why it matters
- suggested direct dependency upgrade or owner action
- override/resolution option if relevant
- next command/action
- false-positive note

## Hard Rules

- Generic advice is not enough.
- Products without remediation guidance cannot be `TOP_10_PUBLISH`.
- Reports should distinguish root cause, symptom, affected path, and next action.
