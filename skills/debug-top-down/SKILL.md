---
name: debug-top-down
description: >-
  Top-down debugging mindset — start from the observable symptom, bisect
  layers, form falsifiable hypotheses, and follow one concrete path with
  evidence. Use when the user reports a bug, error, crash, wrong behavior,
  regression, test failure, or asks how to debug or find root cause. Teaches
  how to think while debugging; operational steps (instrument, repro, verify)
  come from Cursor Debug mode when active.
---

# Debug Top-Down

**How to think while debugging** — not a step-by-step runbook. When Cursor Debug mode is active, follow its workflow for instrumentation, reproduction, and verification. This skill supplies the reasoning frame.

## When to Use / When Not

**Use when** something is broken and you need to reason about *where* and *why*:
- errors, crashes, failed tests, wrong output, missing data, stale UI
- "why doesn't this work?", "find the bug", "root cause", "regression"

**Do not use** for:
- greenfield feature work → normal implementation flow
- deep architecture understanding with no symptom → `deep-agent`
- quick one-bug skim from chat context → `/search-related-problem`

If the symptom is unclear, ask one short question before tracing.

## Core idea

**Top-down** = start at what the user sees, work downward until one layer fails, then drill one path inside that layer.

**Bottom-up** (avoid as default) = start in models/repos and hope the symptom appears. Slow, noisy, easy to fix the wrong thing.

Read code only to confirm or disprove the current hypothesis at the current layer. Stop reading when a layer is ruled out.

## Anchor on the symptom

Before opening files, state one sentence:

> **What breaks, when, and what was expected instead.**

Treat these as clues, not the answer:
- error text, stack trace, HTTP status/body
- trigger (click, cron, deploy, input)
- always / after change / intermittent

No observable symptom → say what evidence is missing. Do not guess a fix.

## Layer map (mental model)

From the symptom, sketch layers **downward** — only as far as needed:

```text
User action / trigger
  → UI / client (render, state, cache)
  → API / handler (route, controller, validation)
  → service / domain logic
  → persistence / external integration
  → config / env / infra
```

Skip layers that cannot produce this symptom. The map answers **where to look first**, not full architecture.

## Bisect layers

At each layer ask: **"Could this layer alone explain the symptom?"**

Work top to bottom. Stop at the **first layer with concrete failure evidence**.

| Layer | Fast checks |
|-------|-------------|
| UI / client | wrong state, stale cache, bad request payload, console/network errors |
| API / handler | status code, response body, validation error, auth |
| Service | wrong branch, bad transform, missing guard |
| Data / integration | wrong/missing row, constraint, stale read, wrong key |
| Config / env | missing var, wrong URL, feature flag, credentials |

Do not patch a lower layer before the failing layer is confirmed. Do not read unrelated folders.

## Drill one concrete path

Inside the failing layer, follow **one real execution path**:

```text
entry (route / handler / click / job)
  → validation / input
  → transform / business rule
  → downstream call or write
  → result back to symptom
```

Follow calls and data — folder names lie.

**Pause where data changes shape:** null ↔ object, id ↔ slug, list ↔ item, string ↔ number, user ↔ session. Most bugs live at these seams.

## Think in hypotheses

Debug by **disproving**, not by reading everything.

For each suspect:
1. **Hypothesis** — one falsifiable sentence
2. **Predict** — what must be true in code/logs/data if correct
3. **Check** — smallest proof that confirms or kills it
4. **Verdict** — confirmed / ruled out → next suspect or root cause

One hypothesis at a time. Name the bug class early:

`logic` | `state` | `data` | `integration` | `env/config` | `concurrency`

When Cursor Debug mode is active, each hypothesis should map to instrumentation or a runtime check — never fix from code alone without evidence.

## State root cause clearly

When confirmed:

> **Because** [condition], [code/path] does [wrong thing], so the user sees [symptom].

The error message is a clue, not the root cause. "Because … so …" forces the full chain.

## Fix discipline

- Change the **smallest** code that addresses the confirmed root cause
- Do not refactor unrelated code during debug
- Do not accumulate speculative guards from rejected hypotheses — revert them
- Add or adjust a test only when it locks the repro or guards regression

Verification (re-run repro, before/after logs) is handled by Debug mode when active.

## Anti-patterns

- **Bottom-up first** — models/repos before the symptom path
- **Shotgun fixes** — changing several things without a confirmed layer
- **Edge-case hunting** — rare races when a common path explains the symptom
- **Reading everything** — full-folder skims without a hypothesis
- **Fixing downstream** — patching UI when the API returns wrong data
- **Stopping at the error message** — symptom ≠ cause
- **Code-only certainty** — static analysis without runtime proof

## Relationship to other tools

| Tool | Role |
|------|------|
| **Cursor Debug mode** | Operational loop: hypotheses → instrument → repro → log proof → fix → verify |
