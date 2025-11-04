#!/usr/bin/python3

#This is a program that lists leap years from users start year to end

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

print(f"Leap years from {start} to {end}")
for year in range (start, end + 1):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print(year, end = " ")
