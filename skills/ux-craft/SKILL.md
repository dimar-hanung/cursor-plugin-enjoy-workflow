---
name: ux-craft
description: >-
  ALWAYS apply when designing, building, or reviewing how a product works:
  user flows, navigation, onboarding, forms, validation, data tables, lists,
  UX writing/microcopy, loading/empty/error/success states, accessibility,
  trust/consent, AI output, billing, permissions, and destructive actions.
  Complements ui-craft (how it looks and moves). Skip only for pure
  backend/data tasks with no user-facing surface.
---

# UX Craft

Work with the grain of how people think, read, decide, trust, and recover — not against it. `ui-craft` covers how it looks and moves; this skill covers how it works and reads. Existing product conventions win unless they violate a **Core law** — then make the smallest fix and name the conflict.

## Before answering

Identify silently; expose in the answer only when useful:

- User/role, primary decision, and the next action the UI should make obvious
- Value visible before signup, payment, permission, or sensitive input
- Happy path + empty/loading/failed/partial/offline + recovery path
- Whether the task works with keyboard, touch, narrow viewport, reduced motion
- Project contract: design system, voice, i18n, nearby patterns

## Core laws (ordered — earlier beats later on conflict)

1. **Make the next action obvious** — never leave "what do I do now?"
2. **Simplify the rule before the screen** — a confusing policy will feel confusing no matter how polished the UI
3. **Show value before asking for effort** — benefit visible before signup, payment, permission, or long forms
4. **Show state, not just controls** — user must know what the system is doing, did, and will do if they act
5. **Usable means accessible** — mouse/perfect vision/large screen/fast network is not a requirement users consented to
6. **Preserve user effort** — input, choices, progress, drafts survive errors, navigation, refresh, retry
7. **Undo beats confirm** — reversibility is the real safety net; confirm only irreversible, object-named actions
8. **Do not surprise the user** — send/charge/delete/share/publish/automate must expose consequences before action
9. **Match the user's model, not the system's** — name things after the task, not the table/endpoint/class
10. **Edges are the product** — empty, loading, failed, partial, offline, permission-denied are first-class screens
11. **Words are UI** — read labels/errors aloud; awkward spoken = wrong written

## Anti-patterns (by force)

- **BLOCK** — do not ship; offer the closest compliant alternative: bundled consent; AI/automation commits send/publish/charge/delete without review; destroys input on error/refresh; primary task hover-only or pointer-only; high-blast-radius delete without object-specific safety + typed confirm when no undo
- **PUSH BACK** — object once, propose smallest safer change: modal for low-stakes confirm or marketing; error toast that auto-dismisses; disabled submit with no explanation; onboarding asks everything upfront; "Are you sure?" without naming the object; signup/permission before value visible; spinner with no label >1s
- **MITIGATE** — fix inside scope: empty state that only says "No items"; success toast with no persistent state change; one hard question instead of several easy ones

## Quick reject checklist

- Merge or remove steps/modals that only relay what the next one says.
- Label above every input — not placeholder-as-label.
- Input, select, and textarea fills remain visibly distinct from the surrounding surface across resting, focus, error, and disabled states.
- Submit stays enabled; reveal errors on attempt.
- Destructive confirms name object + consequence on buttons — not "Are you sure?" with Yes/No.
- Table body: left text, right numbers with `tabular-nums`; no center-aligned body or wrapped IDs.
- Skeleton matching final layout for structured content — not a bare spinner.
- Errors say what happened + how to fix — not "Oops! Something went wrong".
- Onboarding reaches the core action immediately — not a multi-screen tour.
- Primary actions available via keyboard and touch — not hover-only.
- AI/automation does not send/publish/charge/delete without preview + explicit approval.
- One frame + hairline separators between items — not nested boxes or cards.
- All readable UI copy uses `text-base` minimum, including badges, chips, tags, helper text, and table metadata; secondary via muted color, not `text-xs`/`text-sm`.

## Reference routing

Open the smallest set needed. When several match, start highest-stakes: **trust/recovery → input → flow → copy → polish**.

| Trigger | Open first | Also when |
| --- | --- | --- |
| Navigation, flows, onboarding, wizards, IA | [flows.md](references/flows.md) | Dense decisions → [cognitive-load.md](references/cognitive-load.md) |
| Dense screens, settings, defaults, choices | [cognitive-load.md](references/cognitive-load.md) | Unclear sequence → flows |
| Forms, search, filters, uploads, validation | [forms.md](references/forms.md) | Failure → states; import/bulk → trust |
| Tables, lists, dashboards | [tables.md](references/tables.md) | Empty/error → states |
| Keyboard, focus, touch, contrast, motion, responsive | [accessibility.md](references/accessibility.md) | Any interaction behavior change |
| Sharing, billing, privacy, permissions, AI, automation, destructive | [trust.md](references/trust.md) | Recovery → states; consent copy → writing |
| Loading, empty, error, offline, undo, toasts | [states.md](references/states.md) | Input loss → forms; external impact → trust |
| Buttons, errors, empty copy, banners, toasts | [writing.md](references/writing.md) | Cost/consent/billing → trust |

## Output

- **Review:** findings by severity — issue, violated law/anti-pattern, user impact, smallest fix, verification needed
- **Implement:** smallest project-consistent change; report changed behavior + states covered + remaining risk
- **Copy:** before/after when useful; route new strings through existing i18n when present

## Review table

| Location | Problem | Severity | Fix |
| --- | --- | --- | --- |

Verdict: `Clean` · `Needs pass` · `Broken UX`.

## References

- [flows.md](references/flows.md) — flows, navigation, onboarding, wizards, destructive actions
- [cognitive-load.md](references/cognitive-load.md) — decisions per moment, progressive disclosure, defaults
- [forms.md](references/forms.md) — form layout, inputs, validation, multi-step
- [tables.md](references/tables.md) — data tables, lists, sorting, bulk actions, responsive
- [accessibility.md](references/accessibility.md) — keyboard, focus, touch, contrast, motion, responsive
- [trust.md](references/trust.md) — consent, preview, AI/automation, billing, permissions, audit
- [writing.md](references/writing.md) — UX writing: buttons, errors, confirmations, tone
- [states.md](references/states.md) — loading/empty/error/success, undo, toasts, optimistic updates
