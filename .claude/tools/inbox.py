#!/usr/bin/env python3
"""
Prompt Inbox — Task Queue Manager
Reads and manages INBOX.md so Claude picks up queued prompts after finishing current work.

Usage:
  python .claude/tools/inbox.py --check       # Print pending tasks (used by Stop hook)
  python .claude/tools/inbox.py --list        # List all tasks with status
  python .claude/tools/inbox.py --next        # Print text of next pending task
  python .claude/tools/inbox.py --start N     # Mark task N as in-progress [→]
  python .claude/tools/inbox.py --complete N  # Mark task N as done [x]
  python .claude/tools/inbox.py --add "text"  # Add a new task
  python .claude/tools/inbox.py --clear       # Remove all completed tasks
"""

import argparse
import os
import re
import sys
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

INBOX_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "INBOX.md")
INBOX_PATH = os.path.normpath(INBOX_PATH)

# Task states
PENDING     = "[ ]"
IN_PROGRESS = "[→]"
DONE        = "[x]"

TASK_PATTERN = re.compile(r"^(\s*)-\s+(\[[ →x]\])\s+(.+)$")


def read_inbox():
    if not os.path.exists(INBOX_PATH):
        return []
    with open(INBOX_PATH, "r", encoding="utf-8") as f:
        return f.readlines()


def write_inbox(lines):
    with open(INBOX_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)


def parse_tasks(lines):
    """Return list of (line_index, indent, state, text) for all task lines."""
    tasks = []
    for i, line in enumerate(lines):
        m = TASK_PATTERN.match(line.rstrip("\n"))
        if m:
            tasks.append((i, m.group(1), m.group(2), m.group(3)))
    return tasks


def get_pending(tasks):
    return [(i, indent, state, text) for i, indent, state, text in tasks if state == PENDING]


def get_in_progress(tasks):
    return [(i, indent, state, text) for i, indent, state, text in tasks if state == IN_PROGRESS]


def cmd_check():
    """Used by the Stop hook — prints a notice if there are pending tasks."""
    lines = read_inbox()
    tasks = parse_tasks(lines)
    pending = get_pending(tasks)
    in_prog = get_in_progress(tasks)

    if not pending and not in_prog:
        # Silence — no output if nothing to do
        return

    print("─" * 60)
    print("  📥  INBOX — PENDING TASKS DETECTED")
    print("─" * 60)

    if in_prog:
        print(f"\n  ⏳ IN PROGRESS ({len(in_prog)}):")
        for idx, (li, indent, state, text) in enumerate(in_prog, 1):
            print(f"     {idx}. {text}")

    if pending:
        print(f"\n  📋 QUEUED ({len(pending)}):")
        for idx, (li, indent, state, text) in enumerate(pending, 1):
            print(f"     {idx}. {text}")

    print(f"\n  Run: /queue   to process the next task")
    print(f"  Or add more tasks to INBOX.md while Claude is working.")
    print("─" * 60)


def cmd_list():
    """List all tasks."""
    lines = read_inbox()
    tasks = parse_tasks(lines)

    if not tasks:
        print("  Inbox is empty. Add tasks to INBOX.md.")
        return

    icons = {PENDING: "[ ]", IN_PROGRESS: "[→]", DONE: "[x]"}
    status_label = {PENDING: "PENDING", IN_PROGRESS: "IN PROGRESS", DONE: "DONE"}

    all_pending = [t for t in tasks if t[2] == PENDING]
    all_prog    = [t for t in tasks if t[2] == IN_PROGRESS]
    all_done    = [t for t in tasks if t[2] == DONE]

    print(f"\n  INBOX  ({len(tasks)} total | {len(all_pending)} pending | {len(all_prog)} in progress | {len(all_done)} done)")
    print(f"  {'─'*54}")

    for group, label in [(all_prog, "IN PROGRESS"), (all_pending, "PENDING"), (all_done, "DONE")]:
        if group:
            print(f"\n  {label}:")
            for task_num, (li, indent, state, text) in enumerate(tasks, 1):
                if (state == IN_PROGRESS and label == "IN PROGRESS") or \
                   (state == PENDING and label == "PENDING") or \
                   (state == DONE and label == "DONE"):
                    icon = {"[ ]": "○", "[→]": "→", "[x]": "✓"}[state]
                    print(f"    {icon}  {text}")


