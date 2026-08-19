# Post-plan audit

Use in **post-plan** mode after loading the full `.plan.md`. Do not grill until this audit is done.

## Load the plan

Resolve the file in order: user named or attached → plan this chat is working on → newest `*.plan.md` (ask if several).

Read: Goal, Out of Scope, study cases (**After changes**), `# Parallel Domains`, every `## Domain:` (Provides, Consumes, Outcome, Tasks, Data schema, API contract, Inventory), YAML todos, `## Behaviour` when present.

## Seed the decision record from the plan

Treat each **decided** plan statement as already recorded — do not re-ask unless the user wants to change it or new evidence conflicts.

| Plan source | Seed as |
| --- | --- |
| Goal, Out of Scope | Scope decisions |
| Study case **After changes** | Behaviour decisions |
| Each Provides / Consumes call | Interface decisions |
| Data schema / API contract fields | Data & payload decisions |
| Tasks (verb + where + so) | Implementation intent (outcome level) |
| Domain Outcome | Domain completion criteria |

## Find open branches (gap-only scope)

Only grill items in this list. If the list is empty after audit, stop — recommend `/run-plan`.

| Signal | Example | Grill? |
| --- | --- | --- |
| Vague Task (no clear `so`, fuzzy where) | "Improve the API" | Yes |
| Study case **After changes** with no matching Task | Case promises stock error, no Reject/Wire Task | Yes |
| Provides / Consumes mismatch | UI Consumes call not in provider's Provides | Yes |
| Missing contract detail on a Provides call | `POST /orders` Success/Errors incomplete | Yes |
| Undecided language | TBD, consider, optionally, or, "pick one" | Yes |
| Inventory path in two domains | Same file in two domains' lists | Yes |
| Domain Outcome contradicts study case | Outcome says "guest checkout" case says logged-in only | Yes |
| User-named gap | "Grill the stock domain only" | Yes — that slice only |
| Fully specified, consistent plan | All domains have Provides/Consumes/Tasks aligned | **No** — hand off to `/run-plan` |

Skip grilling facts the codebase already proves — explore first, then only ask **decisions** the plan left open.

## Scope the session

Before the first question, output:

```markdown
### Post-plan grill scope

**Plan:** `[path]`
**Mode:** gap-only (not a full re-grill)

**Already decided (from plan):** [N items — brief bullets, no re-questioning]
**Open branches to resolve:** [M items — these are the only grill targets]
**Out of this session:** [everything else in the plan]
```

If **M = 0**, skip to hand off: plan is ready for `/run-plan`.

If the user named one domain or topic, restrict open branches to that slice only.

## Question cards in post-plan mode

Each card must cite the plan anchor:

```markdown
### Decision — [short title]

**Plan gap:** `[domain]` / `[section]` — [quote or paraphrase the vague line]

**Recommended:** …
**Why:** …
**Tradeoff:** …
**Question:** …
```

After each answer, note which plan section will change (for the patch step).

## Patch mapping (after user confirms)

Apply decisions to the existing plan — do not rewrite from scratch. See [plan-handoff.md](plan-handoff.md) § Post-plan handoff.
