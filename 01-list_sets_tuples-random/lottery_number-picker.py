#!/usr/bin/python3

#This code selsects 6 unique numbers between 1 - 49 like a real lottery

import random

print("Welcome to MK's Lottery Number Picker")

numbers = set()

while len(numbers) < 6:
        numbers.add(random.randint(1, 49))

        lottery_numbers = sorted(numbers)

        print("Your lottery numbers are:", lottery_numbers)

