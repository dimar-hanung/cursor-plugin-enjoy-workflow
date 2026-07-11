---
name: plan-rules
description: >-
  Formats implementation plans with overview (goal, current state, changes,
  visualization), phased tasks, out of scope boundaries, and factual summary
  for tech lead review. Use when creating, drafting, or presenting any plan —
  implementation plan, architecture plan, refactoring plan, feature plan,
  migration plan, rollout plan, or when switching to Plan mode.
---

# Plan Rules

Every plan MUST follow the response structure below so tech leads can quickly review scope before approving implementation.

## When This Applies

Apply this skill whenever you:

- Create or propose an implementation plan
- Answer "how should we build X?" with a multi-step approach
- Switch to Plan mode or ask the user to approve before coding
- Break a large task into phases or milestones

Skip only for trivial one-line changes (single file, obvious fix).

## Rules

- Massive explore to gather context
- Ask minimal 2 questions

## Mandatory Response Structure

Use this structure in order. Do not skip sections. Do not add extra top-level sections.

```markdown
# Overview

## Goal
[Restate the requirements and goals in 2-3 sentences]

## What Current
[Describe the existing state — relevant files, modules, schema, APIs, and behavior as they exist today. Factual only, no recommendations]

## What Changes
[High-level list of what will change — new modules, modified areas, schema, APIs, config. Factual only, no recommendations]

## Visualization
[At least one Mermaid diagram showing the planned flow, architecture, or data model. Use real file, module, or service names from the codebase]

### Title ...

- ... is a flowchart
- ... is a sequence diagram
- ... is an ERD, ... is a C4 diagram, ... is a state diagram, ... is a phased rollout diagram

### Another title ...

# Implementation Phases

## Phase 1: [Descriptive Title]
**Goal**: [What this phase accomplishes]

**Tasks:**

### Task 1.1: [Clear description including setup]
Focused on essential logic implementation. No complete code — main logic and structure for AI guidance. Include file location(s) to change.

### Task 1.2: [Clear description]
[Continue with additional tasks and phases as needed]

# Out of Scope
[Explicit list of what this plan does NOT cover — related features, follow-up work, edge cases, or areas deferred to later. Factual boundaries only, no recommendations]

# Summary
[Summarize the plan: new files, modified files, data schema changes, API endpoints, and important notes for implementation. No suggestions or recommendations — factual scope only so tech leads can review and approve before starting implementation]
```

## Overview Rules

### Goal

- Restate user requirements in plain language — what we are building and why
- 2–3 sentences max; no implementation detail here

### What Current

- Describe how the system works today in the areas affected by this plan
- Include existing files, modules, schema, endpoints, and current behavior
- Ground the plan in the codebase — name real paths and components discovered during analysis
- Factual only — describe what exists, not what should exist

### What Changes

- Bullet list of affected areas at a glance
- Include layers (frontend/backend/DB), key files or modules, schema, endpoints if known
- Factual scope only — no suggestions or alternatives

### Visualization

- Always include at least one Mermaid diagram in Overview
- Use project-specific names, not generic labels ("PaymentService", not "Backend")
- Keep ≤15 nodes; use subgraphs if the plan is large

| Plan type | Diagram |
| --- | --- |
| Feature / workflow | `flowchart TD` or `flowchart LR` |
| API / request flow | `sequenceDiagram` |
| Data / schema | `erDiagram` |
| Architecture | `flowchart` with subgraphs or `C4Context` |
| State / lifecycle | `stateDiagram-v2` |
| Phased rollout | phased `flowchart` or `gantt` |

## Task Writing Rules

Each task MUST include:

- **File location** — exact path(s) to create or modify
- **Main logic** — essential behavior, data flow, and structure — not full code
- **Guidance level** — enough for an AI or developer to implement without guessing intent

Each task MUST NOT include:

- Complete code blocks or copy-paste-ready implementations
- Suggestions, recommendations, or "consider also…" notes
- Vague actions like "update the logic" without naming the file and what changes

## Phase Rules

- One phase = one cohesive milestone; split when dependencies or review boundaries differ
- Phase title describes the outcome, not just the layer (e.g. "Payment validation API" not "Backend work")
- Number tasks as `Task N.M` (e.g. Task 2.1, Task 2.2)
- Order tasks by dependency — earlier tasks unblock later ones

## Out of Scope Rules

The Out of Scope section sets clear boundaries before the final summary. Include:

- Features or requirements explicitly excluded from this plan
- Related work deferred to a future phase or ticket
- Edge cases or scenarios not handled in this implementation
- Areas mentioned in discussion but not part of the approved scope

Do NOT include in Out of Scope:

- Suggestions for future improvements
- "Nice to have" recommendations — only state what is excluded, not what could be added later

If nothing is out of scope, write: `None — full scope as stated in Goal.`

## Summary Rules

The Summary section is factual scope only. Include:

- **New files** — path and purpose
- **Modified files** — path and what changes
- **Data schema changes** — tables, columns, migrations
- **API endpoints** — method, path, brief purpose
- **Important notes** — constraints, env vars, config, breaking changes

Do NOT include in Summary:

- Suggestions or recommendations
- Trade-off opinions or alternative approaches
- Risk advice unless it is a stated requirement or hard constraint from the user

## Writing Rules

- **Overview first** — restate requirements before phases
- **Concrete over vague** — name files, functions, endpoints
- **One plan, one goal** — split unrelated work into separate plans
- **Proportional detail** — small plans may use one phase; large plans need multiple phases

## Anti-patterns

- Overview with only prose and no Goal / What Current / What Changes / Visualization sections
- Visualization missing or using generic node names ("Frontend", "Database")
- Phases with tasks that omit file paths
- Tasks with full code instead of logic/structure guidance
- Summary that reads like advice instead of a change list
- Missing Out of Scope section or vague boundaries ("etc.", "other things")
- Extra sections (Trade-offs, Review Checklist, Recommendations) outside the mandatory structure
