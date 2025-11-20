#!/usr/bin/python3

#This program gives the number and type of roots as per the inputs a user provides from a quadratic equation.

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b ** 2 - 4 * a * c #Value of the discriminant

if D > 0:
    print("Two real roots")
elif D == 0:
    print("One real root")
else:
    print("Complex roots")
