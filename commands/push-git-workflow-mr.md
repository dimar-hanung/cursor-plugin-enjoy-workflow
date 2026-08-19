---
name: push-git-workflow-mr
description: Git push / MR only (git only, HTTP). Creates `.branch` when missing and includes it in the push. Pushes a feature branch and gives a GitLab MR URL — never merge into development or production.
---

# Push Git Workflow (MR only)

**Git only** — no `glab`, no GitLab API, **HTTP/HTTPS only** (no SSH). Push a feature branch and give a **GitLab MR URL** derived from `git remote get-url origin`. **Never** `git merge` into `{{dev-branch}}` or `{{prod-branch}}`, and never push those branches.


## Before starting — resolve branch names

Resolve `{{prod-branch}}` and optionally `{{dev-branch}}` from `.branch` or the user (see below). For `{{feature-name}}`: use what the user gave; otherwise pick a kebab-case slug yourself, reuse the same slug for all work on one project (check current or existing `feature/dev/` / `feature/prod/` branches first). Do not store `{{feature-name}}` in `.branch`.

### 1. Check `.branch` in the repo root

Look for `.branch` at the repository root (same directory as `.git`). If it exists, parse it and use those values — do **not** ask the user for branch names.

**Format** — one branch per line, `key: value` (whitespace around `:` is OK):

```text
production: master
development: development
```

| Key | Maps to | Required |
|-----|---------|----------|
| `production` | `{{prod-branch}}` | Yes |
| `development` | `{{dev-branch}}` | No — omit for prod-only repos |

**Prod-only example** (no development branch):

```text
production: main
```

Treat `development` as absent when the key is missing, blank, `none`, or `n/a` (case-insensitive).

**Parse in shell:**

```bash
BRANCH_FILE=".branch"

if [[ -f "$BRANCH_FILE" ]]; then
  PROD_BRANCH=$(grep -iE '^production\s*:' "$BRANCH_FILE" | head -1 | sed -E 's/^[^:]*:\s*//')
  DEV_BRANCH=$(grep -iE '^development\s*:' "$BRANCH_FILE" | head -1 | sed -E 's/^[^:]*:\s*//')
  # Prod-only when development line is missing or empty/none/n/a
  if [[ -z "$DEV_BRANCH" || "$DEV_BRANCH" =~ ^(none|n/a)$ ]]; then
    DEV_BRANCH=""
  fi
fi
```

After parsing, confirm values with the user in one short line, e.g. *"Using production: `master`, development: `development` (from `.branch`)."* For prod-only: *"Using production: `main` only — no development branch (from `.branch`)."*

If `.branch` exists but `production` is missing or blank, ask the user for `{{prod-branch}}` (and optionally `{{dev-branch}}`) — do not guess. Then write or update `.branch` with the answers (same format as below) and include that file in the commits that get pushed.

### 2. If no `.branch` file — ask the user, create `.branch`, include it in the push

Use **AskQuestion** when available:

1. **Production branch** — required (e.g. `main`, `master`, `production`).
2. **Development branch** — optional. Offer an explicit **"None — production only"** option.

If the user chooses prod-only, set `{{dev-branch}}` empty and follow the **prod-only path** below.

| Variable | Description | Example |
|----------|-------------|---------|
| `{{prod-branch}}` | Production / release target branch | `main`, `master`, `production` |
| `{{dev-branch}}` | Development integration branch (optional) | `development`, `develop`, `dev` |

**After the user answers**, create `.branch` in the repo root with **only** `production` and `development` — never put `{{feature-name}}` in `.branch`.

**Dev + prod:**

```bash
cat > .branch <<EOF
production: {{prod-branch}}
development: {{dev-branch}}
EOF
```

**Prod-only** (omit the `development` line):

```bash
cat > .branch <<EOF
production: {{prod-branch}}
EOF
```

Tell the user briefly that `.branch` was created. **Include `.branch` in the commits that get pushed** in this workflow (stage it with the feature commits). Same rule when `.branch` was missing/`production` blank and you create or update it in section 1 — do not leave it as a local-only untracked file.

