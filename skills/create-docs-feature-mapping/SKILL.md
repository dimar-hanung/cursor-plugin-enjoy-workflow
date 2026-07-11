---
name: create-docs-feature-mapping
description: Guide for creating a "feature file-map" Docs.
---

# 🧠 Agent Instructions: Creating Docs Files for GitHub Copilot

Here's a comprehensive guide to creating a "feature file-map" Docs that documents all files for a specific feature across frontend and backend projects.
You can use project-locations skill if available.
---

## 📁 1. Choose Where to Store Your Docs

| Scope                              | Path                           |
| ---------------------------------- | ------------------------------ |
| **Per-repository (project-level)** | `docs/<docs-name>.md` |

---

## 🗂️ 2. Create the Directory Structure

Each Docs file lives in its own subdirectory. The key file is `docs/<docs-name>.md`:

```
docs/<docs-name>.md
```

---

## 📝 3. Write the `docs/<docs-name>.md` File

This file uses **YAML frontmatter** for metadata, followed by Markdown for detailed instructions. Here's a skeleton:

```markdown name=docs/<docs-name>.md
---
name: <docs-name>
description: Describe what this docs file does and when Copilot should use it.
---

```


## 📋 Docs Template

Use this template when creating a new docs file for a feature mapping:

```markdown name=docs-name.md
---
name: <docs-name>
description: <One-line description of what this docs file does.>

# {Feature Display Name} File Map

Use this docs file for the {feature display name} feature, which is implemented as "{internal feature name}".

<!-- 
  INSTRUCTIONS FOR FILLING THIS TEMPLATE:
  - If the feature exists only in certain sections of the files, don't mention line numbers. Mention component or method names instead.
  - Replace all {placeholders} with your actual values.
  - If your feature lives in a SINGLE repo, delete the "Separate Module" section
    and remove all "Secondary Feature" references (including rules and searches).
-->

## Files Mapping

### Frontend (`{frontend-project-root}`)

<!-- Delete this entire section if the feature is backend-only. -->

- [{FeatureIndex.vue}](../../project-folder/example.vue) — main {feature} UI
- [{feature}Service.js](../../project-folder/exampleService.js) — state management and API calls

### Backend (`{backend-project-root}`)

<!-- Delete this heading (but keep the list) if the feature is single-project. -->

- [{feature}.route.ts](../../project-folder/{feature}.example.ts) — REST endpoints for {domain objects}
- [{feature}.service.ts](../../project-folder/{feature}.example.ts) — database operations and seeding

### Integration Entry Points

<!-- Delete if single-project or if there's no special wiring. -->

- [{index.ts}](../../project-folder/index.ts) — initializes socket setup and {feature} seeding
- [{features.route.ts}](../../project-folder/features.route.ts) — mounts `/{feature}` routes

## Database Mapping
<!-- Optional: Include if there are specific database tables or schemas related to this feature. If just some columns are relevant, mention them specifically. -->
- **{table_name}**: Description of how this table relates to the feature.

## Expected Response Pattern

1. Frontend {Primary Feature} files
2. Backend {Primary Feature} files
3. Integration and entry-point files

When helpful, mention the main runtime path:

- **Frontend route:** `/{feature-route}`
- **REST base:** `/{api-version}/{feature}/*`
- **Socket namespace:** `/{namespace}`

## Recommended Search Workflow

If you need to verify or expand the list, use fast searches first.

### Filename searches

```bash
# Feature files — adjust paths per your project layout
rg --files {project-root}/src | rg "{FeaturePascal}|{featureCamel}"
```

### Content searches

```bash
# Feature references
rg -n "{feature-kebab}|{FeaturePascal}" {project-root}/src


```





