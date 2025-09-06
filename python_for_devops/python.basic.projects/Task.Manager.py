tasks = []

print("Welcome to Task Manager Game!")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark!")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            done = int(input("Enter task number to mark as done: "))
            if 1 <= done <= len(tasks):
                removed = tasks.pop(done-1)
                print(f"✅ Task '{removed}' completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete!")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            delete = int(input("Enter task number to delete: "))
            if 1 <= delete <= len(tasks):
                removed = tasks.pop(delete-1)
                print(f"🗑️ Task '{removed}' deleted!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye! 👋")
        break






