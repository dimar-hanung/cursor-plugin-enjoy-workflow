---
name: grill-me
description: >-
  Interview the user relentlessly about a plan or design until shared
  understanding is reached, one decision at a time. Use before writing a
  `.plan.md`, after a `.plan.md` exists (gap-only audit), when stress-testing
  a design, or when the user mentions "grill me". Not for listing options
  (/brainstorm), first-principles reframing (/fundamental-think), unclear
  client requirements (client-business-understanding), or drafting the plan
  from scratch (plan-rules).
disable-model-invocation: true
---

# Grill Me

Stress-test **one** design path. The user keeps control; the agent asks, explores, and records decisions.

Works in two modes — pick automatically from context:

| Mode | When | Scope |
| --- | --- | --- |
| **Pre-plan** | No `.plan.md` yet, or user is designing before planning | Full decision tree for the bounded feature |
| **Post-plan** | User attached/named a `.plan.md`, or asks to vet/review the plan before `/run-plan` | **Gap-only** — open branches the plan left vague; never re-grill settled plan text |

If post-plan audit finds **zero gaps**, say the plan is ready and recommend `/run-plan` — do not invent questions.

## Vs other workflows

| Ask | Use |
| --- | --- |
| Options, names, compare approaches, creative directions | `/brainstorm` |
| Broad/solution-shaped ask needing foundational questions | `/fundamental-think` |
| Unclear client requirement, meeting notes, business process | `client-business-understanding` |
| Write a new `.plan.md` from scratch | `plan-rules` (Plan mode) |
| Execute an existing plan in parallel | `/run-plan` |
| **Stress-test decisions; resolve open branches** | **This skill** |

Do not run this skill **during** `/run-plan`. Wait for domain agents to finish; then gap-only grill if review found misses.

## When to use / skip

| Case | Action |
| --- | --- |
| Design before first `.plan.md` | Pre-plan mode |
| `.plan.md` exists; vet before execute, or fix vague spots | Post-plan mode — [post-plan-audit.md](references/post-plan-audit.md) |
| `.plan.md` is consistent; user wants to build | Skip — `/run-plan` |
| Trivial change (typo, one obvious file) | Skip — execute directly |
| User wants many options | `/brainstorm` first; pick one path, then grill |
| Client-facing requirement clarification | `client-business-understanding` first |

## Hard rules

- **One question per turn.** Wait for the user's answer before the next card.
- **Facts from the codebase** — trace paths, open files, read schema/APIs. Do not ask what code already shows.
- **Decisions are the user's** — recommend a choice; user leads. Do not treat "OK" as consent without a recorded choice.
- **Do not implement** during this skill. Do not edit files except to explore (and post-handoff patch — see below).
- **Do not write or patch `.plan.md` during grilling** — record decisions first; patch or create plan only after user confirms the decision record.
- **One decided path** — no A/B options inside a question.
- **English** for decision cards and the final record (matches `plan-rules`). User may answer in Indonesian.
- Follow workspace **principles** when framing tradeoffs.

**Post-plan only:**

- Treat decided plan text as **already recorded** — do not re-ask unless the user wants to change it.
- Every question must cite a **plan gap** (domain, Task, Provides, study case, etc.).
- Do not full re-grill the entire plan from Goal downward.

## Procedure

### 0. Detect mode

1. User named/attached a `.plan.md`, or chat is clearly about reviewing an existing plan → **post-plan**
2. Otherwise → **pre-plan**

Post-plan: run [post-plan-audit.md](references/post-plan-audit.md) before the first question. Output **Post-plan grill scope**. If zero open branches → recommend `/run-plan` and stop.

### 1. Anchor

**Pre-plan** — restate objective, scope boundary, inputs (draft, chat). Split if too broad; grill one slice per session.

**Post-plan** — restate plan Goal, which domains/slices are in scope, and the open-branch list from the audit.

### 2. Explore (verify, never infer)

Same grounding as `plan-rules`:

1. Trace one real path end to end when touching existing code.
2. Find the closest similar feature.
3. Map callers and file ownership (collision hints).
4. Split reuse vs new.

In post-plan mode, also verify plan Inventory paths and Provides/Consumes against what you opened. Cite only files you opened.

### 3. Maintain a decision record

After every answer:

| Field | Content |
| --- | --- |
| Decision | Short title |
| Choice | What was decided |
| Rationale | Why |
| Consequences | What this locks in downstream |

Post-plan: add **Plan patch target** (which section will change).

Do not reopen a recorded decision unless the user introduces conflicting evidence.

### 4. Ask — one card per turn

**Pre-plan** card:

```markdown
### Decision — [short title]

**Recommended:** [one concrete choice]
**Why:** [1–2 sentences]
**Tradeoff:** [1 sentence]
**Question:** [single clear question]
```

**Post-plan** card — must include plan anchor:

```markdown
### Decision — [short title]

**Plan gap:** `[domain]` / `[section]` — [vague line or missing link]
**Recommended:** …
**Why:** …
**Tradeoff:** …
**Question:** …
```

After each answer: `✅ Recorded: **[decision]** — [chosen option]`

Show settled / open counts when useful. Never show a percentage.

**Priority:** scope → users → interfaces → data/state → failure modes → security → ops → migration → testing → rollout → ownership → stopping criteria. Skip immaterial categories.

**Fidelity:** low-fidelity decisions here; high-fidelity UI layout → prototype first, then resume grill. UI behaviour → `ux-craft`; visual/motion → `ui-craft`.

### 5. Completion

```markdown
### ✅ Decision record
| Decision | Choice | Rationale | Consequence | Plan patch (post-plan only) |
| --- | --- | --- | --- | --- |

### ⚠️ Risks & accepted unknowns
- …

### 🏁 Completion criteria
- …

### 👉 Next step
[See references/plan-handoff.md — pre-plan vs post-plan]
```

Do not end with another question.

### 6. Hand off (after user confirms)

| Mode | Hand off |
| --- | --- |
| Pre-plan | Optional `/plan-behaviour-research` → `plan-rules` (new `.plan.md`) → `/run-plan` |
| Post-plan | Patch existing `.plan.md` per [plan-handoff.md](references/plan-handoff.md) → user reviews → `/run-plan` |

Never skip from pre-plan grill straight to `/run-plan` without a plan file.

## Don't

- Don't ask multiple questions in one message
- Don't dump a questionnaire
- Don't full re-grill a decided plan (post-plan = gaps only)
- Don't expand scope mid-session without consent
- Don't silently accept the recommended answer
- Don't grill and implement in the same turn
- Don't grill while `/run-plan` domain agents are running

## References

- [post-plan-audit.md](references/post-plan-audit.md) — load plan, seed decisions, find gaps, scope the session
- [plan-handoff.md](references/plan-handoff.md) — pre-plan → new plan; post-plan → patch → `/run-plan`
