#!/usr/bin/python3

print("WELCOME TO MK LOVE CALCULATOR")

name1 = input("Romantic 1 please enter your name: ").lower()
name2 = input("Romantic 2 please enter your name: ").lower()

love_name = name1 + name2

t = love_name.count('t')
r = love_name.count('r')
u = love_name.count('u')
e = love_name.count('e')
true = t + r + u + e

l = love_name.count('l')
o = love_name.count('o')
v = love_name.count('v')
e = love_name.count('e')
love = l + o + v + e

love_result = int(str(true) + str(love))

print(f"Your love score is {love_result}")

if love_result <= 30:
    print("LOW COMPATIBILITY!")
elif love_result <= 70:
    print("You are alright together")
elif 70 < love_result < 85:
    print("You are great together")
else:
    print("Your love is like coke and mentos. EXPLOSIVE!!!")
