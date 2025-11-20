#!/usr/bin/python3

'''

This file contains code for a simple to do list command line interface
It allows the user to:
    Add, remove, and mark tasks as done.
    Save tasks to a .txt file (using file I/O).
    
'''

todo_file = "tasks.txt"

# Load existing tasks
try:
        with open(todo_file, "r") as file:
                    tasks = file.read().splitlines()
except FileNotFoundError:
        tasks = []

while True:
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Save & Exit")

    choice = input("Choose option: ")
    
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        task = input("Task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Removed.")
        else:
            print("Task not found.")

    elif choice == "3":
       print("\n--- Your Tasks ---")
       for t in tasks:
           print(f"- {t}")

    elif choice == "4":
        with open(todo_file, "w") as file:
            for t in tasks:
                file.write(t + "\n")
                print("Tasks saved. Goodbye!")
                break

    else:
        print("Invalid choice.")



