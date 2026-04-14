import random

number = random.randint(1, 10)
correct = False

while not correct:
    attempt = int(input("Guess the number (1 to 10): "))

    if attempt == number:
        print("Correct! You guessed the number.")
        correct = True
    else:
        print("Incorrect, try again.")