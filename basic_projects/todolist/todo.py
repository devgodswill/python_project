import os
import json
from datetime import datetime

# file to store the todo list

TASKS_FILE = 'tasks.json'

def load_task():
    """Load task from a JSON file."""

    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Saves tasks to a json file"""

    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all the task with their details"""
    if not tasks:
        print("No tasks to display")
    else:
        print("---Your TODO List---")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['title']} (piority: {task['priority']}, due: {task['due']})")

def add_task(tasks):
    """Add a new task to the todo list."""
    task_name = input("Enter the task name: ")
    priority = input("Enter the priority (high/medium/low): ").capitalize()
    due_date = input("Enter the due date (YYYY-MM-DD): ")

    # validate due date format

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD")
        return


    new_task = {
        "title": task_name,
        "priority": priority,
        "due_date": due_date
    }


    tasks.append(new_task)
    print(f"Task '{task_name} has been added to your Todo list")
    save_tasks(tasks)


def remove_task(tasks):
    """remove a task from the todo list by it's number"""

    display_tasks(tasks)

    if tasks:
        try:
            task_number = int(input('Enter the task number to remove: '))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['title']} has been removed.")
                save_tasks(tasks)
            else:
                print("invalid task number!")
        except ValueError:
            print("Invalid task number! Please enter a valid number.")


def edit_task(tasks):
    """Edit an existing task"""

    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input('Enter the task number to edit: '))
            if 1 <= task_number <= len(tasks):
                task = task[task_number -1]
                print(f"Editing task: {task['title']}")

                new_task_name = input("Enter the new task name (leave empty to keep the current): ")
                if new_task_name:
                    task['title'] = new_task_name

                new_priority = input(f"Enter new priority (current: {task['priority']}): ").capitalize()
                if new_priority:
                    task["priority"] = new_priority

                new_due_date = input(f"Enter new due date (current: {task['due_date']}): ")
                if new_due_date:
                    try:
                        datetime.strptime(new_due_date, "%Y-%m-%d")
                        task["due_date"] = new_due_date
                    except ValueError:
                        print("Invalid date format! Please use YYYY-MM-DD.\n")
                        return

                print(f"Task '{task['task']}' has been updated.\n")
                save_tasks(tasks)
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number.\n")


def todo_list():
     """Main Todo list program that lets the user add, remove, edit, and view tasks."""

     tasks = load_task() # Load tasks from file on startup

     while True:
        print("=== Todo List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Edit Task")
        print("5. Exit")

        # Validate user input
        try:
            choice = int(input("Choose an option (1-5): "))
            print("\n")

            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                edit_task(tasks)
            elif choice == 5:
                print("Exiting Todo List. Have a productive day!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.\n")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.\n")

# Run the Todo List program
todo_list()