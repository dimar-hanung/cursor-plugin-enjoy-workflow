---
name: plan-rules
description: >-
  Formats implementation plans as Cursor `.plan.md` files with YAML frontmatter
  (Plan UI). Agent-first domains ordered bottom-up by codebase deps (default
  backend → frontend). Must do + Inventory per domain. Plans are straightforward
  directives with no questions, options, or opinions — ask decisions via
  AskQuestion outside the plan. Plans may be large — do not truncate. Use when
  creating, drafting, or presenting any plan — or when switching to Plan mode.
---

# Plan Rules

## Plan tone (non-negotiable)

The plan is for an AI agent to **execute**, not to discuss. Write **one** decided path.

- **Do** state facts and required work: Goal, What Changes, Must do, Inventory, Out of Scope.
- **Do not** put questions, A/B options, "or", "optionally", "consider", "we could", trade-off lists, or opinionated recommendations in the plan body or frontmatter.
- **When a decision matters** → stop writing the plan; **AskQuestion outside the plan** (≤4/round). Bake the answer in as settled fact, then continue.
- No "pick one", "recommended", "prefer X unless…", or open-ended choices inside `.plan.md`.

## Before writing

1. Explore real paths and deps.
2. Blocking A vs B → **AskQuestion outside the plan** (≤4/round). Never put questions, options, or opinions in `.plan.md`.
3. Bake answers into Must do / Out of Scope as facts, then write the plan (YAML frontmatter first). Domains, not task lists. Do not truncate.

## Domain order

A **domain** = one dependency-bounded area (inside a project or across projects). Order by codebase deps: foundations before dependents — not by feature story.

- **Stack (default):** shared → **backend** (one domain per area) → **frontend** → wiring  
e.g. `shared-types` → `user-service` → `order-service` → frontend
- **Inside BE:** schema → repos → services → handlers
- **Inside FE:** utils/types → components → pages that use them  
e.g. `OrderLineItem` → `OrderSummary` → `Checkout`

Wrong: one blob “Frontend”/“Backend”, or frontend before the APIs it needs.

## Frontmatter

```yaml
---
name: Short plan title
overview: One-line summary (or "")
todos:
  - id: domain-user-service
    content: "user-service: after shared-schema; done when Must do passes"
    status: pending
isProject: false
---
```

One `todo` per domain, same order as Domain order. Status: `pending` | `in-progress` | `completed` | `error`.

## Body

This order only. No extra top-level sections. No Domain Index / Risks / Review Surface.

```markdown
# Overview

## Goal
[What and why.]

## What Current
[Existing modules / APIs that matter.]

## What Changes
[High-level changes; detail under domains.]

## Visualization
[Each diagram MUST have a title and a short description of what it shows. Skip the whole section if none needed.]

### [Title — e.g. Order create flow]
[1–2 sentences: what this diagram visualizes.]
```mermaid
…
```

### [Title — e.g. Domain dependency order]
[1–2 sentences: what this diagram visualizes.]
```mermaid
…
```


# Implementation by Domain

**Done when:** all Must do boxes checked, Inventory paths exist, no out-of-scope work.

## Domain order
1. `[shared / schema]` depends on none
2. `[backend]` depends on 1
3. `[frontend]` depends on 2

domain order example: `SCHEMA - Master Checkout` → `BACKEND [Codebase Name] - User Service` → `BACKEND [Codebase Name] - Order Service` → `FRONTEND [Codebase Name] - Order Summary` → `FRONTEND [Codebase Name] - Checkout`

## Domain: [matches Domain order #1]
**Goal**: … 1 or 2 paragraphs
**Depends on**: none

### Must do
- [ ] …
- [ ] Reject … / Persist … / Expose … / Call … / Do not …

### Inventory
- **New files** — `path` — purpose
- **Modified files** — `path` — what changes
- **Data schema changes** — … (or None)
- **API endpoints** — `METHOD /path` — purpose (or None)

## Domain: [matches Domain order #2+]
**Goal**: … 1 or 2 paragraphs
**Depends on**: …

### Must do
- [ ] …

### Inventory
- …


# Out of Scope
[Non-goals / nice-to-haves. Or: None.]

# Summary
- **Important notes** — env, config, breaking changes spanning domains
```

## Must do

Observable, required checkboxes. Mix shapes — not only `When…`.

Good:

- When `POST /orders` is valid and stock exists, create the order and decrement stock atomically.
- Reject insufficient stock with `409` `{ code: "INSUFFICIENT_STOCK" }`.
- Return `{ id, status, total }` on create.
- Persist `orders.status` default `pending`; never null.
- Migrate `orders`: add `currency` `char(3) NOT NULL DEFAULT 'USD'`.
- Expose `OrderCreated` `{ orderId, userId }` for billing.
- Call `GET /users/:id` first; if missing, abort `404`.
- Auth: only owner or `admin` may `GET /orders/:id`.
- Idempotent on `Idempotency-Key`: same key + body → same order, no duplicate row.
- After success, enqueue `order.created` once (consumers must be idempotent).
- Render order detail with line items; empty cart → empty state, not an error toast.
- Disable Submit while the request is in flight.
- Redirect to `/orders/:id` after create succeeds.
- Keep copy/labels matching existing checkout strings.
- Do not charge payment here — billing owns charges.

Bad (never in the plan):

- Improve the API / handle errors properly / consider edge cases.
- Optionally add CSV? / Should we support guest checkout?
- Redis vs in-memory? / Prefer Redis unless latency is low (ask via AskQuestion outside the plan; then write one chosen approach)
- We could use webhooks or polling — agent should decide
- Recommended: soft delete; alternatively hard delete if compliance requires it

