# Console Todo App - Phase I

A command-line interface todo application developed as part of the PIAIC Hackathon Phase I submission. This application demonstrates spec-driven development principles with a clean, modular architecture.

## Overview

The Console Todo App is a simple yet powerful command-line application that allows users to manage their tasks efficiently. Built with Python 3.13+, the application implements all 5 basic todo features with an intuitive console interface.

## Features Implemented

- **Add Tasks**: Create new todo items with descriptions
- **List Tasks**: Display all tasks with their status (completed/incomplete)
- **Complete Tasks**: Mark tasks as completed with visual indicators
- **Delete Tasks**: Remove tasks from the list
- **Exit Application**: Clean exit functionality

## Tech Stack

- **Language**: Python 3.13+
- **Architecture**: Clean Architecture (Models, Services, CLI, Utils)
- **Development Methodology**: Spec-driven development
- **Testing**: Pytest for unit and integration testing

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd to-do-evaluation-ph-01
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Execute the following command to start the application:

```bash
python -m src.console_todo.main
```

## Available Commands

Once the application is running, you can use the following commands:

- `add <description>` - Add a new task (e.g., `add Buy groceries`)
- `list` - Display all tasks with their completion status
- `complete <id>` - Mark a task as complete (e.g., `complete 1`)
- `delete <id>` - Remove a task by its ID (e.g., `delete 2`)
- `exit` - Exit the application

## Project Structure

```
to-do-evaluation-ph-01/
├── src/
│   └── console_todo/
│       ├── main.py                 # Entry point of the application
│       ├── models/
│       │   └── task.py             # Task data model and manager
│       ├── services/
│       │   └── task_service.py     # Business logic for task operations
│       ├── cli/
│       │   └── interface.py        # Command line interface and parsing
│       └── utils/
│           └── validators.py       # Input validation utilities
├── tests/
│   ├── unit/
│   │   ├── test_task.py           # Task model tests
│   │   └── test_task_service.py   # Task service tests
│   └── integration/
│       └── test_cli.py            # CLI integration tests
├── requirements.txt               # Project dependencies
├── pyproject.toml                 # Build system configuration
└── README.md                      # This file
```

## Testing

Run the test suite to ensure all functionality works as expected:

```bash
pytest
```

Or run with verbose output:

```bash
pytest -v
```

## Author

PIAIC Hackathon Submission - Phase I

## Phase I Completion

This console application represents the completion of Phase I requirements, implementing all 5 basic todo features with a spec-driven development approach. The application serves as the foundation for future phases of development, potentially expanding to a full-stack web application.

## Future Enhancements

Potential improvements for future phases:
- Persistent storage (database integration)
- Web-based GUI
- User authentication
- Data export/import features
- Task categorization and prioritization