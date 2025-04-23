import random
from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

def print_colored(text, color=Fore.WHITE, delay=0.01):
    """Prints text in the specified color with typing effect."""
    for char in text:
        print(color + char + Style.RESET_ALL, end='', flush=True)
        time.sleep(delay)
    print()

def countdown():
    print_colored("\nGet ready!", Fore.LIGHTCYAN_EX)
    for i in range(3, 0, -1):
        print_colored(f"{i}...", Fore.YELLOW)
        time.sleep(0.5)
    print_colored("GO!\n", Fore.GREEN)
    time.sleep(0.5)

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 0
    max_rounds = 5

    print_colored("="*60, Fore.LIGHTMAGENTA_EX)
    print_colored("🎮 Welcome to the Ultimate Rock, Paper, Scissors Showdown! 🎮", Fore.CYAN)
    print_colored("="*60, Fore.LIGHTMAGENTA_EX)
    print_colored(f"\nYou’ll face off against the computer in {max_rounds} intense rounds!\n", Fore.LIGHTYELLOW_EX)

    while rounds < max_rounds:
        rounds += 1
        print_colored(f"\n🎯 Round {rounds} of {max_rounds}", Fore.LIGHTMAGENTA_EX)
        print_colored("-"*30, Fore.LIGHTBLACK_EX)
        user_choice = input("🧠 Choose (rock/paper/scissors) or 'q' to quit: ").strip().lower()

        if user_choice == 'q':
            print_colored("\n🚪 Exiting the game. See you next time!", Fore.LIGHTMAGENTA_EX)
            return

        if user_choice not in choices:
            print_colored("❗ Invalid choice! Please type rock, paper, or scissors.", Fore.RED)
            rounds -= 1
            continue

        computer_choice = random.choice(choices)
        countdown()
        print_colored(f"🧑 You picked: {user_choice}", Fore.LIGHTBLUE_EX)
        print_colored(f"🤖 Computer picked: {computer_choice}", Fore.LIGHTBLUE_EX)

        if user_choice == computer_choice:
            print_colored("⚖️ It's a tie this round!", Fore.YELLOW)
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print_colored("🔥 You win this round!", Fore.GREEN)
            user_score += 1
        else:
            print_colored("💥 Computer wins this round!", Fore.RED)
            computer_score += 1

        print_colored(f"📊 Scoreboard → You: {user_score} | Computer: {computer_score}", Fore.LIGHTMAGENTA_EX)

    print_colored("\n🏁 Final Results 🏁", Fore.LIGHTCYAN_EX)
    print_colored("-"*60, Fore.LIGHTBLACK_EX)
    if user_score > computer_score:
        print_colored("🏆 You are the CHAMPION! Well played!", Fore.GREEN)
    elif user_score < computer_score:
        print_colored("🤖 The computer wins! But you put up a great fight!", Fore.RED)
    else:
        print_colored("🤝 It's a perfect tie! What a match!", Fore.YELLOW)
    print_colored(f"\nFinal Score → You: {user_score} | Computer: {computer_score}", Fore.LIGHTGREEN_EX)

    play_again = input("\n🔁 Want to challenge the computer again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        print_colored("\n🔄 Restarting the game...\n", Fore.LIGHTCYAN_EX)
        rock_paper_scissors()
    else:
        print_colored("\n👋 Thanks for playing! Stay sharp, champion!", Fore.LIGHTMAGENTA_EX)

# Start the game
if __name__ == "__main__":
    rock_paper_scissors()
