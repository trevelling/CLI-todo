This Python application provides a command-line interface (CLI) for managing a to-do list. Users can add, remove, list, and filter tasks based on priority.

Modules Used

    click: Used for creating the CLI interface in a composable way.

Features

    Add Task: Add a new task to the to-do list with a name, description, and priority.
    Remove Task: Remove a task from the to-do list by index.
    List Tasks: List all tasks in the to-do list or filter by priority.
    Greet User: Greets the user by name.

Usage

    Greeting User:
    python todo.py hello --name "Your Name"

    Adding a Task:
    python todo.py add-todo -n "Task Name" -d "Task Description" -p "Priority"

    Removing a Task:
    python todo.py delete-todo <index>

    Listing Tasks:
    python todo.py list-todo -p "Priority"

    Example:
    python todo.py hello --name "Alice"
    python todo.py add-todo -n "Buy Groceries" -d "Buy fruits and vegetables" -p "h"
    python todo.py add-todo -n "Complete Project" -d "Finish the project report" -p "m"
    python todo.py list-todo -p "h"
    python todo.py delete-todo 1
    python todo.py list-todo

Note:
    Priority options: "o" (Optional), "l" (Low), "m" (Medium), "h" (High), "c" (Crucial).
