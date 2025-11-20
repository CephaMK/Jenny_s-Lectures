#!/usr/bin/python3
'''
This code generates random password as per the number of letters, numbers and 
special characters the user wishes for in the password

'''

import random
import string

print("WELCOME TO MK's PASSWORD GENERATOR")
n_letters = int(input("How many letters would you like in your password: "))
n_num = int(input("How many numbers would you like in your password: "))
n_symbols = int(input("How many symbols would you like in your password: "))

password_list = []
for i in range (1, n_letters + 1):
    char = random.choice(string.ascii_letters)
    password_list += char

for i in range(1, n_num + 1):
    num = random.choice(string.digits)
    password_list += num

for i in range (1, n_symbols):
    symbol = random.choice(string.punctuation)
    password_list += symbol

random.shuffle(password_list)

password = " "
for each_char in password_list:
    password += each_char

print(password)

