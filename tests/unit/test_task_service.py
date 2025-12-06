"""
Unit tests for the TaskService
"""
import pytest
from src.console_todo.models.task import Task
from src.console_todo.services.task_service import TaskService


def test_task_service_initialization():
    """Test that TaskService initializes with empty task list"""
    service = TaskService()
    
    assert service.get_all_tasks() == []
    assert service._next_id == 1


def test_add_task():
    """Test adding a task"""
    service = TaskService()
    
    task = service.add_task("Test task")
    
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed == False
    assert len(service.get_all_tasks()) == 1
    assert service._next_id == 2


def test_add_task_empty_description():
    """Test that adding a task with empty description raises an error"""
    service = TaskService()
    
    with pytest.raises(ValueError):
        service.add_task("")
    
    with pytest.raises(ValueError):
        service.add_task("   ")


def test_get_all_tasks():
    """Test getting all tasks"""
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")
    
    tasks = service.get_all_tasks()
    
    assert len(tasks) == 2
    assert tasks[0].description == "Task 1"
    assert tasks[1].description == "Task 2"


def test_get_task_by_id():
    """Test getting a task by ID"""
    service = TaskService()
    added_task = service.add_task("Test task")
    
    retrieved_task = service.get_task_by_id(1)
    
    assert retrieved_task is not None
    assert retrieved_task.id == added_task.id
    assert retrieved_task.description == added_task.description


def test_get_task_by_id_not_found():
    """Test getting a task that doesn't exist"""
    service = TaskService()
    
    retrieved_task = service.get_task_by_id(999)
    
    assert retrieved_task is None


def test_update_task_description():
    """Test updating a task's description"""
    service = TaskService()
    original_task = service.add_task("Original task")
    
    updated_task = service.update_task(1, description="Updated task")
    
    assert updated_task is not None
    assert updated_task.description == "Updated task"
    assert updated_task.id == 1


def test_update_task_completion():
    """Test updating a task's completion status"""
    service = TaskService()
    original_task = service.add_task("Test task")
    
    updated_task = service.update_task(1, completed=True)
    
    assert updated_task is not None
    assert updated_task.completed == True


def test_update_task_both_fields():
    """Test updating both description and completion status"""
    service = TaskService()
    original_task = service.add_task("Original task")
    
    updated_task = service.update_task(1, description="Updated task", completed=True)
    
    assert updated_task is not None
    assert updated_task.description == "Updated task"
    assert updated_task.completed == True


def test_update_task_not_found():
    """Test updating a task that doesn't exist"""
    service = TaskService()
    
    result = service.update_task(999, description="New description")
    
    assert result is None


def test_update_task_empty_description():
    """Test that updating with empty description raises an error"""
    service = TaskService()
    service.add_task("Original task")
    
    with pytest.raises(ValueError):
        service.update_task(1, description="")


def test_delete_task():
    """Test deleting a task"""
    service = TaskService()
    service.add_task("Task to delete")
    service.add_task("Another task")
    
    result = service.delete_task(1)
    
    assert result == True
    remaining_tasks = service.get_all_tasks()
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0].id == 2


def test_delete_task_not_found():
    """Test deleting a task that doesn't exist"""
    service = TaskService()
    
    result = service.delete_task(999)
    
    assert result == False


def test_mark_task_complete():
    """Test marking a task as complete"""
    service = TaskService()
    service.add_task("Test task")
    
    updated_task = service.mark_task_complete(1)
    
    assert updated_task is not None
    assert updated_task.completed == True


def test_mark_task_incomplete():
    """Test marking a task as incomplete"""
    service = TaskService()
    service.add_task("Test task")
    service.mark_task_complete(1)
    
    updated_task = service.mark_task_incomplete(1)
    
    assert updated_task is not None
    assert updated_task.completed == False