"""
Utility functions for the console todo application
"""
from typing import Any


def validate_task_id(task_id: Any) -> bool:
    """Validate that a task ID is a positive integer"""
    try:
        id_val = int(task_id)
        return id_val > 0
    except (ValueError, TypeError):
        return False


def validate_task_description(description: str) -> bool:
    """Validate that a task description is not empty or just whitespace"""
    return bool(description and description.strip())


def format_task_list(tasks: list) -> str:
    """Format a list of tasks for display"""
    if not tasks:
        return "No tasks found."
    
    task_strings = [str(task) for task in tasks]
    return "\n".join(task_strings)