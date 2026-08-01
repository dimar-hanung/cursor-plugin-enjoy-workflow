---
name: push-git-workflow
description: Pushes changes through a dev-then-prod Git workflow using git commands only (no glab or GitLab API). Sets local git identity (Dimar Hanung / dimarhanung@ecampus.ut.ac.id) before commits. Checks git credentials and remote origin at runtime. Reads production and development branch names from a `.branch` file in the repo root when present; otherwise asks the user and creates `.branch` (feature slug is separate — recommend and reuse per project if user did not provide one). Prod-only repos skip the dev path. Merges feature/dev into the dev branch locally when a development branch exists; pushes feature/prod and opens a GitLab MR to the production branch via URL built from git remote. Detects merge/cherry-pick conflicts, explains them, and asks the user how to resolve. Use when the user asks to push changes, create a merge request (MR), merge to development or production, cherry-pick to production, resolve git conflicts, or follow the push-git workflow.
---

# Push Git Workflow

**Git only** — no `glab`, no GitLab API, **HTTP/HTTPS only** (no SSH). When a development branch exists, step 5 merges to it via `git merge`. Step 8 pushes `feature/prod` and gives a **GitLab MR URL** derived from `git remote get-url origin` — never auto-merge or push to the production branch. Prod-only repos skip the dev path (steps 3–5).

## Before starting — resolve branch names

Resolve `{prod-branch}` and optionally `{dev-branch}` from `.branch` or the user (see below). For `{feature-name}`: use what the user gave; otherwise pick a kebab-case slug yourself, reuse the same slug for all work on one project (check current or existing `feature/dev/` / `feature/prod/` branches first). Do not store `{feature-name}` in `.branch`.

### 1. Check `.branch` in the repo root

Look for `.branch` at the repository root (same directory as `.git`). If it exists, parse it and use those values — do **not** ask the user for branch names.

**Format** — one branch per line, `key: value` (whitespace around `:` is OK):

```text
production: master
development: development
```

| Key | Maps to | Required |
|-----|---------|----------|
| `production` | `{prod-branch}` | Yes |
| `development` | `{dev-branch}` | No — omit for prod-only repos |

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

If `.branch` exists but `production` is missing or blank, ask the user for `{prod-branch}` (and optionally `{dev-branch}`) — do not guess. Then write or update `.branch` with the answers (same format as below).

### 2. If no `.branch` file — ask the user, then create `.branch`

Use **AskQuestion** when available:

1. **Production branch** — required (e.g. `main`, `master`, `production`).
2. **Development branch** — optional. Offer an explicit **"None — production only"** option.

If the user chooses prod-only, set `{dev-branch}` empty and follow the **prod-only path** below.

| Variable | Description | Example |
|----------|-------------|---------|
| `{prod-branch}` | Production / release target branch | `main`, `master`, `production` |
| `{dev-branch}` | Development integration branch (optional) | `development`, `develop`, `dev` |

**After the user answers**, create `.branch` in the repo root with **only** `production` and `development` — never put `{feature-name}` in `.branch`.

**Dev + prod:**

```bash
cat > .branch <<EOF
production: {prod-branch}
development: {dev-branch}
EOF
```

**Prod-only** (omit the `development` line):

```bash
cat > .branch <<EOF
production: {prod-branch}
EOF
```

Tell the user briefly that `.branch` was created. Do **not** commit `.branch` unless the user asks — only create the file locally.

### 3. Workflow mode

| Mode | When | Steps |
|------|------|-------|
| **Dev + prod** | `{dev-branch}` is set | Full checklist (steps 3–8) |
| **Prod-only** | `{dev-branch}` is empty | Skip steps 3–5; start at step 6 |

Confirm `origin` at runtime with `git remote get-url origin`. Never assume host, group, or project path.

Replace `{feature-name}` with the resolved slug on `feature/prod/{feature-name}` (and on `feature/dev/{feature-name}` when using the dev path).

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

The user must run `git remote set-url origin <http-url>` with the correct HTTP URL for their project.

**MR URL template:**

```
{web_base}/-/merge_requests/new?merge_request[source_branch]={source_branch}&merge_request[target_branch]={prod-branch}
```

Build the URL in shell (URL-encode branch names):

```bash
REMOTE=$(git remote get-url origin)
SOURCE_BRANCH="feature/prod/{feature-name}"
TARGET_BRANCH="{prod-branch}"

if [[ ! "$REMOTE" =~ ^https?:// ]]; then
  echo "Error: origin must use HTTP/HTTPS, not SSH."
  echo "Convert: git@host:group/project.git → http://host/group/project.git"
  echo "Then run: git remote set-url origin http://<host>/<group>/<project>.git"
  exit 1
fi

WEB_BASE="${REMOTE%.git}"

SOURCE_ENC=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$SOURCE_BRANCH'))")
TARGET_ENC=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$TARGET_BRANCH'))")

MR_URL="${WEB_BASE}/-/merge_requests/new?merge_request%5Bsource_branch%5D=${SOURCE_ENC}&merge_request%5Btarget_branch%5D=${TARGET_ENC}"
echo "$MR_URL"
```

