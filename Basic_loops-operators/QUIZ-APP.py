#!/usr/bin/python3

#This program simulates a simple QUIZ app with multiple choice answers and that keeps track of the users scores

print("Welcome to MK Quiz App")

score = 0

#Question 1
ans = input("1.What does C.P.U stand for?\n a.Central Processing Unit\n b.Computer Personal Unit\n c.Central Power Unit\n YOUR ANSWER: ").lower()

if ans == "a":
    print("CORRECT!\n")
    score += 1
else:
    print ("WRONG. It's (a) Central Processing Unit")

#Question 2
ans = input("Which word is used to create a function in python?\n a.def\n b.func\n c.define\n YOUR ANSWER: ").lower()

if ans == "a":
    print("CORRECT!\n")
    score += 1
else:
    print("Wrong. Correct answer is (a) def\n")

#Quwstion 3
ans = input("3.What symbol is used for comments in python?\n a.//\n b.#\n c./* */\n YOUR ANSWER: ").lower()

if ans == "b":
    print("CORRECT!\n")
    score += 1
else:
    print("WRONG. It's (b) #\n")

#Scoring track
print(f"You got {score}/3 correct!")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good job")
else:
    print ("Keep practising")
