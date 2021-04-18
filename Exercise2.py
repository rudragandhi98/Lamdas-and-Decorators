# Create a Python project to guess a number that has randomly selected.
import random

random_number = lambda x: random.randint(0, x)
num = random_number(100)


while True:
    user_input = (int(input("Please guess a number between 0 to 100: ")))
    if user_input > num:
        print("Your guess is greater")
    elif user_input < num:
        print("Your guess is less")
    else:
        print("You got it!!")
        break