Present the MR URL to the user as a clickable markdown link. Do **not** push to `{prod-branch}` or merge into `{prod-branch}` locally.

## Push and create MR to production

**Dev + prod path** (when `{dev-branch}` is set):

3. Go to dev branch. Pull origin `{dev-branch}`
4. Create branch `feature/dev/{feature-name}`
5. Merge to `{dev-branch}`
6. Checkout `{prod-branch}`, `git pull origin {prod-branch}`
7. Create branch `feature/prod/{feature-name}`
8. Cherry-pick from merged `feature/dev/{feature-name}`

**Prod-only path** (when `{dev-branch}` is empty):

3–5. *Skipped*
6. Checkout `{prod-branch}`, `git pull origin {prod-branch}`
7. Create branch `feature/prod/{feature-name}` and commit changes (or cherry-pick from the user's current feature branch if they already have commits elsewhere)
8. Push `feature/prod/{feature-name}` and output MR URL → `{prod-branch}` (no cherry-pick from dev)

## Workflow checklist

```
- [ ] Step 1: Set git identity (user.name and user.email) for this repo
- [ ] Step 2: Check git credentials — stop if not available
- [ ] Step 3: Sync {dev-branch} (skip if prod-only)
- [ ] Step 4: Create feature/dev branch and commit (skip if prod-only)
- [ ] Step 5: Push feature/dev, git merge into {dev-branch}, push — auto if no conflict (skip if prod-only)
- [ ] Step 6: Sync {prod-branch}
- [ ] Step 7: Create feature/prod branch (commit here if prod-only)
- [ ] Step 8: Cherry-pick dev commits (dev+prod) or push feature/prod (prod-only), pre-check conflicts, output MR URL → {prod-branch}
```

## Step 1 — Set git identity (required)

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

Use **local** config (no `--global`) so only the current repository is affected.

## Step 2 — Check credentials (required first)

Before any pull or push, verify `origin` uses **HTTP/HTTPS** and git can authenticate. **Stop the workflow** if the remote is SSH or credentials are missing — tell the user to fix it first.

```bash
git remote get-url origin
git ls-remote origin HEAD
```

**Remote must be HTTP/HTTPS.** If URL starts with `git@`, stop and tell the user to convert to HTTP:

```bash
# User provides the correct HTTP URL for their project
git remote set-url origin http://<host>/<group>/<project>.git
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
   http://<username>:<token>@<host>
   ```
   Derive `<host>` from `git remote get-url origin`. Example: remote `http://git.example.com/group/project.git` → host `git.example.com`.
   ```bash
   git config --global credential.helper store
   ```

Tell the user: *"Git credentials are not configured. Set the remote to HTTP, add your GitLab token and credential helper, then re-run the workflow."*

Re-run `git ls-remote origin HEAD` after the user confirms credentials are set. Only then proceed to Step 3.

## Conflict handling (required)

Conflicts can appear during **pull** (steps 3, 6), **merge to dev branch** (step 5), **cherry-pick** (step 8), or **pre-check against prod branch** (step 8). After every pull, merge, or cherry-pick, check for conflicts before continuing.

### 1. Detect conflicts

```bash
git status
```

Conflict signals: `Unmerged paths`, `both modified`, `CONFLICT`, or a non-zero exit from `git pull` / `git cherry-pick` / `git merge`.

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
git diff <file>
```

Do **not** resolve or commit conflict fixes until the user chooses how to proceed.

### 3. Ask the user how to resolve

Use **AskQuestion** when available. One question per conflicted file (or one grouped question if files are closely related).

**Standard options:**

| Option | Meaning |
|--------|---------|
| **Keep ours (current branch)** | Keep HEAD version; discard incoming changes for this file |
| **Keep theirs (incoming)** | Take the merged/cherry-picked version; discard current branch changes for this file |
| **Manual merge** | Agent combines both sides intelligently based on user guidance in chat |
| **Abort operation** | `git cherry-pick --abort`, `git merge --abort`, or `git rebase --abort` — stop and return to pre-conflict state |

Adapt labels to context:

- During **cherry-pick** (step 8): "ours" = `feature/prod` base on `{prod-branch}`; "theirs" = the cherry-picked dev commit
- During **merge to dev branch** (step 5): "ours" = `{dev-branch}`; "theirs" = `feature/dev/{feature-name}`

### 4. Apply the chosen resolution

```bash
# Keep ours
git checkout --ours -- <file>

# Keep theirs
git checkout --theirs -- <file>

# Manual merge: edit file, remove conflict markers, then:
git add <file>
```

After all files are resolved:

```bash
git add <resolved-files>
git cherry-pick --continue   # if cherry-picking
git commit                   # if merge (only when merge paused for conflict resolution)
```

If the user chose **Abort**:

```bash
git cherry-pick --abort
git merge --abort
```

Report the final state (`git status`) and continue the workflow only when the working tree is clean.

## Step 3 — Sync dev branch

*Skip this step when `{dev-branch}` is empty (prod-only).*

```bash
git checkout {dev-branch}
git pull origin {dev-branch}
```

## Step 4 — Create feature/dev branch

*Skip this step when `{dev-branch}` is empty (prod-only).*

Branch from up-to-date `{dev-branch}`:

```bash
git checkout -b feature/dev/{feature-name}
# make and commit changes
git push -u origin feature/dev/{feature-name}
```

## Step 5 — Merge to dev branch

*Skip this step when `{dev-branch}` is empty (prod-only).*

Push the branch, merge into `{dev-branch}` locally, and push. **Auto-complete when `git merge` has no conflicts.**

```bash
# 1. Push feature branch
git push -u origin feature/dev/{feature-name}

# 2. Record commit SHAs (needed for step 8 cherry-pick)
git log feature/dev/{feature-name} --oneline

# 3. Merge into dev branch
git checkout {dev-branch}
git pull origin {dev-branch}
git merge --no-ff feature/dev/{feature-name} -m "Merge branch 'feature/dev/{feature-name}' into {dev-branch}"
```

**If merge succeeds (no conflicts)** — push automatically:

```bash
git push origin {dev-branch}
```

**If merge reports conflicts** — stop. Follow **Conflict handling**: explain each conflict, ask the user, resolve, then `git commit` and `git push origin {dev-branch}`.

Optional — delete remote feature branch after merge:

```bash
git push origin --delete feature/dev/{feature-name}
```

## Step 6 — Sync prod branch

```bash
git checkout {prod-branch}
git pull origin {prod-branch}
```

## Step 7 — Create feature/prod branch

```bash
git checkout -b feature/prod/{feature-name}
```

**Prod-only:** make and commit changes on this branch (or cherry-pick commits from another local branch if the user already has work elsewhere). There is no `feature/dev` branch to cherry-pick from.

## Step 8 — Cherry-pick and create MR to prod branch

**Dev + prod:** cherry-pick the commit(s) recorded in step 5 onto `feature/prod/{feature-name}`:

```bash
# single commit
git cherry-pick <commit-sha>

# or range (oldest..newest)
git cherry-pick <oldest-sha>^..<newest-sha>
```

**Prod-only:** skip cherry-pick from dev. Ensure commits are already on `feature/prod/{feature-name}` from step 7, then continue to pre-check and push.

**If cherry-pick conflicts** — stop, explain, ask user (Conflict handling). Continue only after clean cherry-pick.

Pre-check that `feature/prod` merges cleanly **into** `{prod-branch}` (dry-run only — do not push `{prod-branch}`):

```bash
git fetch origin {prod-branch}
CURRENT_BRANCH=$(git branch --show-current)

git checkout {prod-branch}
git pull origin {prod-branch}
git merge --no-commit --no-ff feature/prod/{feature-name}
# exit 0 = no conflicts → abort dry-run
git merge --abort
git checkout "$CURRENT_BRANCH"
```

**If pre-check reports conflicts** — stop, explain, ask user. Do not push or open MR until resolved.

When cherry-pick is clean and pre-check passes, push the feature branch only:

```bash
git push -u origin feature/prod/{feature-name}
```

Build the MR URL from `git remote get-url origin` (see **Build MR URL from remote**) and give it to the user:

```
Source: feature/prod/{feature-name}
Target: {prod-branch}
MR URL: {built_url}
```

**Do not** `git checkout {prod-branch}`, `git merge`, or `git push origin {prod-branch}`. The user creates and merges the MR in GitLab.

## Rules

- Read `.branch` from the repo root first; only ask the user for branch names when the file is missing or `production` is not set — then create or update `.branch` (production and development only; do not commit unless asked).
- `{dev-branch}` is optional — prod-only repos skip steps 3–5 and commit directly on `feature/prod/{feature-name}`.
- `{feature-name}`: use user's slug if given; otherwise recommend one and reuse it for the same project across `feature/dev/` and `feature/prod/`.
- Always run **Step 1** (git identity) before any commit; use `Dimar Hanung` / `dimarhanung@ecampus.ut.ac.id` via local `git config`.
- Always run **Step 2** (credential check) before any pull or push. Stop and instruct the user if credentials are unavailable or remote uses SSH.
- Use **HTTP/HTTPS remote only** — if `origin` is SSH, tell the user to convert and run `git remote set-url origin http://...` (user provides the correct URL).
- Never force-push `{dev-branch}` or `{prod-branch}`.
- Never push to or merge into `{prod-branch}` locally — only push `feature/prod` and provide the MR URL.
- Use the same `{feature-name}` slug on both `feature/dev/` and `feature/prod/` branches when the dev path is used.
- Only cherry-pick from dev after feature/dev is merged into `{dev-branch}` (dev + prod path only).
- Auto-push to `{dev-branch}` only when step 5 `git merge` has no conflicts.
- Build MR URLs from `git remote get-url origin` at runtime — never hardcode the host or project path.
- On any conflict: detect → explain → ask user with choices → apply → confirm clean state.
- Do not auto-resolve conflicts or commit unless the user explicitly chooses a resolution.
- Do not commit unless the user explicitly asks (merge commits to `{dev-branch}` in step 5 are the exception when auto-merging).
