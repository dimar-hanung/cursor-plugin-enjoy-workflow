# Plan handoff

Use when the decision record is complete and the user confirms shared understanding.

## Pre-plan handoff

Grill finished **before** a `.plan.md` exists.

| Situation | Next step |
| --- | --- |
| Decisions touch library/framework behaviour that may change Tasks | `/plan-behaviour-research`, then `plan-rules` |
| Decisions are stable; ready for parallel domains | `plan-rules` → write `.plan.md` |
| High-fidelity UI was deferred | Build a quick prototype or mock, resume `grill-me` on that artifact, then plan |
| User only wanted design clarity, no plan yet | Stop — decision record is the deliverable |

### Mapping decisions → new plan (`plan-rules`)

| Grill output | plan-rules section |
| --- | --- |
| Goal / why | `## Goal` |
| User-visible behaviour | `## User Behaviour (Study Cases)` — max 5 cases, Before/After prose |
| Existing modules reused | `## What Current (Technical)` |
| Capability split / API boundaries | `# Parallel Domains` — `Provides` / `Consumes` / `Outcome` |
| Schema decisions | Domain `### Data schema changes` |
| API payload decisions | Domain `### API contract` |
| Explicit non-goals from grill | `# Out of Scope` |
| Deferred unknowns | `# Summary` **Important notes** or `# Out of Scope` |

Hard rules from `plan-rules` still apply: one decided path, parallel domains, English body, Tasks at outcome level.

Then `/run-plan` when todos are pending.

---

## Post-plan handoff

Grill finished **after** a `.plan.md` exists — gap-only session. See [post-plan-audit.md](post-plan-audit.md) for how gaps were found.

| Situation | Next step |
| --- | --- |
| Audit found zero gaps | `/run-plan` — no patch needed |
| New decisions conflict with library behaviour | `/plan-behaviour-research`, then patch plan |
| Decisions resolved | **Patch** the existing plan (below), user reviews, then `/run-plan` |
| `/run-plan` already ran; review found misses | Patch plan → re-launch **failed domain only** (same as `run-plan` §5) |

### Patch rules

- Edit the **existing** `.plan.md` in place — do not create a second plan file.
- Change only sections tied to recorded decisions. Leave settled plan text untouched.
- Keep `plan-rules` hard rules: one path, no options, parallel domains, English.
- After patch, run plan-rules self-check mentally (todos ↔ domains, Tasks ↔ study cases, Consumes ↔ Provides).

### Mapping decisions → plan patches

| Decision from grill | Patch target |
| --- | --- |
| Scope / non-goals | `# Out of Scope`, `## Goal` |
| User-visible behaviour | Study cases and/or domain Tasks / Outcome |
| API / function contract | Domain `### Provides`, `### Consumes`, `### API contract` |
| Schema | Domain `### Data schema changes` |
| Domain split or collision | `# Parallel Domains` index + affected `## Domain:` sections + YAML todos |
| Cross-cutting note | `# Summary` **Important notes** |

Sync YAML todo `content` if a domain Outcome changed materially.

### Execute

- Plan patched and reviewed → `/run-plan`
- Do not grill during `/run-plan`
- Do not full re-grill the whole plan after patch — only another **gap-only** session if new ambiguity appears
