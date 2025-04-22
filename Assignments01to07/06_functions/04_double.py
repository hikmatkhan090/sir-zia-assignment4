def double(num: int) -> int:
    """Return the double of the given number."""
    return num * 2

def main():
    try:
        num = int(input("Enter a number: "))
        num_times_2 = double(num)
        print(f"The double of {num} is {num_times_2}.")
    except ValueError:
        print("Oops! Please enter a valid integer.")

if __name__ == '__main__':
    main()
