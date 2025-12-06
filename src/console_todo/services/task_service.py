from typing import List, Optional
from ..models.task import Task

class TaskService:
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        task = Task(id=self._next_id, description=description)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False
