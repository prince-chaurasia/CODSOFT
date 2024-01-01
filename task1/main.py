# Sample in-memory storage for tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task index.")

def list_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks added yet.")

def main():
    while True:
        print("\nChoose an action:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
            if tasks:
                task_index = int(input("Enter the index of the task to remove: ")) - 1
                remove_task(task_index)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
