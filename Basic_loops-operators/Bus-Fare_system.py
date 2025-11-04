#!/usr/bin/python3

#This program contains a simulation of a simple bus fare system dependent on age and distance travelled

age = int(input("Enter age: "))
distance = float(input("Enter distance in kilometers: "))

fare = distance * 10

if age < 12:
    fare *= 0.5
if age >= 60:
    fare *= 0.7

print(f"Final fare: {fare:.2f}")
