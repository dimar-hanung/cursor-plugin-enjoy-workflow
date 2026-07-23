# Flows, Navigation, Onboarding

Open when designing or reviewing a user flow, navigation structure, onboarding, or a multi-step process.

## Decide first

- **LOCK the user's goal** — the one thing they came to do, in their words
- **LOCK entry points** — where users arrive from (link, search, notification, cold start); design for the worst-informed one
- **LOCK the happy path** — entry → steps → success, with a step count you can defend
- **LOCK the exits** — what "done" looks like, and where every failure/cancel lands

## Flow shape

- **DO** design the path before the page — one decision per screen. **DON'T** send users back to a hub to continue a task; surface the next step in context.
- **DO** group by the user's task ("Things I own"), not the data model ("Resources"). **DO** name navigation with user nouns.
- **DO** simplify the policy/eligibility rule before explaining a complicated path — another screen won't fix a confusing rule.
- **DO** one primary action per screen; secondary actions visually quieter or in overflow.
- **DO** progressive disclosure — defer optional settings/details behind "Advanced" or a later moment. **DON'T** front-load every decision.
- **DO** sensible defaults that do the work; remember previous choices. **DON'T** make users re-decide.
- Wizard vs single page: **DO** a single page when it's roughly ≤7 fields with no dependencies; **DO** a wizard when steps depend on earlier answers or need focus. **DON'T** split a short form into steps for looks.
- Multi-step: **DO** show progress (step x of y, labeled), allow going back without data loss, save partial progress.

## Navigation

- **DO** keep current location visible (active nav state, breadcrumb on deep hierarchies).
- **DON'T** exceed ~7 top-level destinations; group or demote the rest.
- **DO** label navigation with the user's nouns. **DON'T** use internal/team names or clever labels.
- **NEVER** hijack or break browser back. Back never loses data (see forms.md for preserving input).
- **DO** make state deep-linkable and refresh-safe — URL reflects the selected tab, filter, item.
- **DON'T** open new contexts (modals over modals, nested drawers). One overlay level; beyond that, navigate to a page.

## Destructive actions

- **DO** undo instead of confirm when reversible: perform + toast with Undo (see states.md).
- **DO** confirm only truly destructive actions, naming object and consequence: "Delete 'Q3 report'? This can't be undone." with buttons "Delete report" / "Cancel".
- **NEVER** Yes/No buttons on a destructive confirm.
- **DO** separate destructive actions from routine ones (spacing, overflow menu, red only on the destructive item).
- **DON'T** make destructive the default focus or the easiest tap target.

## Onboarding

- **DO** get the user to the core action immediately — the product's first real success is the onboarding.
- **DON'T** ship a multi-screen tour or coach-mark carpet; nobody reads it.
- **DO** ask setup questions only when their answer changes what happens next; defer the rest.
- **DO** keep Skip available on every optional step.
- **DO** design the first-use empty state as the guide (see states.md).

## Dead-end audit

Walk every terminal screen and ask "what now?":

- Success → next likely action or back to a sensible home
- Error → retry / fix / support path (see states.md)
- Empty → what this is + how to fill it (see writing.md)
- Cancel/abandon → returns to where the user was, input preserved
