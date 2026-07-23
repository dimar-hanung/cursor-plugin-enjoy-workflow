# Data Tables & Lists

Open when building or reviewing a data table, list view, or dashboard grid.

## Alignment & formatting

- **DO** left-align text, right-align numbers; header aligns with its column.
- **NEVER** center-align body cells — it breaks scanning.
- **DO** `font-variant-numeric: tabular-nums` on all numeric columns so digits line up.
- **DO** format numbers: thousands separators, consistent decimal places per column, units in the header ("Revenue (USD)") not repeated per cell.
- **DO** relative time for recent ("2h ago") with absolute on hover/title; absolute for records (see writing.md for formats).
- **DO** truncate long text with `title`/tooltip. **NEVER** wrap or truncate IDs mid-value — give them room or a copy affordance.

## Structure

- **DO** put the primary identifying column first; make it the row's link/click target.
- **DO** one row = one entity; if a row needs paragraphs, it wants a detail view, not a wider row.
- **DO** pick density by job: compact for operators scanning hundreds of rows, comfortable for a handful of rich rows.
- **DO** sticky header on scroll; sticky first column only when horizontally scrolling wide tables.
- **DON'T** zebra-stripe by default; use it only when rows are dense and hard to track. Hairline row dividers or spacing first.

## Sorting, filtering, pagination

- **DO** ship a meaningful default sort (newest first, highest priority first) and show which column is sorted.
- **DO** keep sort/filter/page state in the URL — shareable and refresh-safe.
- **DO** show active filters as removable chips with a "clear all".
- **DO** pagination for reference data users return to; infinite scroll only for feeds nobody re-finds. **DON'T** infinite-scroll a table with a footer.
- **DO** show total count ("128 results") — it's orientation, not decoration.

## Row & bulk actions

- **DO** one primary action on row click; the rest in a trailing overflow menu.
- **DON'T** stack 4+ icon buttons per row; **DO** overflow menu with labeled items.
- **DO** separate destructive actions inside the menu (divider + red on the item only).
- **DO** bulk actions via leading checkboxes: selection reveals an action bar with count ("3 selected") and applicable actions; support select-all-across-pages explicitly.

## States (see states.md for depth)

- **DO** skeleton rows matching column layout while loading. **DON'T** spinner-in-a-void.
- **DO** design three distinct non-happy states: first-use empty (what this is + CTA), no-results (show the query/filters + how to loosen), error (what failed + retry).
- **DO** keep header and filters visible in every state so users can act.

## Responsive

- **DO** choose deliberately on small screens: card-per-row layout, or column-priority (hide low-value columns first), or a dedicated mobile list.
- **NEVER** shrink a 9-column table into an unreadable horizontal scroll as the only strategy.
