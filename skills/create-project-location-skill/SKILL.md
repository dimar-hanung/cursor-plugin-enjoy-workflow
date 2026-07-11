---
name: create-project-location-skill
description: Guides the creation of a new 'project-locations' skill for a workspace. Use whenever the user wants to document project paths, create a project reference skill, or map out main directories in the current workspace.
---

# Skill: Create Project Location Skill

## Overview

This skill generates a reusable **project-locations** skill for the current workspace. The output is a `SKILL.md` file stored in `.agents/skills/project-locations/` that documents the absolute paths of main projects so agents can reference them consistently.

## When to Use

- The user asks to "create a project locations skill".
- The user wants to document main project paths in the workspace.
- The user provides a list of projects and paths and wants them turned into a skill.

## Instructions

### Step 1: Identify Projects

Determine the main projects in the workspace. For each project, collect:
- **Name**: The project folder or repository name.
- **Absolute Path**: The full path on disk (e.g., `c:\Users\<user>\project\<name>`).
- **Type / Framework**: Brief tech stack (e.g., Nuxt.js, NestJS, Express).
- **Key Files**: 2-3 important files that identify the project (e.g., `package.json`, `src/main.ts`).

### Step 2: Choose Skill Storage Location

Create or overwrite the skill directory inside the **current workspace**:

```
.agents/skills/project-locations/
    └── SKILL.md
```

> The workspace root is the directory where `.agents/` lives or should live.

### Step 3: Generate `SKILL.md`

Use the following template. Replace all `{{placeholders}}` with real values.

```markdown
---
name: project-locations
description: Provides absolute paths to the main projects in this workspace. Use this skill when you need to reference, read, write, or execute files in any of the listed projects.
---

# Project Locations Reference

This skill contains the absolute paths to the main projects in this workspace.

## Project Paths

{{#each projects}}
1. **{{name}}** ({{type}})
   - Path: `{{absolutePath}}`
   - Type: {{description}}
   - Key files: {{keyFiles}}

{{/each}}

## Usage

When referencing any of these projects in file operations, use the absolute paths provided above.

## Rules

- **MUST**: Always use the absolute paths listed in this skill when operating on files in these projects.
- **MUST**: Use the `workdir` parameter (or equivalent) when running commands inside a project directory instead of using `cd`.
- **NEVER**: Use relative paths (e.g., `..\project\name`) when referring to these projects.
- **NEVER**: Assume the current working directory is inside one of these projects unless explicitly confirmed.

## Resources

<Base directory for this skill: file:///{{skillBaseDir}}>
Relative paths in this skill are relative to this base directory.
```

### Step 4: Deliver Confirmation

After writing the file, confirm:
- The full path to the created `SKILL.md`.
- The list of projects included.

## Examples

### Example 1: User provides a template
**User Input:**
> Create Skill for Creating Skill Project Location for this template: [template with 3 projects]

**Action:**
1. Extract project details from the template.
2. Write `.agents/skills/project-locations/SKILL.md` using the template above.
3. Confirm completion.

### Example 2: Discovering projects automatically
**User Input:**
> Create a project locations skill for my workspace.

**Action:**
1. Explore the workspace to find directories containing `package.json`, `.git`, or framework-specific config files.
2. Ask the user to confirm the discovered projects if ambiguous.
3. Generate the skill file.

## Rules

- **MUST**: Store the generated skill in `.agents/skills/project-locations/SKILL.md`.
- **MUST**: Use absolute paths in the generated skill.
- **MUST**: Include at minimum the project name, absolute path, type, and key files.
- **NEVER**: Include secrets, credentials, or environment files in the key files list.
- **NEVER**: Use relative paths in the generated skill content.

## Resources

<Base directory for this skill: file:///C:/Users/dimar/.agents/skills/create-project-location-skill>
Relative paths in this skill are relative to this base directory.
