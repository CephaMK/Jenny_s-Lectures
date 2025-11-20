#!/usr/bin/python3

'''
This code looks for numbers among 1-100 divisible by 3, 5 and by both 3 and 5 
For numbers divisible by 3 it prints fizz for numbers divisble by 5 it prints buzz
For numbers divisible by both 3 and 5 it prints fizzbuzz

'''

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    else:
        print(number)
