# UX Writing / Microcopy

Open when writing or reviewing any in-product text: buttons, labels, errors, empty states, confirmations, notifications.

## Buttons & actions

- **DO** verb + object: "Save changes", "Delete file", "Send invoice". The button alone must answer "what does clicking this do?"
- **NEVER** "Yes" / "No" / "OK" on consequential actions; **DON'T** bare "Submit" / "Continue" when a specific verb exists.
- **DO** sentence case everywhere (buttons, titles, labels). **DON'T** Title Case Every Word or ALL CAPS.
- **DO** keep the verb during progress: "Saving…" not "Loading…".

## Errors

- **DO** three parts when useful: what happened + why + how to fix. **NEVER** blame the user — "We couldn't find an account with that email," not "You entered an invalid email."
- **NEVER** "Oops!" or "Something went wrong". Calm, specific, blameless.
- **DON'T** show raw codes/jargon alone; if a code helps support, append it quietly after the human sentence.
- **DO** put the fix in the message when known ("File must be under 10 MB — this one is 14 MB").
- **DON'T** exclamation marks, "please", or "sorry" padding. State it plainly.

## Confirmations & consequences

- **NEVER** "Are you sure?". **DO** name object + consequence: "Delete 'Q3 report'? This can't be undone." Buttons: "Delete report" / "Cancel".
- **DO** state scope with numbers: "This removes 3 members from the project."
- **DO** success messages that name what happened: "Invoice #204 sent to acme.com" — plus the next action when useful ("View invoice").

## Empty states

- **DO** two jobs: what this space is + how to fill it, with the CTA right there. "No API keys yet. Create a key to start making requests." + [Create API key]
- **DON'T** a lone illustration with "Nothing here!". Distinguish first-use / no-results / error (see states.md).

## Labels & vocabulary

- **DO** one term per concept, everywhere — pick "project" or "workspace", never both for the same thing. Keep a terms list for the product.
- **DO** the user's nouns, not internal names ("Download report", not "Export SSRS artifact").
- **DO** front-load the key word: "Delete account" not "Click here if you would like to delete your account".
- **NEVER** marketing adverbs in product UI: "Effortlessly", "Seamlessly", "Supercharge", "Unlock". Plain verbs; say what happens.
- **DO** tone that scales with stakes — casual for routine, neutral for transactional, formal for irreversible/legal.
- **NEVER** write copy you wouldn't read aloud to a stranger.

## Numbers, dates, formats

- **DO** locale-aware dates and numbers; never raw ISO in body copy.
- **DO** relative time for recent activity ("2h ago") with absolute on hover; absolute ("12 Mar 2026") for records, invoices, logs.
- **DO** consistent precision per context; round display values, keep exact on hover/export.

## Notifications & toasts

- **DO** lead with the event: "Export finished — report.csv ready" + action ("Download").
- **DON'T** notify what the user is looking at, and don't toast errors that need action (keep those inline — see states.md).
