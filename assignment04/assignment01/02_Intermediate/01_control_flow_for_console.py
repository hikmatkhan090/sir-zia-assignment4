import random

NUM_ROUNDS = 5

def main():
    print("🎮 Welcome to the High-Low Game!")
    print('--------------------------------\n')

    your_score = 0

    for i in range(NUM_ROUNDS):
        print(f"🔢 Round {i + 1}")
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is: {your_num}")

        choice = input("Do you think your number is *higher* or *lower* than the computer's?: ").strip().lower()
        while choice not in ["higher", "lower"]:
            choice = input("Please enter either 'higher' or 'lower': ").strip().lower()

        # Determine result
        correct_guess = (
            (choice == "higher" and your_num > computer_num) or
            (choice == "lower" and your_num < computer_num)
        )

        if correct_guess:
            print(f"✅ Correct! The computer's number was {computer_num}.")
            your_score += 1
        else:
            print(f"❌ Incorrect. The computer's number was {computer_num}.")

        print(f"📊 Your score is now: {your_score}\n")

    # Final score message
    print(f"🏁 Game Over! Your final score is {your_score}/{NUM_ROUNDS}")

    if your_score == NUM_ROUNDS:
        print("🌟 Incredible! You got them all right!")
    elif your_score > NUM_ROUNDS // 2:
        print("👍 Great job! You know your intuition!")
    else:
        print("💡 Keep practicing — you’ll get better!")

if __name__ == "__main__":
    main()
