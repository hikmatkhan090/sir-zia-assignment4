import random

def guess_the_number():
    """Project 2: Guess the Number Game By Computer."""
    number = random.randint(1, 100)
    attempts_left = 7

    # Welcome message
    print("Welcome to the Guess the Number Game!")
    print("I have picked a number between 1 and 100. Let's see if you can guess it.")

    # Loop for guessing
    while attempts_left > 0:
        print(f"\nYou have {attempts_left} guesses remaining.")

        try:
            guess = int(input("Make your guess: "))
        except ValueError:
            print("Oops! That's not a valid number. Please try again.")
            continue

        # Checking the guessed number
        if guess < number:
            print("Your guess is too low! Try again.")
        elif guess > number:
            print("Your guess is too high! Try again.")
        else:
            print(f"Congratulations! You nailed it in {7 - attempts_left + 1} guesses.")
            return  # Exit function after correct guess

        attempts_left -= 1

    # When all guesses are finished
    print(f"\nSorry, you've run out of guesses. The correct number was {number}.")

# Call the function once to start the game
guess_the_number()
