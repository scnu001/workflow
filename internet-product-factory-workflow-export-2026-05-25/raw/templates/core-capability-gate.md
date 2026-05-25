# Core Capability Gate

## Principle
A frontend does not equal product depth.

Every product must define the one capability that makes it non-trivial. If that capability is not implemented, the product cannot be `PUBLIC_PRODUCT` or `TOP_10_PUBLISH`.

## Required Questions
- What is the one core capability?
- What real user work does the product remove?
- What data does the product need?
- What does the product automate, parse, import, estimate, detect, cluster, simulate, or validate?
- What would make this product shallow?

## Bad Core Capabilities
- calculate cost from manually entered values
- summarize text
- show a dashboard
- classify input with one prompt
- format a report from user-provided work

## Good Core Capabilities
- import real traces and calculate agent workflow cost
- parse logs into structured workflow steps
- detect risks from real prompt/tool instructions
- cluster real user complaints into opportunities
- simulate alternative model routing strategies from real usage data
- generate actionable optimization reports from real evidence

## Decision Rule
If the core capability is missing or only implied by the README, classify as `EXPERIMENT`, `PARK`, `BUILD_INTERNAL`, or `NEEDS_V2_BEFORE_LAUNCH`.

