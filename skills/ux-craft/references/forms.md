# Forms, Inputs, Validation

Open this file when building or reviewing any form, from login to multi-step checkout.

## Contents

- Fields
- Input behavior
- Validation
- Submission
- Multi-step forms
- Quick checklist

## 1. Fields

Ask the minimum. Every field must be used by the product now.

- Infer or fetch instead of asking — country from phone code, city from postal code, data you can retrieve later.
- Single column layout. Side-by-side only for tightly-coupled pairs (first/last name, month/year).
- Label above the input, always visible. Placeholder-as-label vanishes on focus and kills recall.
- Placeholder only for format examples ("name@company.com"); helper text below for rules that matter before typing.
- Mark **optional** fields, not required ones (most fields should be required — if not, cut them).
- Group related fields with headings; order easy → hard (name before payment).
- Size inputs to expected content — a postal-code field should not be full width.

## 2. Input behavior

Small mechanical choices at the field level compound into large time savings — or friction — across every submission.

- Match input type to data: `type="email"`, `inputmode="numeric"`, `type="tel"` — right mobile keyboard for each.
- Set `autocomplete` attributes (name, email, address, cc-number); autofill is the fastest form.
- Auto-format as the user types (card number spacing, phone grouping) and accept any paste — strip spaces and dashes yourself.
- Trim whitespace; trailing space should not fail validation.
- Autofocus the first field on dedicated form pages; no autofocus inside long content pages.
- Radio or segmented controls for fewer than five known options; combobox with search for large bounded sets — not a dropdown for either extreme.

## 3. Validation

Prevent before validate, validate before submit — catch issues at the earliest step.

- Validate a field on blur after first interaction; re-validate on keystroke only once it is in error (reward fixing instantly).
- Untouched fields stay unflagged while the user is still working.
- Submit stays enabled. On submit, show an error summary at top + inline errors, and move focus to the first error.
- Errors say what's wrong + how to fix: "Card number is 15 digits — Amex cards start with 34 or 37" (see writing.md for tone).
- All input survives errors, back navigation, and accidental refresh where feasible.
- Server validates too; map server errors back to fields, not a generic banner.

## 4. Submission

The moment of submit is when anxiety peaks — the UI must show progress, preserve effort, and make the outcome unmistakable.

- Progress on the button itself ("Saving…"), disabled during flight, verb stays.
- Success is unmistakable: navigate or confirm what happened ("Invoice sent") — not a silent state change.
- Long forms: warn before navigation discards unsaved changes, or autosave drafts.

## 5. Multi-step forms

Splitting a form is a pacing decision: each step should feel like progress, not like arbitrary gates.

- Labeled progress and back navigation without loss.
- Persist each completed step server-side or locally.
- Review step for consequential submissions (orders, applications) — editable per section.

## 6. Quick checklist

Try submitting empty, submitting with one bad field, going back mid-flow, and refreshing — input and errors should survive all four.

- [ ] Is every field necessary now?
- [ ] Does every field have a visible label (not placeholder-as-label)?
- [ ] Does submit stay enabled with errors shown on attempt?
- [ ] Does input survive errors, back, and refresh?
- [ ] Are server errors mapped to fields?
