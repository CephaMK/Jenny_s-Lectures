#!/usr/bin/python3

#Pizza order program

print ("Welcome to MK Pizza Delivery")

#Pizza size
size = input("What size pizza do you want?( SMALL, MEDIUM or LARGE):").upper()
pepperonni = input ("Do you want to add pepperonni? (YES or NO):").upper()
extra_cheese = input ("Do you want cheese?(YES or NO):").upper()

#Billing
if size == "SMALL":
    bill = 100
elif size == "MEDIUM":
    bill = 200
elif size == "LARGE":
    bill = 300
else:
    print("Invalid size entered")
    bill = 0

#add pepperonni
if pepperonni == "YES":
    if size == "SMALL":
        bill += 20
    elif size in ["MEDIUM", "LARGE"]:
        bill +=50

#extra cheese
if extra_cheese == "YES":
    bill +=20

#final bill
print(f"Your total comes to {bill}.Thank you for using MK pizza delivery.")

