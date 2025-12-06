"""
Integration tests for the CLI interface
"""
import pytest
from src.console_todo.services.task_service import TaskService
from src.console_todo.cli.interface import CLIInterface


def test_cli_add_command():
    """Test the add command through CLI"""
    service = TaskService()
    cli = CLIInterface(service)
    
    result = cli.execute_command("add", ["Buy groceries"])
    
    assert "Added task:" in result
    assert "Buy groceries" in result
    assert len(service.get_all_tasks()) == 1
    assert service.get_all_tasks()[0].description == "Buy groceries"


def test_cli_list_command():
    """Test the list command through CLI"""
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")
    cli = CLIInterface(service)
    
    result = cli.execute_command("list", [])
    
    assert "Your tasks:" in result
    assert "Task 1" in result
    assert "Task 2" in result


def test_cli_complete_command():
    """Test the complete command through CLI"""
    service = TaskService()
    service.add_task("Task to complete")
    cli = CLIInterface(service)
    
    result = cli.execute_command("complete", ["1"])
    
    assert "Marked task as complete:" in result
    completed_task = service.get_task_by_id(1)
    assert completed_task is not None
    assert completed_task.completed == True


def test_cli_update_command():
    """Test the update command through CLI"""
    service = TaskService()
    service.add_task("Original task")
    cli = CLIInterface(service)
    
    result = cli.execute_command("update", ["1", "Updated", "task"])
    
    assert "Updated task:" in result
    assert "Updated task" in result
    updated_task = service.get_task_by_id(1)
    assert updated_task is not None
    assert updated_task.description == "Updated task"


def test_cli_delete_command():
    """Test the delete command through CLI"""
    service = TaskService()
    service.add_task("Task to delete")
    cli = CLIInterface(service)
    
    result = cli.execute_command("delete", ["1"])
    
    assert "Deleted task" in result
    assert service.get_all_tasks() == []


def test_cli_help_command():
    """Test the help command through CLI"""
    service = TaskService()
    cli = CLIInterface(service)
    
    result = cli.execute_command("help", [])
    
    assert "Available commands:" in result
    assert "add" in result
    assert "list" in result
    assert "complete" in result


def test_cli_command_parsing():
    """Test CLI command parsing functionality"""
    service = TaskService()
    cli = CLIInterface(service)
    
    # Test parsing add command
    command, args = cli.parse_command("add Buy groceries")
    assert command == "add"
    assert args == ["Buy", "groceries"]
    
    # Test parsing list command
    command, args = cli.parse_command("list")
    assert command == "list"
    assert args == []
    
    # Test parsing complete command
    command, args = cli.parse_command("complete 5")
    assert command == "complete"
    assert args == ["5"]


def test_cli_empty_input():
    """Test CLI with empty input"""
    service = TaskService()
    cli = CLIInterface(service)
    
    command, args = cli.parse_command("")
    assert command == ""
    assert args == []


def test_cli_unknown_command():
    """Test CLI with unknown command"""
    service = TaskService()
    cli = CLIInterface(service)
    
    result = cli.execute_command("unknown", ["arg1", "arg2"])
    
    assert "Unknown command: unknown" in result


def test_cli_exit_command():
    """Test CLI exit command returns exit signal"""
    service = TaskService()
    cli = CLIInterface(service)
    
    result = cli.execute_command("exit", [])
    
    assert result == "exit"