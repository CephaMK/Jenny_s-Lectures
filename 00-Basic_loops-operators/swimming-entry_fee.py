#!/usr/bin/python3

#Swimming entry fees

print ("WELCOME TO MK PARK")
height = float(input("What is your height in feet?"))
age = int(input("What is your age?"))


if height > 3:
    print("You can swim")
    if age <= 12:
        bill = 150
    elif age > 12 and age <= 18:
        bill = 250
    elif age > 18:
        bill = 500
else:
    print("You cannot swim")
    bill = 0

print (f"Your total bill is {bill}. Thank you for visiting MK Park.")
