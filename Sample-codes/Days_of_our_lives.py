#!/usr/bin/python3

# This is a simple program showing the number of days, weeks, months we have left as per the assumption we live until 90years old

#Year = 365 Days
#Year = 52 weeks
#Year = 12 months

age = int (input("What is your age?\n"))
left_years = 90 - age

days = left_years * 365
weeks = left_years * 52
months = left_years * 12

print(f"You have {days} days, {weeks} weeks, {months} months, {left_years} years left")


