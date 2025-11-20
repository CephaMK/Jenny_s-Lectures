#!/usr/bin/python3

# This file contains code for a command line interface expense tracker

print("=== Welcome to MK's Expense Tracker ===")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Item name: ")
        cost = float(input("Cost (KES): "))
        category = input("Category (food, transport, etc): ")
        expenses.append((item, cost, category))
        print("Expense added.")

    elif choice == "2":
        print("\n--- Expenses ---")
        for item, cost, category in expenses:
            print(f"{item} - KES {cost:.2f} ({category})")

    elif choice == "3":
        total = sum(e[1] for e in expenses)
        print(f"\nTotal spent: KES {total:.2f}")

    elif choice == "4":
        break

    else:
        print("Invalid option.")
