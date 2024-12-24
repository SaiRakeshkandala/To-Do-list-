import json

# File to save tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"pending": [], "completed": []}

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    print("\nPending Tasks:")
    for i, task in enumerate(tasks["pending"], 1):
        print(f"{i}. {task}")
    print("\nCompleted Tasks:")
    for i, task in enumerate(tasks["completed"], 1):
        print(f"{i}. {task}")

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks["pending"].append(task)
    print("Task added!")

# Mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to mark as completed: ")) - 1
        tasks["completed"].append(tasks["pending"].pop(task_no))
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to delete: ")) - 1
        tasks["pending"].pop(task_no)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
