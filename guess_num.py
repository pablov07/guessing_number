"""
Guessing game with limited attempts to guess the number correctly.
"""

import random
import sys

print("Guessing Number Game! \n3 attempts to guess number correctly.")

number = random.randint(1,9)

CHANCES = 0

print("Guess a number(1-9):")

while True:

    guess = int(input())

    if guess == number:
        print(f"YOU GUESSED CORRECTLY! THE NUMBER WAS {number} \
              AND YOU DID IT IN {CHANCES} ATTEMPTS!")
        break

    if guess < number:
        print(f"Guess was low. Guess again. (Attempt: {CHANCES+1})", guess)

    else:
        print(f"Guess was high. Guess again. (Attempt: {CHANCES+1})", guess)

    CHANCES += 1

    if CHANCES == 3:
        print("Ran out of chances. You Lose.")
        sys.exit(0)
