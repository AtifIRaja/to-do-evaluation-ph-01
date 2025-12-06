import sys
import os

# Ensure we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.console_todo.services.task_service import TaskService
from src.console_todo.cli.interface import CLIInterface

def main():
    print('Welcome to the Console Todo Application!')
    print('Type "help" for available commands or "exit" to quit.')

    task_service = TaskService()
    cli = CLIInterface(task_service)

    while True:
        try:
            user_input = input('\n> ').strip()
            if not user_input:
                continue

            command, args = cli.parse_command(user_input)
            result = cli.execute_command(command, args)

            if result == 'exit':
                print('Goodbye!')
                break

            print(result)

        except KeyboardInterrupt:
            print('\nGoodbye!')
            break
        except EOFError:
            print('\nGoodbye!')
            break

if __name__ == '__main__':
    main()
