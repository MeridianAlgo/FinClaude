---
name: queue
description: Processes the next task from INBOX.md. Use when the user runs /queue, when the stop hook detects pending tasks, or when you want to pick up the next queued prompt. Reads INBOX.md, marks the task in-progress, executes it, then marks it complete.
argument-hint: "[optional: task number N to run a specific task]"
allowed-tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - WebFetch
---

# Prompt Queue Processor

Process the next task from INBOX.md, or a specific task if a number is provided.

## Input

Optional task number via `$ARGUMENTS`. If empty, process the next pending task.

---

## Steps

### Step 1: Check the Inbox

Run the inbox tool to see what's queued:

```bash
python .claude/tools/inbox.py --list
```

If no tasks are pending, report that the inbox is empty and stop.

### Step 2: Get the Next Task

If `$ARGUMENTS` is a number N, get that specific task. Otherwise get the next pending task:

```bash
python .claude/tools/inbox.py --next
```

This prints the task text AND marks it as in-progress (`[→]`).

### Step 3: Execute the Task

Read the task text and execute it exactly as if the user had typed it.

- If it's a financial analysis request (e.g. "analyze AAPL"), invoke the appropriate skill
- If it's a direct instruction, do it
- If it references a specific skill (e.g. "run /dcf-valuation on MSFT"), invoke that skill
- Use all available tools (WebSearch, WebFetch, Bash, etc.) as needed

### Step 4: Mark Complete

After finishing the task:

```bash
python .claude/tools/inbox.py --complete 1
```

### Step 5: Check for More

After completing, check if more tasks are queued:

```bash
python .claude/tools/inbox.py --check
```

If more tasks exist, ask the user: "There are N more tasks in the inbox. Process the next one?"

---

## INBOX.md Format

Tasks are stored in `INBOX.md` at the project root:

```
- [ ] pending task
- [→] in progress task
- [x] completed task  *(completed 2026-04-14 15:30)*
```

## Adding Tasks (for the user)

While Claude is working, open `INBOX.md` and add:
```
- [ ] analyze NVDA earnings
- [ ] run DCF on META with 12% WACC
- [ ] compare AAPL vs MSFT
```

Claude will see them when it finishes.

## Management Commands

```bash
# See all tasks
python .claude/tools/inbox.py --list

# Add a task programmatically
python .claude/tools/inbox.py --add "analyze TSLA technical setup"

# Mark complete manually
python .claude/tools/inbox.py --complete 1

# Clear completed tasks
python .claude/tools/inbox.py --clear
```
