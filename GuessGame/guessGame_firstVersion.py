# Imperative version

import random

number = random.randrange(1, 10)
u_input = int(input("Provide your input: "))

if u_input == number:
    print("You won the game!!! Congratulations!!!")
else:
    print("You lost. Try again.")