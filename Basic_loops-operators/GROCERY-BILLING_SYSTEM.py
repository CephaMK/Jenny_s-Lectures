#!/usr/bin/python3

#GROCERY BILLING SYSYTEM. This Code contains a basic billing system for a teller in a market setting

print("Welcome to MK Grocery Billing System.")

total = 0

while True:
    price = input("Enter item price or type 'done' to finish: ")
    if price.lower() == "done":
        break

    #curbing invlaid inputs
    if price.replace('.', ' ', 1).isdigit():
        total += float(price)
    else:
        print("Invalid input! Please enter a number.")
        print(f"\nSubtotal: {total:.2f} KES")

#Applying the discount
if total > 500:
    discount = total * 0.10
    total -= discount
    print(f"Discount applied: {discount:.2f} KES")

#Add 5% tax
tax = total * 0.05
total += tax

print(f"Tax added: + {tax:.2f} KES")
print(f"Final total: {total:.2f} KES")
