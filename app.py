tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour tasks:")
        for i, tasks in enumerate(tasks,1):
            print(f"{i}. {tasks}")

while True:
    print("\n1. Add a task\n2. Remove a task\n3. show tasks\n4. Exit")
    choice = input("Enter yoyur choice:")

    if choice == '1':
        task = input("enter task:")
        tasks.append(task)
        print("task added!")

    elif choice == '2':
        show_tasks()
        num = int(input("enter task number to remove:"))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("task removed!")
        else:
            print("Invalid number")

    elif choice == '3':
        show_tasks()

    elif choice == '4':
        break

    else:
        print("Invalid choice")
        