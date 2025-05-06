# Problem Statement:

# Develop a Python program for a number guessing game with the following requirements:

# 1. Random Number Generation: Utilize the `random` library to generate a random number between 1 and 100.

# 2. Guess Attempts: The player should be allowed 1 attempt to guess the number.

# 3. Feedback Mechanism: After each guess, the program should provide feedback to the player:
# - If the guessed number is higher than the random number, display "Too high!"
# - If the guessed number is lower than the random number, display "Too low!"
# - If the guessed number matches the random number, display a congratulatory message.

# This program will simulate a fun and interactive game where players can practice their guessing skills within a limited number of attempts,
#  leveraging Python's `random` library for randomness.

import random

def randomguess(user_input):
    random_num = random.randint(1,100)
    if user_input < random_num :
        print("Too low!")
    elif user_input > random_num :
        print("Too high!")
    else:
        print("congratulation, you gussed it right!")

while True:
    try:
        user_input = int(input("enter a number between 1 to 100\n"))
        break
    except ValueError:
        print("looks like you entered an alphabet or special char")
        

randomguess(user_input)