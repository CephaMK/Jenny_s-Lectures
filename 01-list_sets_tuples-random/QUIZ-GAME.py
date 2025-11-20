#!/usr/bin/python3

#Simple Quiz game

import random

questions = [
         {
             "question": "What is the capital of Kenya?",
             "options": ["1. Nairobi", "2. Mombasa", "3. Kisumu"],
             "answer": "1"
         },
         {
             "question": "Which planet is known as the Red Planet?",
             "options": ["1. Venus", "2. Mars", "3. Jupiter"],
             "answer": "2"
         },
         {
             "question": "Who created Python?",
             "options": ["1. Elon Musk", "2. Bill Gates", "3. Guido van Rossum"],
             "answer": "3"
         }
]

score = 0

random.shuffle(questions)

print("=== Quiz Game ===")

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_ans = input("Your answer: ")

    if user_ans == q["answer"]:
        print("Correct!")
        score += 1
        
    else:
        print("Wrong!")


print(f"\nYour final score: {score}/{len(questions)}")
