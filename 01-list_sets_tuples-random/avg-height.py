#!/usr/bin/python3

#This code calculates the average heights from a list of heights

print("WELCOME TO MK's AVERAGE HEIGHT CALCULATOR")

height = input("Enter your heights in cm separated by a space: ")
height_list = height.split(" ")

height_list = [int(h) for h in height_list]

count = 0
for i in height_list:
    count += 1

Sum = 0
for person_height in height_list:
    Sum += person_height

avg = Sum / count
print(f"Your average height is {round(avg)}")
