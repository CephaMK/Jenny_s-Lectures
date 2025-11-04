#!/usr/bin/python3

#This program calculates Body Mass Index of a user and provides the weight status of said user.

weight = float(input("Enter your weight in Kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal weight"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print(f"BMI = {bmi:.2f} - {status}")
