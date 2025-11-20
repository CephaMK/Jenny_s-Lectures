#!/usr/bin/python3

#This code specifies the type of traingle based on the inputs provided by the user.

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a: #Checking if it is a triangle using traingle equality rule
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene traingle")
else:
    print("Not a valid triangle")