### 3. Workflow mode

| Mode | When | Feature branch | MR target |
|------|------|----------------|-----------|
| **Dev + prod** | `{{dev-branch}}` is set | `feature/dev/{{feature-name}}` | `{{dev-branch}}` |
| **Prod-only** | `{{dev-branch}}` is empty | `feature/prod/{{feature-name}}` | `{{prod-branch}}` |

Confirm `origin` at runtime with `git remote get-url origin`. Never assume host, group, or project path.

Replace `{{feature-name}}` with the resolved slug.

## Build MR URL from remote

Always read the remote URL at runtime (do not hardcode):

```bash
git remote get-url origin
```

Convert the HTTP/HTTPS remote URL to the project web base, then append the GitLab new-MR path.

| Remote format | Web base |
|---------------|----------|
| `http(s)://host/group/project.git` | `http(s)://host/group/project` |

If `origin` uses SSH (`git@host:...`), stop and tell the user to switch to HTTP first. Show the conversion pattern — do not invent a URL:

```
git@host:group/project.git  →  http://host/group/project.git
```

The user must run `git remote set-url origin {{http-url}}` with the correct HTTP URL for their project.

**MR URL template:**

```
{{web_base}}/-/merge_requests/new?merge_request[source_branch]={{source_branch}}&merge_request[target_branch]={{target_branch}}
```

Build the URL in shell (URL-encode branch names):

```bash
REMOTE=$(git remote get-url origin)
SOURCE_BRANCH="{{source_branch}}"
TARGET_BRANCH="{{target_branch}}"

if [[ ! "$REMOTE" =~ ^https?:// ]]; then
  echo "Error: origin must use HTTP/HTTPS, not SSH."
  echo "Convert: git@host:group/project.git → http://host/group/project.git"
  echo "Then run: git remote set-url origin http://{{host}}/{{group}}/{{project}}.git"
  exit 1
fi

WEB_BASE="${REMOTE%.git}"

SOURCE_ENC=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$SOURCE_BRANCH'))")
TARGET_ENC=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$TARGET_BRANCH'))")

MR_URL="${WEB_BASE}/-/merge_requests/new?merge_request%5Bsource_branch%5D=${SOURCE_ENC}&merge_request%5Btarget_branch%5D=${TARGET_ENC}"
echo "$MR_URL"
```

Present the MR URL to the user as a clickable markdown link. Do **not** push to or merge into the MR target branch locally.

## Push and create MR

**Dev + prod path** (when `{{dev-branch}}` is set):

3. Checkout `{{dev-branch}}`, `git pull origin {{dev-branch}}`
4. Create branch `feature/dev/{{feature-name}}` and commit changes
5. Push `feature/dev/{{feature-name}}` and output MR URL → `{{dev-branch}}`

**Prod-only path** (when `{{dev-branch}}` is empty):

