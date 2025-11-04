#!/usr/bin/python3

#Rollacoster entry fee

print ("WELCOME TO MK PARK")

height = float(input("What is your height in feet?"))
age = int(input("What is your age?"))
pic = input("Do you want photos of the experience? (Y or N):").upper()

if height > 3:
    print ("You can ride the Rollacoster")
    if age < 12:
        bill = 150
    elif age > 12 and age < 18:
        bill = 250
    elif age > 18:
        bill = 500
else:
    print("You cannot ride the Rollacoster")
    bill = 0

if pic == "Y":
    bill += 50


print (f"Your total bill is {bill}.Thank you for visiting MK park")
