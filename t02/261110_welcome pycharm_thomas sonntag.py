# List to store tasks
tasks = []

def add_task(task):
    """Adds a new task to the list."""
    tasks.append(task)
    print(f'Task "{task}" added!')

def show_tasks():
    """Displays all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(task_number):
    """Removes a task by its number."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed}" removed!')
    else:
        print("Invalid task number.")

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task description: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_number = int(input("Enter task number to remove: "))
        remove_task(task_number)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
