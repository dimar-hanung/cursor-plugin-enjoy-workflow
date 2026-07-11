---
name: tidy-env
description: Repositions existing .env entries into a sectioned layout (header, # Section groups, blank lines, optional ENV-LOCAL). Does not rename, add, or invent env keys. Use when the user asks to tidy, clean, organize, format, or restructure a .env / .env.example / .env.local file.
disable-model-invocation: true
---

# Tidy Env

**Scope: positioning only.** Reorder and regroup keys that already exist in the file. Never rename a key, never add a new key, never invent a missing key, never change a value (unless the user explicitly asks).

## Target format

```dotenv
# <project> — <one-line purpose>
# <optional usage note>

# General
EXISTING_MODE_KEY=development

# GraphQL
EXISTING_GRAPHQL_KEY=https://example.com/graphql

# REST
EXISTING_REST_KEY=https://example.com/rest
# EXISTING_OPTIONAL_KEY=https://example.com/internal

# =============================================================================
# ENV-LOCAL — uncomment for local backends
# =============================================================================
# EXISTING_GRAPHQL_KEY=http://localhost:3901/graphql
```

(Keys above are placeholders — use the real keys already present in the file.)

## Hard constraints

- **Do not** rename any `KEY`
- **Do not** create / add any new `KEY=` line that was not already in the file (active or commented)
- **Do not** change values
- **Do not** drop keys (including commented `# KEY=value` lines)
- **Do** move lines, add `# Section` comments, blank lines, and header/ENV-LOCAL banners

## Rules

1. **Header** — `# <project> — <purpose>`, optional usage note, then a blank line.
2. **Sections** — group *existing* related keys under `# Section Name`. One blank line between sections; none inside a section.
3. **Assignment** — keep `KEY=value` with no spaces around `=`. Empty stays `KEY=`.
4. **Comments** — keep `# KEY=value` as-is; place next to its section or in ENV-LOCAL if it is a local override line already in the file.
5. **Order** — reposition keys into sections; preserve relative order within a section when possible.
6. **ENV-LOCAL** — only if local-override lines already exist (or user asks to gather existing ones into a bottom banner):

   ```dotenv
   # =============================================================================
   # ENV-LOCAL — <short instruction>
   # =============================================================================
   # KEY=http://localhost:...
   ```

7. **Secrets** — never commit `.env`; tidy on disk only when asked.

## Workflow

1. Read the file; collect every existing key (active + commented) — this set is frozen.
2. Group those keys under short `# Section` labels (reuse labels already in the file when present).
3. Rewrite layout only: header → sections → optional ENV-LOCAL.
4. Verify: same key set, same values; only positions/comments/whitespace changed.
5. Summarize: which keys moved under which section; confirm no keys added/renamed.

## Grouping hint

Section comments are labels for *placement* of existing keys only — never a list of keys to create.

1. Reuse `# Section` labels already in the file when they still fit.
2. Otherwise group by domain from the key name / value role, e.g.:
   - App / mode / feature flags
   - Auth / SSO / tokens
   - API / GraphQL / REST bases
   - Storage / CDN / assets
   - Monitoring / Sentry / analytics
   - Timeouts / session
   - Third-party integrations (one section per service when several keys share a prefix)
3. Prefer short section titles; match the project's language if labels already exist.
4. Unmatched keys: nearest related section, or a short new `# Section` — still do not invent keys.

## Example trigger

User: "Tidy up `.env`"

Agent: reposition existing entries into header + sections (+ ENV-LOCAL if those lines already exist); report moves only — no new/renamed keys.
