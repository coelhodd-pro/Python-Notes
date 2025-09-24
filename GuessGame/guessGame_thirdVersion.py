# Object Oriented version

import random

class Game:
    def __init__(self):
        self.random_number = self.generate_number()

    def generate_number(self):
        random_number = random.randrange(1, 10)
        return random_number

    def play(self):
        while True:
            try:
                u_input = int(input("What is the number? "))
            except ValueError:
                print("Provide a valid number.")
                continue

            if u_input == self.random_number:
                print("Congratulations!!! You won!!!")
                break
            else:
                print("You lost. Try again.")

game = Game()
game.play()