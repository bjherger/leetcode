# Agent instructions

## Commit and push

When the user asks to **commit and push** (or similar: "commit and push", "commit all and push", etc.):

1. **Stage all changes**: Run `git add -A` (or `git add .`) so that every new and modified file is staged. Do not commit only a subset unless the user explicitly specifies which files.
2. **Commit**: Create a single commit with all staged files. Use a clear commit message; if the user gave a message, use it; otherwise infer one from the changes (e.g. "Add solution for LeetCode 933", "Update decode string solution").
3. **Push**: Run `git push` to push all commits to the remote.

Do not leave any new or modified files unstaged when the user intends to commit and push everything.

## Setting up new LeetCode question files

When the user asks to create a new solution file for a LeetCode problem (e.g. from a URL or problem name):

1. **Use an existing solution file as the template** (e.g. one in `questions/` they point to). Create a new file named by problem number and slug (e.g. `questions/933_number_of_recent_calls.py`).

2. **Docstring** (at top of file):
   - **Start / End**: Use the **current time** (when the file is created) for `Start:` and `TODO` for `End:`.
   - **Content**: Include only the problem **description**, **examples**, and **constraints** from the problem. Do **not** include Options, Edge cases, or a filled-in "Questions / notes" section.
   - **Structure**: After the constraints, include these three sections as **empty** placeholders (no bullets, or a single placeholder bullet if you want):
     - `Questions / notes:` (empty list)
     - `Options` (empty list)
     - `Notes for next time:` (empty list)

3. **Code**:
   - Add only the necessary imports (e.g. `from unittest import TestCase`) and the **class/function signatures** required by the problem. **Do not implement** the solution (use `...` or `pass` in the body).

4. **Tests**:
   - Include **all relevant unit tests** from the problem (e.g. the examples). Use `TestCase` and `assertEqual` (or the same style as the template). Tests should run against the stub so they fail until the user implements the solution.

5. **Do not** add options, edge cases, or "questions/notes" content in the docstring; keep those sections empty for the user to fill when solving.