def cmd_next():
    """Print the text of the next pending task (for Claude to act on)."""
    lines = read_inbox()
    tasks = parse_tasks(lines)
    pending = get_pending(tasks)

    if not pending:
        print("  No pending tasks in inbox.")
        return

    li, indent, state, text = pending[0]
    # Mark as in-progress
    lines[li] = f"{indent}- {IN_PROGRESS} {text}\n"
    write_inbox(lines)
    print(text)


def cmd_start(n):
    """Mark task N (1-indexed among pending) as in-progress."""
    lines = read_inbox()
    tasks = parse_tasks(lines)
    pending = get_pending(tasks)

    if n < 1 or n > len(pending):
        print(f"ERROR: Task {n} not found. {len(pending)} pending tasks.", file=sys.stderr)
        sys.exit(1)

    li, indent, state, text = pending[n - 1]
    lines[li] = f"{indent}- {IN_PROGRESS} {text}\n"
    write_inbox(lines)
    print(f"  → Marked as in-progress: {text}")


def cmd_complete(n):
    """Mark task N (1-indexed among in-progress, or pending if none in-progress) as done."""
    lines = read_inbox()
    tasks = parse_tasks(lines)
    in_prog = get_in_progress(tasks)
    pending = get_pending(tasks)

    candidates = in_prog if in_prog else pending
    if n < 1 or n > len(candidates):
        print(f"ERROR: Task {n} not found. {len(candidates)} available tasks.", file=sys.stderr)
        sys.exit(1)

    li, indent, state, text = candidates[n - 1]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines[li] = f"{indent}- {DONE} {text}  *(completed {timestamp})*\n"
    write_inbox(lines)
    print(f"  ✓ Completed: {text}")


def cmd_add(text):
    """Add a new pending task to INBOX.md."""
    lines = read_inbox()

    # Find the Queue section or append
    queue_idx = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## queue") or line.strip().lower().startswith("## pending"):
            queue_idx = i
            break

    new_task = f"- {PENDING} {text}\n"

    if queue_idx is not None:
        # Insert after the section header
        lines.insert(queue_idx + 1, new_task)
    else:
        if lines and not lines[-1].endswith("\n"):
            lines.append("\n")
        lines.append(new_task)

    write_inbox(lines)
    print(f"  + Added: {text}")


def cmd_clear():
    """Remove all completed tasks from INBOX.md."""
    lines = read_inbox()
    tasks = parse_tasks(lines)
    done_lines = {li for li, _, state, _ in tasks if state == DONE}
    new_lines = [line for i, line in enumerate(lines) if i not in done_lines]
    write_inbox(new_lines)
    removed = len(done_lines)
    print(f"  Cleared {removed} completed task(s) from inbox.")


def main():
    parser = argparse.ArgumentParser(
        description="Prompt Inbox Queue Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--check",    action="store_true", help="Check for pending tasks (used by Stop hook)")
    parser.add_argument("--list",     action="store_true", help="List all tasks")
    parser.add_argument("--next",     action="store_true", help="Print and start next pending task")
    parser.add_argument("--start",    type=int, default=None, help="Mark pending task N as in-progress")
    parser.add_argument("--complete", type=int, default=None, help="Mark task N as complete")
    parser.add_argument("--add",      type=str, default=None, help="Add a new task")
    parser.add_argument("--clear",    action="store_true", help="Remove all completed tasks")

    args = parser.parse_args()

    if args.check:
        cmd_check()
    elif args.list:
        cmd_list()
    elif args.next:
        cmd_next()
    elif args.start is not None:
        cmd_start(args.start)
    elif args.complete is not None:
        cmd_complete(args.complete)
    elif args.add:
        cmd_add(args.add)
    elif args.clear:
        cmd_clear()
    else:
        # Default: check (so the hook is silent when nothing pending)
        cmd_check()


if __name__ == "__main__":
    main()
