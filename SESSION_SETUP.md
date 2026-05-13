# PythonAcademy Session Setup

This guide is for students working on their own machines in VS Code.

Repository:
`https://github.com/alientometal/PythonAcademy`

If you are using the provided VDI, follow the instructor workflow for that environment.
If you cannot use the VDI, use this guide for local setup.

## 1. Before the session

Install these tools first:

- Git
- Python 3.10+ or newer
- VS Code
- VS Code extensions:
  - Python
  - Jupyter

Create or confirm access to:

- A GitHub account
- Permission to fork and clone repositories

## 2. Fork the repository

Create your own copy of the course repository so you can save your own notes, notebook runs, and exercises.

1. Open the course repository in GitHub:
   `https://github.com/alientometal/PythonAcademy`
2. Click `Fork`.
3. Create the fork under your own GitHub account.

After this, you should have two repositories:

- `upstream`: the instructor repository
- `origin`: your fork

## 3. Clone your fork to your machine

Clone your own fork, not the instructor repository.

Example:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/PythonAcademy.git
cd PythonAcademy
```

If you prefer SSH:

```bash
git clone git@github.com:YOUR_GITHUB_USERNAME/PythonAcademy.git
cd PythonAcademy
```

## 4. Add the instructor repo as `upstream`

This lets you pull in new material from the instructor's `main` branch.

```bash
git remote add upstream https://github.com/alientometal/PythonAcademy.git
git remote -v
```

You should see both:

- `origin` -> your fork
- `upstream` -> the instructor repository

## 5. Open the repo in VS Code

From the project folder:

```bash
code .
```

If the `code` command is not available:

1. Open VS Code manually.
2. Choose `File` -> `Open Folder`.
3. Open the `PythonAcademy` folder.

## 6. Configure Git on your machine

If this is your first time using Git on your machine, set your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Check your configuration:

```bash
git config --global --list
```

## 7. Create a virtual environment

From the repository root:

```bash
python -m venv .venv
```

If your machine uses `python3` instead:

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

When the environment is active, your terminal should show something like:

```text
(.venv)
```

## 8. Upgrade pip and install session dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r IntermediatePython/requirements_web_automation.txt
```

## 9. Select the interpreter in VS Code

In VS Code:

1. Open the Command Palette with `Ctrl+Shift+P` or `Cmd+Shift+P`.
2. Search for `Python: Select Interpreter`.
3. Choose the interpreter inside `.venv`.

For notebooks:

1. Open the notebook.
2. Click the kernel selector in the top right.
3. Choose the same `.venv` interpreter.

## 10. Create a branch for your work

Do not work directly on `main`.

Create a branch for your notes or session progress:

```bash
git checkout -b yourname/module4-notes
```

Examples:

```bash
git checkout -b carlos/module4-notes
git checkout -b ana/web-automation-practice
```

## 11. Save your progress during the session

Check what changed:

```bash
git status
```

Stage and commit:

```bash
git add .
git commit -m "Add module 4 session notes"
```

Push your branch to your fork:

```bash
git push -u origin yourname/module4-notes
```

After the first push, later pushes are usually just:

```bash
git push
```

## 12. Keep your fork updated from the instructor `main`

Use this workflow when the instructor adds or updates material.

### Update your local `main`

First, switch to your local `main` branch:

```bash
git checkout main
```

Fetch the latest changes:

```bash
git fetch upstream
```

Rebase your local `main` on top of the instructor `main`:

```bash
git rebase upstream/main
```

Push the updated `main` to your fork:

```bash
git push origin main
```

### Update your working branch

Switch back to your branch:

```bash
git checkout yourname/module4-notes
```

Rebase your branch on top of your updated local `main`:

```bash
git rebase main
```

Push again:

```bash
git push --force-with-lease
```

Why `--force-with-lease` here?

Because rebasing rewrites your branch history. `--force-with-lease` is the safer way to update the branch on your fork after a rebase.

## 13. If rebase feels too advanced

Use this simpler workflow:

1. Keep your own work in a branch.
2. Before a new session, update `main` from `upstream/main`.
3. Create a new fresh branch from the updated `main`.

Example:

```bash
git checkout main
git fetch upstream
git rebase upstream/main
git push origin main
git checkout -b yourname/module4-notes-v2
```

This is often easier for beginners than rebasing an older working branch.

## 14. Recommended beginner Git reference

For Git basics, use the first eight chapters of:

`https://swcarpentry.github.io/git-novice/`

Recommended topics to review:

1. Automated version control
2. Setting up Git
3. Creating a repository
4. Tracking changes
5. Exploring history
6. Ignoring things
7. Remotes in GitHub
8. Collaborating

## 15. If you cannot use the VDI

Use Google Colab as a fallback for notebook work.

Good fallback options:

- Open notebooks from GitHub in Colab
- Upload notebooks manually to Colab
- Keep your notes in your fork even if execution happens in Colab

Important limitation:

- Colab is good for running notebooks
- Colab is not a full replacement for learning local Git, local VS Code, and virtual environment workflows

## 16. Quick session checklist

Before class starts, make sure this works:

```bash
git status
python --version
python -m pip --version
```

And confirm:

- You cloned your fork
- `upstream` is configured
- `.venv` is active
- Dependencies installed successfully
- VS Code is using the `.venv` interpreter
- You created your own working branch
- You can open the session notebooks
