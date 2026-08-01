---
name: plan-behaviour-research
description: Verify the exact versions of tech the plan touches, search only version-specific pitfalls, and add a Behaviour section to the current plan.
---

Add a `## Behaviour` section to the current plan. Training data often disagrees with how the **installed** version actually behaves — verify versions from the workspace first, then search only for what usually goes wrong.

Applies to any tech the plan touches, not just frameworks and databases: libraries/packages, ORMs, runtimes, DB engines, external APIs/SDKs, infra tools (Docker, nginx, message queues), browser APIs, CLI tools.

## 1. Detect what is implemented and the exact version

- Read lockfiles and manifests, never guess: `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock`, `composer.lock`, `go.mod`, `requirements.txt` / `poetry.lock` / `uv.lock`, `Gemfile.lock`, `*.csproj`, `.tool-versions`, `Dockerfile`.
- Runtime, DB engine, and infra versions: check `docker-compose.yml`, infra/IaC config, CI config, or connection config.
- External APIs/SDKs: find the pinned API version in client config, headers, or SDK version (e.g. Stripe API date, S3 SDK major).
- If a version is not written anywhere in the workspace, ask the user — do not assume.
- Scope to tech the plan actually touches. Skip everything else.

## 2. Search only what usually goes wrong

For each `tech + exact version` pair, web-search pitfalls that intersect the plan's Must do items:

- Query shape: `<tech> <major.minor> <feature being touched> breaking change | gotcha | pitfall | known issue`
- Prioritize:
  - Breaking changes between the installed version and the version you "remember".
  - Surprising defaults — transactions, isolation level, lazy loading, caching, connection pooling, timezone/encoding, cascade behaviour, retry/timeout defaults, rate limits, pagination limits.
  - Behaviour that silently differs from the docs (open GitHub issues, migration guides, release notes, API changelogs).
- Skip general tutorials, marketing pages, and anything that does not touch what the plan changes.

## 3. Write the section into the plan

Insert after `## What Current (Technical)` and before `## What Changes (Technical)` — this section extends the plan-rules body order when this command is used.

```markdown
## Behaviour

### <tech> <exact version>
- [behaviour fact] — affects [stage or Must do item] ([source link])
```

Rules:

- Every fact names the exact installed version and links a source. No facts from memory alone.
- Include only facts that change how a Must do item is executed. This is a filter, not a dump.
- If research finds nothing surprising, write one line: `Verified <tech versions>; no version-specific behaviour affects this plan.`
- Plan tone still applies — facts only, no options, questions, or "consider".
