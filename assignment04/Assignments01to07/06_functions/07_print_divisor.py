def print_divisors(num: int):
    """Print the divisors of the given number."""
    print(f"Here are the divisors of {num}:")
    for i in range(1, num + 1):  # Start from 1 and go up to num
        if num % i == 0:
            print(i)

def main():
    num = int(input("Enter a number: "))
    if num > 0:
        print_divisors(num)
    else:
        print("Please enter a positive number.")

if __name__ == '__main__':
    main()
