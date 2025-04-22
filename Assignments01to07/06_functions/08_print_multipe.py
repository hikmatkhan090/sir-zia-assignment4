def print_multiple(message, repeats):
    """Prints the message the specified number of times, each on a new line."""
    for _ in range(repeats):
        print(message)  # Each print automatically adds a newline

def main():
    message = input("Please type a message: ")

    # Add input validation for the repeats variable to ensure it is a positive integer
    while True:
        try:
            repeats = int(input("Enter a number of times to repeat your message: "))
            if repeats > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
