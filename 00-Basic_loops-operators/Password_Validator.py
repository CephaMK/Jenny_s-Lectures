#!/usr/bin/python3

#This program checks for the strength of the user's choice for a password

password = input ("Enter password: ")

has_upper = any(ch.isupper() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in "$%#@!*&()?" for ch in password)

if len(password) >= 8 and has_upper and has_digit and has_special:
    print("Strong password")
else:
    print("Weak password")
