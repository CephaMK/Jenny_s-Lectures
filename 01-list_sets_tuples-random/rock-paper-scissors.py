#!/usr/bin/python3

#This code provides a CLI environment for a user to play ROCK PAPER SCISSORS against the computer

import random

print("WELCOME TO MK's ROCK PAPER SCISSORS")
Player = int(input("Enter 0 for R0CK. 1 for PAPER. 2 for SCISSORS: "))

comp = random.randint(0, 2)
print("Computer chose", comp)

if 0 <= Player <= 2:
    if Player == 0 and comp == 2:
        print("YOU WIN")
    elif Player == 2 and comp == 0:
        print("YOU LOSE")
    elif Player == comp:
        print("DRAW")
    elif Player < comp:
        print("YOU LOSE")
    elif Player > comp:
        print("YOU WIN")
else:
    print("INVALID INPUT!! YOU LOSE")
