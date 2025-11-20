#!/usr/bin/python3

#This code simulates the working of simple contact book

print("WELCOME TO MK's CONTACT BOOK")
contacts = {}

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Name: ").title()
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        name = input("Search name: ").title()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Not found.")

    elif choice == "3":
        name = input("Delete name: ").title()
        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print("Not found.")

    elif choice == "4":
        print("\n--- All Contacts ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

    elif choice == "5":
        break
    
    else:
        print("Invalid choice.")
