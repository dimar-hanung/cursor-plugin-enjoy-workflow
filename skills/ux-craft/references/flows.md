# Flows, Navigation, Onboarding

Open this file when designing or reviewing a user flow, navigation structure, onboarding, or a multi-step process.

## Contents

- Decide first
- Flow shape
- Navigation
- Destructive actions
- Onboarding
- Dead-end audit
- Quick checklist

## 1. Decide first

Flows fail when screens are designed in isolation. Lock the shape of the journey before debating layout details.

Before drawing screens, lock these four:

- **The user's goal** — the one thing they came to do, in their words
- **Entry points** — where users arrive from (link, search, notification, cold start); design for the worst-informed one
- **The happy path** — entry → steps → success, with a step count you can defend
- **The exits** — what "done" looks like, and where every failure/cancel lands

## 2. Flow shape

Design the path before the page — one decision per screen.

- Surface the next step in context; do not send users back to a hub to continue a task.
- Group by the user's task ("Things I own"), not the data model ("Resources").
- Name navigation with user nouns.
- Simplify the policy or eligibility rule before explaining a complicated path — another screen will not fix a confusing rule.
- One primary action per screen; secondary actions visually quieter or in overflow.
- Progressive disclosure — defer optional settings and details behind "Advanced" or a later moment.
- Sensible defaults that do the work; remember previous choices so users do not re-decide.
- Single page when roughly seven or fewer fields with no dependencies; wizard when steps depend on earlier answers or need focus.
- Multi-step: show labeled progress (step x of y), allow going back without data loss, save partial progress.

## 3. Navigation

Navigation is the user's map of the product — it must answer "where am I?" and "how do I get back?" without forcing them to remember the hierarchy.

- Keep current location visible (active nav state, breadcrumb on deep hierarchies).
- About seven top-level destinations maximum; group or demote the rest.
- Label navigation with the user's nouns — not internal team names or clever labels.
- Browser back is never hijacked and never loses data (see forms.md for preserving input).
- State is deep-linkable and refresh-safe — URL reflects the selected tab, filter, item.
- One overlay level at a time; beyond that, navigate to a page instead of modals over modals or nested drawers.

## 4. Destructive actions

The cost of a mistake scales with blast radius — match the safety mechanism to how hard the action is to reverse.

- Undo instead of confirm when reversible: perform + toast with Undo (see states.md).
- Confirm only truly destructive actions, naming object and consequence: "Delete 'Q3 report'? This can't be undone." with buttons "Delete report" / "Cancel".
- Destructive confirms never use Yes/No buttons.
- Separate destructive actions from routine ones (spacing, overflow menu, red only on the destructive item).
- Destructive is never the default focus or the easiest tap target.

## 5. Onboarding

The product's first real success is the onboarding — get the user to the core action immediately.

- No multi-screen tour or coach-mark carpet; nobody reads it.
- Ask setup questions only when their answer changes what happens next; defer the rest.
- Skip available on every optional step.
- Design the first-use empty state as the guide (see states.md).

## 6. Dead-end audit

A flow is only as good as its worst terminal screen — the moment the user succeeds, fails, or gives up and has nowhere sensible to go.

Walk every terminal screen and ask "what now?":

- Success → next likely action or back to a sensible home
- Error → retry / fix / support path (see states.md)
- Empty → what this is + how to fill it (see writing.md)
- Cancel/abandon → returns to where the user was, input preserved

## 7. Quick checklist

Walk the happy path once, then walk every exit — cancel, error, empty, and success — before calling the flow done.

- [ ] Is there one clear decision per screen?
- [ ] Can the user continue the task without returning to a hub?
- [ ] Does browser back preserve data?
- [ ] Is URL state shareable and refresh-safe?
- [ ] Does every terminal screen have a clear "what now?"
