tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    print("\n----- YOUR TASKS -----")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")


def add_task():
    title = input("\nEnter task: ")

    if title.strip() == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    print("Task added successfully!")


def update_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to update: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        new_title = input("Enter new task: ")

        if new_title.strip() == "":
            print("Task cannot be empty.")
            return

        tasks[number - 1]["title"] = new_title

        print("Task updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to mark as completed: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["completed"] = True

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(number - 1)

        print(f"Task '{deleted_task['title']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:

        print("\n============================")
        print("       TO-DO LIST APP")
        print("============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        print("============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print("\nThank you for using To-Do List App!")
            break

        else:
            print("Invalid choice. Please try again.")


main()