MAX_TERM_VALUE: int = 10000

def main():
    """Print all Fibonacci numbers up to a maximum value."""
    curr_term = 0  # 0th Fibonacci number
    next_term = 1  # 1st Fibonacci number

    print("\n📜 Fibonacci Sequence up to", MAX_TERM_VALUE, ":\n")

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print numbers on the same line with space
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

    print("\n\n✅ Sequence complete!")

if __name__ == '__main__':
    main()
