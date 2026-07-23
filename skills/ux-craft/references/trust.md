# Trust, Consent & External Impact

Open this file when designing sharing, billing, privacy, permissions, AI output, automation, imports, bulk changes, or destructive actions with external effects.

## Contents

- Do not surprise
- Consent
- AI & automation
- Permissions & billing
- Imports & bulk changes
- Quick checklist

## 1. Do not surprise

Send, publish, charge, delete, share, or sync only when the user knows it happened.

- Preview before external impact — real audience, content, timing, permissions.
- Generic "Are you sure?" is not enough (see writing.md).

## 2. Consent

Consent works when the user understands what they are agreeing to, at the moment it matters — not when they are eager to finish onboarding.

- Ask at the moment it matters, not only at onboarding.
- Required agreement, marketing, and tracking each get their own clear choice — never one bundled checkbox.
- Name object, audience, destination, duration where relevant.
- Consent is revocable where revocation is meaningful.

## 3. AI & automation

When a system acts on the user's behalf, the user must stay in the loop for anything that leaves the screen or affects others.

- AI output is draft until the user accepts — preview, edit, regenerate, and discard are distinct actions.
- Generated text, code, email, or report does not auto-commit to send, publish, charge, delete, or durable data without explicit approval when stakes are real.
- Automation states are visible: pending, running, completed, failed, skipped, cancelled — with pause, cancel, and undo when stakes justify.
- History and logs for actions that affect others or durable data; user vs system/automation actions are distinguishable.

## 4. Permissions & billing

Money and access are where trust breaks fastest — surprise cost or opaque permission prompts erode confidence in everything else.

- Smallest permission for the current task, in context, after value is visible.
- Permission prompts explain what access enables in user terms — "Allow access" alone is not enough.
- Price, interval, renewal, tax/fees, and cancellation effects visible before purchase.
- Limits that create surprise cost are not hidden; warn before trial converts or quota is exceeded.
- Cost, effort, risk, and limits are not buried behind friendly copy — respect beats conversion pressure.

## 5. Imports & bulk changes

Bulk operations multiply blast radius — one mistaken click can affect hundreds of records, so preview and scope are non-negotiable.

- Preview imports and bulk changes before mutating durable data.
- Partial failure shows scope ("3 of 5 files uploaded — retry failed files").

## 6. Quick checklist

For any action that sends, charges, shares, or mutates data others can see — ask whether the user would feel blindsided if it happened while they looked away.

- [ ] Is external impact previewed before it happens?
- [ ] Is consent granular and revocable?
- [ ] Does AI/automation require explicit approval for high-stakes actions?
- [ ] Are price, limits, and renewal clear before payment?
- [ ] Can the user see what automation did and undo when appropriate?
