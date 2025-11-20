#!/usr/bin/python3

#This a virtual simulation of a coin toss head/tails.

import random

toss = random.randint(0, 1)

if toss == 1:
    print("Heads")
else: 
    print("tails")
