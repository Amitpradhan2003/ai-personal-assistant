import json
import re
from langchain.tools import tool

TODO_FILE = "data/todos.json"

def load_todos():
    try:
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

@tool("todo")
def todo_tool(text: str) -> str:
    """
    Natural-language todo tool.
    Examples it understands:
    - add Complete my AI project
    - please add: buy groceries
    - remove homework
    - delete: laundry
    - show tasks
    - view my todo list
    """

    todos = load_todos()
    t = text.lower().strip()

    # -------------------------------
    # VIEW
    # -------------------------------
    if any(word in t for word in ["view", "show", "list", "display"]):
        if not todos:
            return "Your todo list is empty."
        items = "\n".join(f"- {item}" for item in todos)
        return f"Your tasks:\n{items}"

    # -------------------------------
    # ADD
    # -------------------------------
    if "add" in t or "create" in t:
        # extract everything after 'add'
        match = re.search(r"add[: ]?(.*)", text, re.IGNORECASE)
        if match:
            task = match.group(1).strip()
            if not task:
                return "Please specify a task to add."
            todos.append(task)
            save_todos(todos)
            return f"Added task: {task}"

    # -------------------------------
    # REMOVE / DELETE
    # -------------------------------
    if "remove" in t or "delete" in t:
        match = re.search(r"(remove|delete)[: ]?(.*)", text, re.IGNORECASE)
        if match:
            task = match.group(2).strip()
            if task in todos:
                todos.remove(task)
                save_todos(todos)
                return f"Removed task: {task}"
            else:
                return f"Task not found: {task}"

    # -------------------------------
    # INVALID
    # -------------------------------
    return (
        "Invalid todo command.\n"
        "You can say:\n"
        "- add <task>\n"
        "- remove <task>\n"
        "- view tasks"
    )
