---
name: run-plan
description: >-
  Execute a plan-rules .plan.md by launching one Composer 2.5 subagent per
  domain in parallel. Use when the user says run the plan, execute the plan,
  implement the plan in parallel, or /run-plan.
---

Execute the current plan with **one Composer 2.5 subagent per domain, all started in the same turn**. Do not implement domains yourself. Do not wait for one domain before starting another. Do not change the plan's decided path.

## 1. Load the plan

Use, in order: the file the user named or attached → the plan this chat is working on → the newest `*.plan.md` in the workspace (ask if several).

Read the whole file. You need Goal, Out of Scope, study-case **After changes**, `# Parallel Domains`, every `## Domain:` (including Data schema and API contract), YAML `todos`, and `## Behaviour` when present.

If the user named a domain, run only that one. Otherwise run every todo that is not `completed`.

## 2. Split into parallel domains

Each `## Domain: [name]` is one agent. Treat `## Stage:` the same if an older plan still uses it. Ignore `Depends on` / `after [domain]` (or `after [stage]`) if an older plan still has them.

**Collision check:** collect Inventory paths (new + modified) per domain. If two pending domains share a path, merge those domains into **one** agent. Keep the rest parallel.

If a domain has no `### Provides` / `### Consumes`, still launch; do not invent a contract from Inventory.

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

Fill the template. Do not point the subagent at the plan file and expect it to pick a domain.

```text
Workspace: {{absolute workspace path}}
Plan file: {{absolute plan path}}

## This domain
{{include context: this domain's full ## Domain: section}}

## You Consume (bind now — do not wait)
{{for each call under this domain's ### Consumes, include THAT call from the providing domain's ### Provides:}}

**`[consumed-domain]` `[call]`**
- Request: …
- Success: …
- Errors: …

{{if Consumes is none: none}}

## Shared plan facts
Goal: {{include context: Goal}}
Out of Scope: {{include context: Out of Scope}}
Study cases this domain must satisfy (After changes only): {{include context: relevant cases}}
Behaviour: {{include context: ## Behaviour when present, else omit this line}}

## Rules
- Edit ONLY this domain's Inventory paths (new + modified). Do not touch other domains' files.
- Bind to **You Consume** as written even if those domains' files are not in the tree yet.
- Follow the plan's decided path. Do not ask questions, add options, or expand Out of Scope.
- If Inventory includes UI (components, pages, CSS), follow ui-craft and ux-craft.
- Follow workspace principles (readable, low abstraction, guard clauses).
- Do not run the plan's `# Validation` or a test suite.

## Return
- Outcome met: yes/no
- Provides implemented: yes/no/none
- Consumes bound: [domain.call names] or none
- Files created and modified
- Anything blocked
```

## 5. When all domain agents have finished

Do not poll. When completion notifications have arrived for every launched agent:

1. Read what each returned, then **review the implementation** — open the files they changed. Do not run `# Validation`, domain Verify commands, or a test suite.
2. For each domain, check the code against that domain's `### Provides`, `### Consumes`, `### Outcome`, and `### Tasks`, plus relevant study-case **After changes**. Note misses, extra work in Out of Scope, and Inventory path collisions.
3. Mark matching YAML todos `completed` or `error`.
4. Report a review per domain: what landed, what matches the plan, what does not. Link `[Name](id)` again.

If a domain missed its Provides or failed to bind Consumes, say so. Do not silently re-run every domain. Re-launch only the failed domain (same Task args) when the miss is clear, or ask if the failure is ambiguous.

If review finds **plan ambiguity** (vague Tasks, missing Consumes, study cases without Tasks) rather than implementation bugs, run `grill-me` in **post-plan** mode on those gaps, patch `.plan.md`, then re-launch affected domains only.
