def make_sentence(word, part_of_speech):
    """Prints a sentence with the word inserted based on its part of speech."""
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0 (noun), 1 (verb), or 2 (adjective).")

def main():
    word = input("Please type a noun, verb, or adjective: ")

    # Add input validation for the part of speech
    while True:
        try:
            part = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
            if part in [0, 1, 2]:  # Ensuring the part of speech is valid
                break
            else:
                print("Please enter 0, 1, or 2 for noun, verb, or adjective respectively.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
    
    make_sentence(word, part)

if __name__ == '__main__':
    main()
