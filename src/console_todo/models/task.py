from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: int
    description: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.description}"