3. Checkout `{{prod-branch}}`, `git pull origin {{prod-branch}}`
4. Create branch `feature/prod/{{feature-name}}` and commit changes (or cherry-pick from the user's current feature branch if they already have commits elsewhere)
5. Push `feature/prod/{{feature-name}}` and output MR URL → `{{prod-branch}}`

Do **not** cherry-pick onto a production feature branch in this command. For that, use `/push-git-workflow`.

## Workflow checklist

```
- [ ] Step 1: Set git identity (user.name and user.email) for this repo
- [ ] Step 2: Check git credentials — stop if not available
- [ ] Step 3: Sync target branch ({{dev-branch}} if set, else {{prod-branch}})
- [ ] Step 4: Create feature branch and commit
- [ ] Step 5: Push feature branch, pre-check conflicts, output MR URL — never merge the target
```

## Step 1 — Set git identity (required)

**Allowed exception:** for this workflow, local `git config` (identity + credential helper when Step 2 needs it) is **explicitly allowed** — do not skip Step 1 because of a general "never update git config" rule.

Before any commit in this workflow, set the local repo identity:

```bash
git config user.name "Dimar Hanung"
git config user.email "dimarhanung@ecampus.ut.ac.id"
```

Verify:

```bash
git config user.name
git config user.email
```

Use **local** config for identity (no `--global`) so only the current repository is affected. Credential helper may use `--global` only as documented in Step 2 when fixing auth.

## Step 2 — Check credentials (required first)

Before any pull or push, verify `origin` uses **HTTP/HTTPS** and git can authenticate. **Stop the workflow** if the remote is SSH or credentials are missing — tell the user to fix it first.

```bash
git remote get-url origin
git ls-remote origin HEAD
```

**Remote must be HTTP/HTTPS.** If URL starts with `git@`, stop and tell the user to convert to HTTP:

```bash
# User provides the correct HTTP URL for their project
git remote set-url origin http://{{host}}/{{group}}/{{project}}.git
```

**Credentials OK** — `git ls-remote` exits 0 and prints a commit SHA.

**Credentials missing** — non-zero exit with errors such as:
- `Authentication failed`
- `could not read Username`
- `HTTP Basic: Access denied`
- `403` / `401`

If the check fails, report the error and give the setup steps below. Do **not** continue to Step 3.
and tell the user to run `git ls-remote origin HEAD` again after the user confirms credentials are set.

### Set up HTTP credentials

1. Create a **Personal Access Token** in GitLab: Profile → Preferences → Access Tokens (`read_repository`, `write_repository`).
2. Enable a credential helper:
   ```bash
   git config --global credential.helper 'cache --timeout=28800'
   ```
3. Store credentials on first use — run in terminal (agent cannot enter interactive prompts):
   ```bash
   git ls-remote origin HEAD
   ```
   - **Username:** GitLab username
   - **Password:** Personal Access Token (not account password)
4. Or store in `~/.git-credentials` (user sets manually):
   ```
   http://{{username}}:{{token}}@{{host}}
   ```
   Derive `{{host}}` from `git remote get-url origin`. Example: remote `http://git.example.com/group/project.git` → host `git.example.com`.
   ```bash
   git config --global credential.helper store
   ```

Tell the user: *"Git credentials are not configured. Set the remote to HTTP, add your GitLab token and credential helper, then re-run the workflow."*

Re-run `git ls-remote origin HEAD` after the user confirms credentials are set. Only then proceed to Step 3.

## Conflict handling (required)

Conflicts can appear during **pull** (step 3) or **pre-check against the MR target** (step 5). After every pull, check for conflicts before continuing.

### 1. Detect conflicts

```bash
git status
```

Conflict signals: `Unmerged paths`, `both modified`, `CONFLICT`, or a non-zero exit from `git pull` / `git merge`.

List conflicted files:

```bash
git diff --name-only --diff-filter=U
```

### 2. Explain the conflict to the user

For each conflicted file, read the conflict markers and summarize in plain language:

- **File path**
- **What changed on the current branch** (HEAD / ours)
- **What changed on the incoming side** (theirs)
- **Why they clash** (same lines edited differently, one side deleted while the other edited, etc.)

Show the conflicting hunks when helpful:

```bash
git diff {{file}}
```

Do **not** resolve or commit conflict fixes until the user chooses how to proceed.

### 3. Ask the user how to resolve

Use **AskQuestion** when available. One question per conflicted file (or one grouped question if files are closely related).

**Standard options:**

| Option | Meaning |
|--------|---------|
| **Keep ours (current branch)** | Keep HEAD version; discard incoming changes for this file |
| **Keep theirs (incoming)** | Take the incoming version; discard current branch changes for this file |
| **Manual merge** | Agent combines both sides intelligently based on user guidance in chat |
| **Abort operation** | `git merge --abort` — stop and return to pre-conflict state |

Adapt labels to context:

- During **pull** (step 3): "ours" = local target branch; "theirs" = `origin`
- During **pre-check** (step 5): "ours" = MR target; "theirs" = the feature branch

### 4. Apply the chosen resolution

```bash
# Keep ours
git checkout --ours -- {{file}}

# Keep theirs
git checkout --theirs -- {{file}}

# Manual merge: edit file, remove conflict markers, then:
git add {{file}}
```

After all files are resolved:

```bash
git add {{resolved-files}}
git commit                   # if merge paused for conflict resolution
```

If the user chose **Abort**:

```bash
git merge --abort
```

Report the final state (`git status`) and continue the workflow only when the working tree is clean.

## Step 3 — Sync target branch

```bash
# Dev + prod
git checkout {{dev-branch}}
git pull origin {{dev-branch}}

# Prod-only
git checkout {{prod-branch}}
git pull origin {{prod-branch}}
```

## Step 4 — Create feature branch and commit

**Dev + prod** — branch from up-to-date `{{dev-branch}}`:

```bash
git checkout -b feature/dev/{{feature-name}}
# make and commit changes (if `.branch` was created/updated this run, stage it too)
git add .branch   # when newly created or updated
```

**Prod-only** — branch from up-to-date `{{prod-branch}}`:

```bash
git checkout -b feature/prod/{{feature-name}}
# make and commit changes (or cherry-pick from another local branch if the user already has work elsewhere)
git add .branch   # when newly created or updated
```

## Step 5 — Push feature branch and create MR

Pre-check that the feature branch merges cleanly **into** the MR target (dry-run only — do not push the target):

```bash
git fetch origin {{target_branch}}
CURRENT_BRANCH=$(git branch --show-current)

git checkout {{target_branch}}
git pull origin {{target_branch}}
git merge --no-commit --no-ff {{source_branch}}
# exit 0 = no conflicts → abort dry-run
git merge --abort
git checkout "$CURRENT_BRANCH"
```

Use `{{source_branch}}` / `{{target_branch}}` from workflow mode (`feature/dev/...` → `{{dev-branch}}`, or `feature/prod/...` → `{{prod-branch}}`).

**If pre-check reports conflicts** — stop, explain, ask user. Do not push or open MR until resolved.

When the pre-check passes, push the feature branch only:

```bash
git push -u origin {{source_branch}}
```

Build the MR URL from `git remote get-url origin` (see **Build MR URL from remote**) and give it to the user:

```
Source: {{source_branch}}
Target: {{target_branch}}
MR URL: {{built_url}}
```

**Do not** `git checkout` the target to merge, `git merge` into the target, or `git push origin {{target_branch}}` / `git push origin {{dev-branch}}` / `git push origin {{prod-branch}}`. The user creates and merges the MR in GitLab.

## Rules

- Read `.branch` from the repo root first; only ask the user for branch names when the file is missing or `production` is not set — then create or update `.branch` (production and development only) and **include it in the push** (stage/commit with the feature branch work).
- `{{dev-branch}}` is optional — prod-only repos MR `feature/prod/{{feature-name}}` → `{{prod-branch}}`.
- When `{{dev-branch}}` is set, MR `feature/dev/{{feature-name}}` → `{{dev-branch}}` only. Do not create `feature/prod`, cherry-pick, or open an MR to `{{prod-branch}}` in this command.
- `{{feature-name}}`: use user's slug if given; otherwise recommend one and reuse it for the same project.
- Always run **Step 1** (git identity) before any commit; use `Dimar Hanung` / `dimarhanung@ecampus.ut.ac.id` via local `git config`. User confirmed local (and Step 2 credential-helper) `git config` is allowed for this command.
- Always run **Step 2** (credential check) before any pull or push. Stop and instruct the user if credentials are unavailable or remote uses SSH.
- Use **HTTP/HTTPS remote only** — if `origin` is SSH, tell the user to convert and run `git remote set-url origin http://...` (user provides the correct URL).
- Never force-push `{{dev-branch}}` or `{{prod-branch}}`.
- Never push to or merge into `{{dev-branch}}` or `{{prod-branch}}` locally — only push the feature branch and provide the MR URL.
- Build MR URLs from `git remote get-url origin` at runtime — never hardcode the host or project path.
- On any conflict: detect → explain → ask user with choices → apply → confirm clean state.
- Do not auto-resolve conflicts or commit unless the user explicitly chooses a resolution.
- Do not commit unless the user explicitly asks (exception: committing a newly created/updated `.branch` as part of this workflow's feature commits).

USER REQUEST:
