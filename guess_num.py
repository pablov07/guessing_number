"""
Guessing game with limited attempts to guess the number correctly.
"""

import random
import sys

print("Guessing Number Game! \n3 attempts to guess number correctly.")

#Initializing the range of numbers to be guessed
number = random.randint(1,9)

#Initialze 0 chances have been taken
CHANCES = 0

print("Guess a number(1-9):")

while True:
    #User inputs guess
    guess = int(input())

    #User guessed correctly!
    if guess == number:
        print(
            f'YOU GUESSED CORRECTLY! THE NUMBER WAS {number} AND YOU DID IT IN {CHANCES} ATTEMPT(S)!')
        break

    #Guess was low and asked to attempt again
    if guess < number:
        print(f"Guess was low. (Attempt: {CHANCES+1})", guess)
        CHANCES += 1

    #Guess was high and asked to attempt again
    else:
        print(f"Guess was high. (Attempt: {CHANCES+1})", guess)
        CHANCES += 1

    #Limited attempts to 3 and quits program
    if CHANCES == 3:
        print("Ran out of chances. You Lose.")
        sys.exit(0)
