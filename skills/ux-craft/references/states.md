# States & Feedback

Open when wiring async actions, loading, empty, error, or success behavior. A screen is not done when the happy path renders — it's done when all states are designed.

## The state checklist (every async surface)

- [ ] Loading (first load *and* refetch)
- [ ] Empty: first-use / no-results / cleared
- [ ] Error, partial success, offline, permission-denied
- [ ] Success: unmistakable confirmation
- [ ] Pending action: the triggering control shows progress

## Feedback by duration

- **<100ms** — no indicator; showing one adds noise.
- **100ms–1s** — subtle: button label swap ("Saving…"), inline spinner. **DON'T** block the screen.
- **1s–10s** — skeleton (first load) or progress indicator; keep the rest of the UI usable.
- **>10s** — progress + estimate if honest, cancel if possible; **DO** ask first whether the wait can be removed, backgrounded, or cached — spinner is not a strategy.
- **DO** skeletons that mirror the final layout — same columns, same blocks — so nothing shifts on arrival. **DON'T** a centered spinner in a void for structured content.
- **DON'T** show a flash of loading state for cached/instant data — delay indicators ~150ms so fast responses never flicker one.

## Optimistic updates & undo

- **DO** update optimistically when the action is reversible and usually succeeds (toggle, rename, reorder); roll back + inline error on failure.
- **DON'T** optimistic for payments, sends, deletes with external effects — show real progress instead.
- **DO** undo over confirm for reversible destructive actions: perform immediately + toast "Message archived — Undo" (5–10s window).
- **DO** keep the triggering button as the progress locus: disable during flight, verb stays ("Sending…"). **NEVER** leave a form silently frozen.

## Errors & recovery

- **DO** pair every error with its recovery: Retry (safe/idempotent), Fix (focus the field), or a support path with context attached.
- **NEVER** lose user input on failure — the retry must resend what they wrote.
- **DO** errors inline at the point of failure; **DON'T** toast an error that needs action (toasts vanish).
- **DO** distinguish partial failure ("3 of 5 files uploaded — retry failed files") from total failure.
- **DO** design offline/timeout for critical flows: queued state + auto-retry beats a dead modal.

## Empty states (three kinds, three designs)

- **First-use** — teach + invite: what this space is + primary CTA. This is onboarding (see flows.md).
- **No-results** — show the active query/filters and how to loosen them ("No matches for 'invoce' — check spelling or clear filters"). **DON'T** reuse the first-use art.
- **Cleared/done** — quiet, or a small win ("Inbox zero"). No CTA pressure.

## Toasts & notifications

- **DO** toasts for confirmations and undo only; auto-dismiss 5–8s; never stack more than ~3.
- **DON'T** toast what's already visible on screen, and **NEVER** put required actions only in a toast.
- **DO** make success survivable-by-glance: if the user looks away for 2s, the outcome must still be discoverable (updated list, badge, activity log).
