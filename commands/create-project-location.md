---
name: create-project-location
description: Create a project-locations skill that maps absolute paths of main projects in the current workspace.
---

Generate `.agents/skills/project-locations/SKILL.md` for this workspace so agents use absolute project paths consistently.

## Steps

1. Identify main projects (user list, or discover via `package.json` / `.git` / framework configs). Per project: name, absolute path, type/framework, 2–3 key files (never secrets/env files).
2. Confirm with the user if discovery is ambiguous.
3. Write/overwrite `.agents/skills/project-locations/SKILL.md` using the template below.
4. Confirm the full path and the projects included.

## Generated skill template

```markdown
---
name: project-locations
description: Provides absolute paths to the main projects in this workspace. Use this skill when you need to reference, read, write, or execute files in any of the listed projects.
---

# Project Locations Reference

## Project Paths

1. **{{name}}** ({{type}})
   - Path: `{{absolutePath}}`
   - Type: {{description}}
   - Key files: {{keyFiles}}

## Usage

When referencing these projects, use the absolute paths above.

## Rules

- **MUST**: Use the absolute paths listed here for file operations in these projects.
- **MUST**: Use `working_directory` (or equivalent) instead of `cd` when running commands in a project.
- **NEVER**: Use relative paths when referring to these projects.
- **NEVER**: Assume cwd is inside a listed project unless confirmed.
```

## Rules

- **MUST** store at `.agents/skills/project-locations/SKILL.md`
- **MUST** use absolute paths only
- **NEVER** list secrets, credentials, or env files as key files

User Request:
