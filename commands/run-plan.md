---
name: run-plan
description: >-
  Execute a plan-rules .plan.md by launching one Composer 2.5 subagent per
  domain in parallel. Use when the user says run the plan, execute the plan,
  implement the plan in parallel, or /run-plan.
---

Execute the current plan with **one Composer 2.5 subagent per domain, all started in the same turn**. Do not implement domains yourself. Do not wait for one domain before starting another.

## 1. Load the plan

Use, in order: the file the user named or attached → the plan this chat is working on → the newest `*.plan.md` in the workspace (ask if several).

Read the whole file. You need Goal, Out of Scope, study-case **After changes**, `# Parallel Domains`, every `## Stage:`, and YAML `todos`.

If the user named a domain, run only that one. Otherwise run every todo that is not `completed`.

## 2. Split into parallel domains

Each `## Stage: [domain]` is one agent. Ignore `Depends on` / `after [stage]` if an older plan still has them — bind to **Contract**, never to stage order.

**Collision check:** collect Inventory paths (new + modified) per domain. If two pending domains share a path, merge those domains into **one** agent. Keep the rest parallel.

If a stage has no Contract, derive Request / Success / Errors from Must do (`Return`, `Expose`, `Wire`) and Inventory **API endpoints**. Still launch; do not block on format.

## 3. Launch — one message, every domain

In a **single** response, call `Task` once per domain (or merged collision set). Required on every call:

| Arg | Value |
| --- | --- |
| `subagent_type` | `generalPurpose` |
| `model` | `composer-2.5` |
| `run_in_background` | `true` |
| `description` | 3–5 words, domain name (e.g. `Implement orders-api`) |
| `prompt` | The template below, with plan context included |

Do not use any other model. Do not launch one agent for the whole plan. Do not start a second batch in this turn. Do not poll, `AwaitShell`, or wait on a domain before launching the others.

After launch, tell the user which domains started (say **Composer 2.5**, not the slug) and that they run in parallel. Link each agent as `[Name](id)`. Stop. Wait for completion notifications.

## 4. Prompt template (include context; the subagent has no chat history)

Include these context blocks in every `prompt`. Do not point the subagent at the plan file and expect it to pick a domain.

- This domain's full `## Stage:` section (Contract, Outcome, Must do, Inventory)
- Contract blocks of every domain listed under Consumes (`none` if omitted)
- Goal, Out of Scope, and study-case After changes this domain must satisfy
- Absolute workspace path and plan file path

```text
Workspace: {absolute workspace path}
Plan file: {absolute plan path}

## This domain
{include context: this domain's ## Stage: section — Contract, Outcome, Must do, Inventory}

## Contracts you bind to
{include context: Contract blocks of every domain listed under Consumes}
{if Consumes is omitted: none}

## Shared plan facts
Goal: {include context: Goal}
Out of Scope: {include context: Out of Scope}
Study cases this domain must satisfy (After changes only): {include context: relevant cases}

## Rules
- Implement this domain's Must do until Outcome is true.
- Edit ONLY this domain's Inventory paths (new + modified). Do not touch other domains' files.
- Bind to Consumes Contracts as written. Use the request/success/errors shape even if the other domain's code is not in the tree yet.
- Follow the plan's decided path. Do not ask questions, add options, or expand Out of Scope.
- If Inventory includes UI (components, pages, CSS), follow ui-craft and ux-craft.
- Follow workspace principles (readable, low abstraction, guard clauses).
- Do not run the plan's `# Validation` or a test suite.

## Return
- Outcome met: yes/no
- Files created and modified
- Anything blocked
```

## 5. When all domain agents have finished

Do not poll. When completion notifications have arrived for every launched agent:

1. Read what each returned, then **review the implementation** — open the files they changed. Do not run `# Validation`, domain Verify commands, or a test suite.
2. For each domain, check the code against that stage's **Contract**, **Outcome**, and **Must do**, plus relevant study-case **After changes**. Note misses, extra work in Out of Scope, and Inventory path collisions.
3. Mark matching YAML todos `completed` or `error`.
4. Report a review per domain: what landed, what matches the plan, what does not. Link `[Name](id)` again.

If a domain missed its Contract, say so. Do not silently re-run every domain. Re-launch only the failed domain (same Task args) when the miss is clear, or ask if the failure is ambiguous.

## Do not

- Implement domain Must do in this parent agent
- Sequence domains (backend first, “after schema”, wait-then-UI)
- Put two Task launches in different turns when they can start together
- Change the plan’s decided path while executing
- Run `# Validation`, Verify commands, or a test suite — review the implementation instead
