#!/usr/bin/python3

#This code calculates the cost of the users electricity bill as pr the amount of units used.

units = float(input("Enter electricity units used: "))

if units < 100:
    cost = units * 5
elif units >= 101 and units <= 200:
    cost = 100 * 5 + (units - 100) * 7
elif units >= 201 and units <= 300:
    cost = 100 * 5 + 100 * 7 + (units - 200) * 10
else:
    cost = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12

# 15% tax addition
total = cost * 1.15
print (f"Total bill: {total:.2f}")
