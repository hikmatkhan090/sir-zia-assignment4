def main():
    for i in range(10, 20):  # Iterate from 10 to 19
        if is_odd(i):
            print(f"{i} is odd")
        else:
            print(f"{i} is even")

def is_odd(value: int) -> bool:
    """Returns True if the value is odd, False otherwise."""
    return value % 2 != 0  # Check if the number is odd

if __name__ == '__main__':
    main()
