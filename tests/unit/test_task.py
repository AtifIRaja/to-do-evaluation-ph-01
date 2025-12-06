"""
Unit tests for the Task model
"""
import pytest
from datetime import datetime
from src.console_todo.models.task import Task


def test_task_creation():
    """Test creating a new task"""
    task = Task(id=1, description="Test task")
    
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed == False
    assert isinstance(task.created_at, datetime)


def test_task_str_representation():
    """Test string representation of a task"""
    task = Task(id=1, description="Test task")
    
    str_repr = str(task)
    assert "○" in str_repr  # Not completed marker
    assert "1:" in str_repr
    assert "Test task" in str_repr


def test_task_completion():
    """Test marking a task as complete"""
    task = Task(id=1, description="Test task")
    task.completed = True
    
    str_repr = str(task)
    assert "✓" in str_repr  # Completed marker


def test_task_post_init_sets_current_time():
    """Test that created_at is set to current time if not provided"""
    task = Task(id=1, description="Test task")
    
    assert task.created_at is not None
    assert isinstance(task.created_at, datetime)
    # Verify it's reasonably close to current time (within a few seconds)
    time_diff = abs((datetime.now() - task.created_at).total_seconds())
    assert time_diff < 5