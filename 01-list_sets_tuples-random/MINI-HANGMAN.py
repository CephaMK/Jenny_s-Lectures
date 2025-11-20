#!/usr/in/python3

'''

This code:
Picks a random word from a list.
Displays underscores for hidden letters.
Asks the user to guess letters until they guess the full word or run out of attempts.

'''

import random

print("WELCOME TO MK's MINI HANGMAN GAME")

words = ["python", "computer", "student", "program"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 7

print("=== Guess the Word ===")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print(f"Attempts left: {attempts}")

    letter = input("Guess a letter: ").lower()

    #input validation
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter ONE letter ")
        continue

    if letter in word:
        print("Correct!")

        for i, ch in enumerate(word):
            if ch == letter:
                guessed[i] = letter
                
    else:
        print("Wrong guess.")
        attempts -= 1

    
    if "_" not in guessed:
        print("\n🎉 You guessed the word:", word)
        break
    
if "_" in guessed:
    print("\n❌ You lost! The word was:", word)




