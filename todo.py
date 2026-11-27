"""Simple To-Do List Manager"""


def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    print(f"Added: {task}")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\n===== Your To-Do List =====")
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. [{status}] {t['task']}")
    print()


def mark_done(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        print(f"Marked as done: {tasks[index - 1]['task']}")
    else:
        print("Invalid task number!")


def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number!")


def main():
    tasks = []
    print("===== To-Do List Manager =====")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            num = int(input("Task number to mark done: "))
            mark_done(tasks, num)
        elif choice == "4":
            view_tasks(tasks)
            num = int(input("Task number to delete: "))
            delete_task(tasks, num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
