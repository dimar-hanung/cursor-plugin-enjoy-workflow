---
name: behaviour-research
description: Verify exact versions of tech the current work touches, then search only version-specific pitfalls — report facts with sources. Not plan-specific; use plan-behaviour-research to insert into a plan.
---

Verify how the **installed** versions actually behave. Training data often disagrees with the workspace — check versions first, then search only what usually goes wrong for the work in scope.

Applies to any tech the current task touches, not just frameworks and databases: libraries/packages, ORMs, runtimes, DB engines, external APIs/SDKs, infra tools (Docker, nginx, message queues), browser APIs, CLI tools.

**Scope:** conversation context, the open task, or tech the user names. Not limited to plans. To add a `## Behaviour` section to a `.plan.md`, use `/plan-behaviour-research` instead.

## 1. Detect what is in play and the exact version

- Read lockfiles and manifests, never guess: `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock`, `composer.lock`, `go.mod`, `requirements.txt` / `poetry.lock` / `uv.lock`, `Gemfile.lock`, `*.csproj`, `.tool-versions`, `Dockerfile`.
- Runtime, DB engine, and infra versions: check `docker-compose.yml`, infra/IaC config, CI config, or connection config.
- External APIs/SDKs: find the pinned API version in client config, headers, or SDK version (e.g. Stripe API date, S3 SDK major).
- If a version is not written anywhere in the workspace, ask the user — do not assume.
- Scope to tech the current work actually touches. Skip everything else.

## 2. Search only what usually goes wrong

For each `tech + exact version` pair, web-search pitfalls that intersect what is being built, fixed, or changed:

- Query shape: `{{tech}} {{major.minor}} {{feature being touched}} breaking change | gotcha | pitfall | known issue`
- Prioritize:
  - Breaking changes between the installed version and the version you "remember".
  - Surprising defaults — transactions, isolation level, lazy loading, caching, connection pooling, timezone/encoding, cascade behaviour, retry/timeout defaults, rate limits, pagination limits.
  - Behaviour that silently differs from the docs (open GitHub issues, migration guides, release notes, API changelogs).
- Skip general tutorials, marketing pages, and anything that does not touch the current work.

## 3. Report findings in chat

```markdown
## Behaviour

### {{tech}} {{exact version}}
- {{behaviour fact}} — affects {{current task / code path}} ({{source link}})
```

Rules:

- Every fact names the exact installed version and links a source. No facts from memory alone.
- Include only facts that change how the current work should be done. This is a filter, not a dump.
- If research finds nothing surprising, write one line: `Verified <tech versions>; no version-specific behaviour affects this work.`
- Facts only — no options, questions, or "consider".
