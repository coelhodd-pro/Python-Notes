# Structured/Procedural version

import random

def generate_number():
    rand_n = random.randrange(1, 10)
    return rand_n

def main():
    while True:
        rand_n = generate_number()

        try:
            u_input = int(input("What is the number? "))
        except ValueError:
            print("Provide a valid number.")
            continue

        if u_input == rand_n:
            print("You won the game!!! Congratulations!!!")
            break
        else:
            print("You lost. Try again.")

main()