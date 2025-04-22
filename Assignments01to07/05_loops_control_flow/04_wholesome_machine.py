AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    """Affirmation practice program — helps you memorize a positive statement."""
    print("\n🌟 AFFIRMATION PRACTICE 🌟\n")
    print("Please type the following affirmation exactly as shown:\n")
    print(f"👉 \"{AFFIRMATION}\"\n")

    user_feedback = input("Your turn: ")

    while user_feedback != AFFIRMATION:
        print("\n❌ Oops! That's not quite right.")
        print("Let's try again. Repeat the affirmation below:\n")
        print(f"👉 \"{AFFIRMATION}\"\n")
        user_feedback = input("Your turn: ")

    print("\n✅ That's correct! Well done! 🌈 Keep believing in yourself!")

if __name__ == '__main__':
    main()
