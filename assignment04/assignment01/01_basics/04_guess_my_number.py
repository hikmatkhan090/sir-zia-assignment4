import random

def main():
    # Generate a random secret number
    secret_number: int = random.randint(1, 99)
    print("🎲 I am thinking of a number between 1 and 99...")

    while True:
        try:
            guess: int = int(input("Enter your guess: "))
            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Congrats! You guessed it. The number was {secret_number}.")
                break
        except ValueError:
            print("Please enter a valid integer.\n")

if __name__ == '__main__':
    main()
