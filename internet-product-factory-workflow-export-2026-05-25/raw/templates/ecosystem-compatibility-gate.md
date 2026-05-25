# Ecosystem Compatibility Gate

Does the product handle real-world variants, or only the happy path?

## Required Sections

- Supported variants
- Unsupported variants
- Variant test matrix
- Large/complex case behavior
- Downgrade decision if support is narrow

## npm Example

For npm products, check:

- `package-lock` v1/v2/v3
- workspaces
- monorepos
- dev/prod/optional/peer dependencies
- overrides/resolutions
- scoped packages
- nested dependencies
- large lockfiles

## Hard Rule

If only toy samples are supported, block `TOP_10_PUBLISH`.
