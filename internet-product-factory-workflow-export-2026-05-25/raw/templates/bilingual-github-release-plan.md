# Bilingual GitHub Release Plan

- Stage: Packaging / Marketing / Launch
- Status: NOT_STARTED

## 1. Release Strategy

- English default branch:
- Chinese branch name:
- Product code localization needed? Default: No.
- GitHub repo metadata language: Default English because description/topics are repo-level.

## 2. English Public Asset

- README source:
- GitHub description:
- GitHub topics:
- Demo instructions:
- Launch posts:
- README claim check completed:

## 3. Chinese Branch Asset

- Chinese README source:
- Chinese description copy:
- Chinese launch posts:
- Files allowed to differ from English branch:
  - README.md or README.zh-CN.md
  - launch copy
  - GitHub-facing explanatory markdown
- Files that must remain unchanged:
  - app/source code
  - tests
  - sample data schemas
  - environment variable names
  - API routes
  - commands

## 4. Branch Procedure

1. Prepare English main branch.
2. Commit product code and English packaging.
3. Create `zh-CN` branch from the same commit.
4. Replace or add Chinese GitHub-facing docs only.
5. Verify product behavior remains unchanged.
6. Push both branches after explicit approval.

## 5. Claim Mapping

| Claim | English README Evidence | Chinese README Evidence | Implemented? | Risk |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD |

## 6. Secret And Safety Check

- `.env` ignored:
- `.env.example` uses placeholders:
- No API key in README:
- No API key in logs/examples:
- No secret in git diff:
- Frontend does not expose secrets:

## 7. Decision

Choose one:
- READY_TO_PUSH_WITH_APPROVAL
- NEEDS_COPY_REVIEW
- NEEDS_SECRET_FIX
- DO_NOT_PUSH
