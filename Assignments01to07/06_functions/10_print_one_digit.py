def print_ones_digit(num):
    """Prints the ones digit of a number."""
    ones_digit = num % 10
    print(f"The ones digit of {num} is {ones_digit}")

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            print_ones_digit(num)
            break  # Exit the loop after valid input
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == '__main__':
    main()
