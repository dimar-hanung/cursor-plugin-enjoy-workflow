---
name: push-git-workflow
description: Pushes changes through a dev-then-prod Git workflow using git commands only (no glab or GitLab API). Sets local git identity (Dimar Hanung / dimarhanung@ecampus.ut.ac.id) before commits. Checks git credentials and remote origin at runtime; uses user-provided development and production branch names. Merges feature/dev into the dev branch locally; pushes feature/prod and opens a GitLab MR to the production branch via URL built from git remote. Detects merge/cherry-pick conflicts, explains them, and asks the user how to resolve. Use when the user asks to push changes, create a merge request (MR), merge to development or production, cherry-pick to production, resolve git conflicts, or follow the push-git workflow.
---

# Push Git Workflow

**Git only** — no `glab`, no GitLab API, **HTTP/HTTPS only** (no SSH). Step 6 merges to the dev branch via `git merge`. Step 9 pushes `feature/prod` and gives a **GitLab MR URL** derived from `git remote get-url origin` — never auto-merge or push to the production branch.

## Before starting — gather from user

Ask the user for these values **before** running the workflow (do not hardcode them):

| Variable | Description | Example |
|----------|-------------|---------|
| `{dev-branch}` | Development integration branch | `development`, `develop`, `dev` |
| `{prod-branch}` | Production / release target branch | `main`, `master`, `production` |
| `{feature-name}` | Short kebab-case slug for the feature | `chat-agent-analytics` |

Confirm `origin` at runtime with `git remote get-url origin`. Never assume host, group, or project path.

Replace `{feature-name}` with the user-provided slug on both `feature/dev/` and `feature/prod/` branches.

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

4. Go to dev branch. Pull origin `{dev-branch}`
5. Create branch `feature/dev/{feature-name}`
6. Merge to `{dev-branch}`
7. Checkout `{prod-branch}`, `git pull origin {prod-branch}`
8. Create branch `feature/prod/{feature-name}`
9. Cherry-pick from merged `feature/dev/{feature-name}`

## Workflow checklist

```
- [ ] Step 1: Confirm {dev-branch}, {prod-branch}, {feature-name} with user
- [ ] Step 2: Set git identity (user.name and user.email) for this repo
- [ ] Step 3: Check git credentials — stop if not available
- [ ] Step 4: Sync {dev-branch}
- [ ] Step 5: Create feature/dev branch and commit
- [ ] Step 6: Push feature/dev, git merge into {dev-branch}, push — auto if no conflict
- [ ] Step 7: Sync {prod-branch}
- [ ] Step 8: Create feature/prod branch
- [ ] Step 9: Cherry-pick dev commits, push feature/prod, pre-check conflicts, output MR URL → {prod-branch}
```

## Step 2 — Set git identity (required)

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

## Step 3 — Check credentials (required first)

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

If the check fails, report the error and give the setup steps below. Do **not** continue to Step 4.

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

Re-run `git ls-remote origin HEAD` after the user confirms credentials are set. Only then proceed to Step 4.

## Conflict handling (required)

Conflicts can appear during **pull** (steps 4, 7), **merge to dev branch** (step 6), **cherry-pick** (step 9), or **pre-check against prod branch** (step 9). After every pull, merge, or cherry-pick, check for conflicts before continuing.

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

- During **cherry-pick** (step 9): "ours" = `feature/prod` base on `{prod-branch}`; "theirs" = the cherry-picked dev commit
- During **merge to dev branch** (step 6): "ours" = `{dev-branch}`; "theirs" = `feature/dev/{feature-name}`

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

## Step 4 — Sync dev branch

```bash
git checkout {dev-branch}
git pull origin {dev-branch}
```

## Step 5 — Create feature/dev branch

Branch from up-to-date `{dev-branch}`:

```bash
git checkout -b feature/dev/{feature-name}
# make and commit changes
git push -u origin feature/dev/{feature-name}
```

## Step 6 — Merge to dev branch

Push the branch, merge into `{dev-branch}` locally, and push. **Auto-complete when `git merge` has no conflicts.**

```bash
# 1. Push feature branch
git push -u origin feature/dev/{feature-name}

# 2. Record commit SHAs (needed for step 9 cherry-pick)
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

## Step 7 — Sync prod branch

```bash
git checkout {prod-branch}
git pull origin {prod-branch}
```

## Step 8 — Create feature/prod branch

```bash
git checkout -b feature/prod/{feature-name}
```

## Step 9 — Cherry-pick and create MR to prod branch

Cherry-pick the commit(s) recorded in step 6 onto `feature/prod/{feature-name}`:

```bash
# single commit
git cherry-pick <commit-sha>

# or range (oldest..newest)
git cherry-pick <oldest-sha>^..<newest-sha>
```

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

- Ask for `{dev-branch}` and `{prod-branch}` before starting — never assume `development` or `main`.
- Always run **Step 2** (git identity) before any commit; use `Dimar Hanung` / `dimarhanung@ecampus.ut.ac.id` via local `git config`.
- Always run **Step 3** (credential check) before any pull or push. Stop and instruct the user if credentials are unavailable or remote uses SSH.
- Use **HTTP/HTTPS remote only** — if `origin` is SSH, tell the user to convert and run `git remote set-url origin http://...` (user provides the correct URL).
- Never force-push `{dev-branch}` or `{prod-branch}`.
- Never push to or merge into `{prod-branch}` locally — only push `feature/prod` and provide the MR URL.
- Use the same `{feature-name}` slug on both `feature/dev/` and `feature/prod/` branches.
- Only cherry-pick after feature/dev is merged into `{dev-branch}`.
- Auto-push to `{dev-branch}` only when step 6 `git merge` has no conflicts.
- Build MR URLs from `git remote get-url origin` at runtime — never hardcode the host or project path.
- On any conflict: detect → explain → ask user with choices → apply → confirm clean state.
- Do not auto-resolve conflicts or commit unless the user explicitly chooses a resolution.
- Do not commit unless the user explicitly asks (merge commits to `{dev-branch}` in step 6 are the exception when auto-merging).
