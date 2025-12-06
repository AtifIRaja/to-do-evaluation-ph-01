from typing import List, Tuple
from ..services.task_service import TaskService

class CLIInterface:
    """Handles command line interface operations"""

    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def parse_command(self, user_input: str) -> Tuple[str, List[str]]:
        parts = user_input.strip().split()
        if not parts:
            return "", []
        return parts[0].lower(), parts[1:]

    def execute_command(self, command: str, args: List[str]) -> str:
        if command == "add":
            return self._add_task(args)
        elif command == "list":
            return self._list_tasks()
        elif command in ["complete", "done"]:
            return self._complete_task(args)
        elif command == "delete":
            return self._delete_task(args)
        elif command in ["help", "?"]:
            return self._show_help()
        elif command in ["exit", "quit"]:
            return "exit"
        else:
            return f"Unknown command: {command}. Type 'help' for commands."

    def _add_task(self, args: List[str]) -> str:
        if not args:
            return "Usage: add <description>"
        description = " ".join(args)
        task = self.task_service.add_task(description)
        return f"Added task: {task}"

    def _list_tasks(self) -> str:
        tasks = self.task_service.get_all_tasks()
        if not tasks:
            return "No tasks found."
        return "\n".join([str(t) for t in tasks])

    def _complete_task(self, args: List[str]) -> str:
        if not args:
            return "Usage: complete <id>"
        try:
            task = self.task_service.mark_task_complete(int(args[0]))
            if task:
                return f"Completed: {task}"
            return "Task not found."
        except ValueError:
            return "Invalid ID. Please enter a number."

    def _delete_task(self, args: List[str]) -> str:
        if not args:
            return "Usage: delete <id>"
        try:
            success = self.task_service.delete_task(int(args[0]))
            if success:
                return f"Deleted task {args[0]}"
            return "Task not found."
        except ValueError:
            return "Invalid ID. Please enter a number."

    def _show_help(self) -> str:
        return """
Available Commands:
  add <text>      Add a new task
  list            Show all tasks
  complete <id>   Mark a task as done
  delete <id>     Remove a task
  exit            Quit the application
        """
