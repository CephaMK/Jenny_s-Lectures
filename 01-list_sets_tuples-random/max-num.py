#!/usr/bin/python3

#This code finds the maximum number from a list of numbers

print("WELCOME TO MK's MAXIMUM NUMBER FINDER")
numbers = input("Enter numbers separated by a comma: ")
number_list = numbers.split(",")

number_list = [int(n) for n in number_list]  #Convert each input in the list into an int
print(number_list)

max_num = number_list[0]
for num in number_list:
    if num > max_num:
        max_num = num

print(f"The maximum number is: {max_num}")
