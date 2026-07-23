# States & Feedback

Open this file when wiring async actions, loading, empty, error, or success behavior. A screen is not done when the happy path renders — it is done when all states are designed.

## Contents

- The state checklist
- Feedback by duration
- Optimistic updates & undo
- Errors & recovery
- Empty states
- Toasts & notifications
- Quick checklist

## 1. The state checklist (every async surface)

Every surface that loads, submits, or waits on the network needs explicit designs beyond the happy path — if you only designed success, you only designed one state.

- [ ] Loading (first load *and* refetch)
- [ ] Empty: first-use / no-results / cleared
- [ ] Error, partial success, offline, permission-denied
- [ ] Success: unmistakable confirmation
- [ ] Pending action: the triggering control shows progress

## 2. Feedback by duration

Match the weight of feedback to how long the user waits — too much noise for fast actions, too little structure for slow ones.

- **<100ms** — no indicator; showing one adds noise.
- **100ms–1s** — subtle: button label swap ("Saving…"), inline spinner. Screen stays usable.
- **1s–10s** — skeleton (first load) or progress indicator; keep the rest of the UI usable.
- **>10s** — progress + estimate if honest, cancel if possible; ask first whether the wait can be removed, backgrounded, or cached — spinner is not a strategy.
- Skeletons mirror the final layout — same columns, same blocks — so nothing shifts on arrival.
- Delay loading indicators ~150ms for cached/instant data so fast responses never flicker.

## 3. Optimistic updates & undo

Speed and safety trade off — optimistic UI earns its place only when rollback is cheap and failure is rare.

- Update optimistically when the action is reversible and usually succeeds (toggle, rename, reorder); roll back + inline error on failure.
- Real progress for payments, sends, deletes with external effects — no optimistic UI.
- Undo over confirm for reversible destructive actions: perform immediately + toast "Message archived — Undo" (5–10s window).
- The triggering button is the progress locus: disabled during flight, verb stays ("Sending…"). Forms never freeze silently.

## 4. Errors & recovery

An error without a recovery path is a dead end — the user must always know whether to retry, fix something, or escalate.

- Every error paired with recovery: Retry (safe/idempotent), Fix (focus the field), or a support path with context attached.
- User input survives failure — retry resends what they wrote.
- Errors inline at the point of failure; errors that need action stay inline, not in toasts (toasts vanish).
- Partial failure is distinct from total failure ("3 of 5 files uploaded — retry failed files").
- Offline and timeout for critical flows: queued state + auto-retry beats a dead modal.

## 5. Empty states (three kinds, three designs)

"Empty" is not one state — first-use, no-results, and cleared each mean something different and need different copy and visuals.

- **First-use** — teach + invite: what this space is + primary CTA. This is onboarding (see flows.md).
- **No-results** — show the active query/filters and how to loosen them ("No matches for 'invoce' — check spelling or clear filters"). Not the same art as first-use.
- **Cleared/done** — quiet, or a small win ("Inbox zero"). No CTA pressure.

## 6. Toasts & notifications

Toasts confirm what already happened — they are not a substitute for persistent UI state or inline errors.

- Toasts for confirmations and undo only; auto-dismiss 5–8s; never stack more than about three.
- No toast for what is already visible on screen.
- Required actions never live only in a toast.
- Success survives a glance away: if the user looks away for 2s, the outcome must still be discoverable (updated list, badge, activity log).

## 7. Quick checklist

Throttle the network, submit invalid data, and dismiss every toast — the UI should still tell a coherent story.

- [ ] Are loading, empty, error, and success all designed?
- [ ] Does feedback duration match the wait time?
- [ ] Does every error have a recovery path?
- [ ] Is input preserved on failure?
- [ ] Can success still be seen after the toast dismisses?
