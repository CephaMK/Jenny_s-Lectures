#!/usr/bin/python3

'''

This file contains code for a library book borrowing system
It allows the user to:
    View books (list of dicts)
    Borrow a book (mark unavailable)
    Return a book
    Add new books

'''

library = [
        {"title": "Python Basics",      "available": True},
        {"title": "Clean Code",         "available": True},
        {"title": "Data Structures",    "available": True}
]

while True:
    print("\n=== Library System ===")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("\n--- Books ---")
        for book in library:
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book['title']} - {status}")

    elif choice == "2":
        title = input("Book title to borrow: ").title()

        for book in library:
            if book["title"] == title:
                if book["available"]:
                    book["available"] = False
                    print("Book borrowed!")
                else:
                    print("Book already borrowed!")
                break
            else:
                print("Book not found.")

    elif choice == "3":
        title = input("Book to return: ").title()
        
        for book in library:
            if book["title"] == title:
                if not book["available"]:
                    book["available"] = True
                    print("Book returned!")
                else:
                    print("This book wasn't borrowed.")
                    break

        else:
            print("Book not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice")

