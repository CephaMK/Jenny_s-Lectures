#!/usr/bin/python3

#This is a simple love calculator that tests a couple's compatibility as per the number of
#occurences of the characters 'T''R''U''E' 'L''O''V''E' in their names.

print("Welcome to MK Love Calculator")

persona1 = input("Persona 1 please enter your full names: ").upper()
persona2 = input("Persona 2 please enter your full names: ").upper()

love_name = persona1 + persona2

T = love_name.count('T')
R = love_name.count('R')
U = love_name.count('U')
E = love_name.count('E')
TRUE = T + R + U + E

L = love_name.count('L')
O = love_name.count('O')
V = love_name.count('V')
E = love_name.count('E')
LOVE = L + O + V + E


love_result = int(str(TRUE) + str(LOVE))

print("Your love result is ", love_result)

if love_result <= 30:
    print("VERY LOW COMPATIBILITY")
elif love_result <= 70:
    print("YOU ARE ALRIGHT TOGETHER")
elif love_result > 70 and love_result < 85:
    print("YOU ARE GREAT TOGETHER")
else:
    print("YOUR LOVE IS LIKE COKE & MENTOS. EXPLOSIVE!!!")
