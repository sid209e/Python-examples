"""Create a console-based to-do list application that allows users
to add, view, update, and delete tasks. The application should provide
 a menu-driven interface for interacting with the to-do list."""

tasks = []


def display_menu():
    print("To-Do List Application")
    print("1. To Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully")


def view_task():
    print("Tasks: ")
    for i,task in enumerate(tasks, start =1):
        print(f"{i}. {task}")


def update_task():
    view_task()
    index = int(input("Enter the task number to update: ")) - 1
    if index < 0 or index >= len(tasks):
        print("Invalid task number!")
    else:
        new_task = input("Enter the new task: ")
        tasks[index] = new_task
        print("Task updated successfully")


def delete_task():
    view_task()
    index = int(input("Enter the task number to delete: ")) - 1
    if index < 0 or index >= len(tasks):
        print("Invalid task number!")
    else:
        del tasks[index]
        print("Task deleted successfully!")


while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")