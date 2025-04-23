PROMPT: str = "What do you want? "
JOKE: str = (
    "Here is a joke for you!\n"
    "Sophia is heading out to the grocery store. A programmer tells her: "
    "Get a liter of milk, and if they have eggs, get 12. "
    "Sophia returns with 13 liters of milk. The programmer asks why, and Sophia replies: "
    "'Because they had eggs.'"
)
SORRY: str = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT).strip().lower()
    
    if "joke" in user_input:
        print("\n" + JOKE)
    else:
        print("\n" + SORRY)

if __name__ == "__main__":
    main()
