def main():
    # Get initial number from user
    curr_value = int(input("Enter a number: "))

    # Check if doubling is needed
    if curr_value >= 100:
        print("The number is already 100 or more. No doubling needed.")
    else:
        print("Doubling the number until it reaches 100 or more:")
        while curr_value < 100:
            curr_value *= 2
            print(curr_value, end=' ')
        print()  # Add a newline at the end

if __name__ == "__main__":
    main()
