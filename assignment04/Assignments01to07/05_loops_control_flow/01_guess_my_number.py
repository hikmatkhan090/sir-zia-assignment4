import random

def main():
    # Generate the secret number randomly between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("\n🎲 I'm thinking of a number between 1 and 99...")
    print("Can you guess what it is?\n")

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            
            if guess < 1 or guess > 99:
                print("⚠️ Please enter a number *between* 1 and 99.\n")
                continue

            if guess < secret_number:
                print("📉 Too low!\n")
            elif guess > secret_number:
                print("📈 Too high!\n")
            else:
                print(f"🎉 Congrats! You guessed it right — the number was {secret_number}.\n")
                break

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

if __name__ == '__main__':
    main()
