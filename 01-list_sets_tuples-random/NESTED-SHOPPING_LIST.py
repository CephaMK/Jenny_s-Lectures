#!/usr/bin/python3

'''
This code is a shopping list implementation that takes input from the user
iT allows thw user to:
    add items
    update quantities
    remove items
    view items on list

'''
shopping = []

while True:
        print("\nWelcome to MK's Shopping List Menu")
        print("1. Add item")
        print("2. Update quantity")
        print("3. Remove item")
        print("4. View list")
        print("5. Exit")
        
        choice = input("Select option: ")
        
        if choice == "1":
            item = input("Item name: ")
            qty = int(input("Quantity: "))
            shopping.append([item, qty])
            print("Item added.")
        
        elif choice == "2":
            item = input("Item to update: ")
            for i in shopping:
                if i[0].lower() == item.lower():
                    new_qty = int(input("New quantity: "))
                    i[1] = new_qty
                    print("Updated.")
                    break 
            else:
                print("Item not found")

        elif choice == "3":
            item = input("Item to remove: ")
            for i in shopping:
                if i[0].lower() == item.lower():
                    shopping.remove(i)
                    print("Removed.")
                    break
                else:
                    print("Item not found.")

        elif choice == "4":
            print("\nCurrent Shopping List:")
            for item, qty in shopping:
                print(f"- {item}: {qty}")
                
        elif choice == "5":
            break

        else:
            print("Invalid option")
