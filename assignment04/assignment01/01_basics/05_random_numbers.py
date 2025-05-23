import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Prints 10 random numbers between 1 and 100 (inclusive)
    """
    print(f"🎲 Generating {N_NUMBERS} random numbers between {MIN_VALUE} and {MAX_VALUE}:")
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=' ')
    print("\n✅ Done!")

if __name__ == '__main__':
    main()
