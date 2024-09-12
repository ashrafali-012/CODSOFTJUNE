# Simple To-Do List Program

def show_menu():
    print("==== TO-DO LIST MENU ====\n")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        except (IndexError, ValueError):
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
