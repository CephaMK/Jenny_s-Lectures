#!/usr/bin/python3

'''
This code:
Asks the user for a sentence.
Splits it into words.
Uses set function to find unique words.
Displays how many unique words are in the sentence.

'''
sentence = input("Enter a sentence: ")

words = sentence.lower().split()      # list of words
unique_words = set(words)             # removes duplicates

print(f"\nTotal words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Unique list: {unique_words}")
