import random
import sys

WORDS = {
    "easy": ["moon", "book", "fish", "cake", "rain"],
    "medium": ["guitar", "flower", "planet", "coffee", "rocket"],
    "hard": ["adventure", "universe", "algorithm", "chocolate", "astronomy"]
}

HINTS = {
    "easy": ["It's in the sky", "You read it", "Swims in water", "Sweet dessert", "Falls from clouds"],
    "medium": ["Musical instrument", "Blooms in spring", "Orbits the sun", "Morning drink", "Goes to space"],
    "hard": ["Exciting journey", "Everything that exists", "Coding logic", "Sweet treat", "Study of stars"]
}

def choose_random_word(difficulty):
    combined = list(zip(WORDS[difficulty], HINTS[difficulty]))
    random.shuffle(combined)
    return combined[0]

def display_current_state(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)

def play_round(round_number, difficulty):
    word, hint = choose_random_word(difficulty)
    guessed_letters = set()
    remaining_attempts = 6
    hint_used = False

    print(f"\n🎯 Round {round_number} - Difficulty: {difficulty.capitalize()}")
    print(f"Word: {display_current_state(word, guessed_letters)}")
    print(f"Attempts Left: {remaining_attempts} | Type 'hint' to reveal a clue")

    while remaining_attempts > 0:
        guess = input("🔤 Guess a letter: ").strip().lower()

        if not guess.isalpha() and guess != "hint":
            print("❗ Invalid input. Please enter a valid letter.")
            continue

        if guess == "hint":
            if not hint_used:
                print(f"\n💡 Hint: {hint}")
                unrevealed = [c for c in word if c not in guessed_letters]
                if unrevealed:
                    revealed = random.choice(unrevealed)
                    guessed_letters.add(revealed)
                    print(f"✨ Bonus Letter Revealed: '{revealed}'\n")
                hint_used = True
            else:
                print("⚠️ Hint already used!")
        elif guess in guessed_letters:
            print("🔁 You've already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            print("✅ Correct guess!")
        else:
            remaining_attempts -= 1
            print(f"❌ Incorrect! Attempts Left: {remaining_attempts}")

        print(display_current_state(word, guessed_letters))

        if all(char in guessed_letters for char in word):
            print("🎉 Congratulations! You guessed the word!")
            return 1

    print(f"💔 Sorry, you lost this round. The correct word was: {word}")
    return -1

def game():
    print("🔥 Welcome to the Ultimate Hangman Challenge 🔥")

    while True:
        difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        while difficulty not in WORDS:
            print("❌ Invalid choice. Please try again.")
            difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()

        score = 0
        for round_num in range(1, 6):
            result = play_round(round_num, difficulty)
            score += result
            print(f"📊 Your current score: {score}\n")

        print("🏁 Game Over")
        if score >= 3:
            print(f"🏆 Well done! Final Score: {score}")
        elif score >= 0:
            print(f"😊 Great try! Final Score: {score}")
        else:
            print(f"💪 Keep practicing! Final Score: {score}")

        again = input("\n🔁 Would you like to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing. See you next time!")
            break
        print("\n🚀 Restarting the game...\n")

# Start the game
if __name__ == "__main__":
    game()
