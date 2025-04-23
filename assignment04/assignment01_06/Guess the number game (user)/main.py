import random

print("Guess a number between 1 and 100!")
# Generate random number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number: "))

    if guess < number:
        print("Too Low Number!")
    elif guess > number:  # Fixed indentation error
        print("Too High Number!")
    else:
        print("Congratulations! You Got it Right!")
        break