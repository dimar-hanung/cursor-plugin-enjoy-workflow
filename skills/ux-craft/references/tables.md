# Data Tables & Lists

Open this file when building or reviewing data tables, lists, dashboards, sorting, filtering, bulk actions, or responsive table layouts.

## Contents

- Alignment & formatting
- Row structure
- Sort, filter, pagination
- Row & bulk actions
- Loading & empty states
- Responsive
- Quick checklist

## 1. Alignment & formatting

Tables are read by scanning columns, not by reading rows like prose — alignment and numeric formatting determine whether that scan works.

- Left-align text, right-align numbers; header aligns with its column.
- Body cells are never center-aligned — it breaks scanning.
- `font-variant-numeric: tabular-nums` on all numeric columns so digits line up.
- Format numbers: thousands separators, consistent decimal places per column, units in the header ("Revenue (USD)") not repeated per cell.
- Relative time for recent ("2h ago") with absolute on hover/title; absolute for records (see writing.md for formats).
- Truncate long text with `title`/tooltip. IDs get room or a copy affordance — never wrap or truncate mid-value.

## 2. Row structure

Each row is a unit of comparison — its shape should make identity, density, and the primary action obvious at a glance.

- Table surface remains visibly distinct from the page background through a small hue or value shift; use a restrained hairline or elevation when the shift alone is insufficient.
- Primary identifying column first; it is the row's link/click target.
- One row = one entity; if a row needs paragraphs, it wants a detail view, not a wider row.
- Density by job: compact for operators scanning hundreds of rows, comfortable for a handful of rich rows.
- Sticky header on scroll; sticky first column only when horizontally scrolling wide tables.
- Hairline row dividers or spacing first; zebra-stripe only when rows are dense and hard to track.

## 3. Sort, filter, pagination

Users return to tables to find things again — state must be visible, shareable, and recoverable after refresh.

- Meaningful default sort (newest first, highest priority first) with visible sorted column.
- Sort, filter, and page state in the URL — shareable and refresh-safe.
- Active filters as removable chips with a "clear all".
- Pagination for reference data users return to; infinite scroll only for feeds nobody re-finds — not for tables with a footer.
- Total count visible ("128 results") — it is orientation, not decoration.

## 4. Row & bulk actions

Row-level actions compete for attention with the data itself — keep the row clean and push secondary work into predictable overflow patterns.

- One primary action on row click; the rest in a trailing overflow menu.
- Overflow menu with labeled items instead of four or more icon buttons per row.
- Destructive actions separated inside the menu (divider + red on the item only).
- Bulk actions via leading checkboxes: selection reveals an action bar with count ("3 selected") and applicable actions; support select-all-across-pages explicitly.

## 5. Loading & empty states

A table with no rows or no data yet is still a table — filters, headers, and next steps should remain usable.

- Skeleton rows matching column layout while loading — not a spinner in a void.
- Three distinct non-happy states: first-use empty (what this is + CTA), no-results (show the query/filters + how to loosen), error (what failed + retry).
- Header and filters stay visible in every state so users can act.

## 6. Responsive

Mobile is not a shrunk desktop table — pick a layout that preserves the job-to-be-done, not every column.

- Deliberate choice on small screens: card-per-row layout, column-priority (hide low-value columns first), or a dedicated mobile list.
- A nine-column table squeezed into horizontal scroll alone is not a mobile strategy.

## 7. Quick checklist

Load the table with zero rows, one row, many rows, and a failed fetch — each state should still orient the user.

- [ ] Text left, numbers right with tabular nums?
- [ ] Is the table surface visibly distinct from the page background?
- [ ] Is default sort obvious and is state in the URL?
- [ ] Are row actions in overflow when there are more than a few?
- [ ] Do loading and empty states match the final layout?
- [ ] Is there a real mobile layout strategy?
