import random

TOTAL_NUMBERS: int = 10
MIN_LIMIT: int = 1
MAX_LIMIT: int = 100

def main():
    
    random_numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(TOTAL_NUMBERS)]
    
    print(f"🎲 Here are {TOTAL_NUMBERS} randomly generated numbers between {MIN_LIMIT} and {MAX_LIMIT}:")
    print(random_numbers)
    
   
    print("\n📊 Stats Summary:")
    total = sum(random_numbers)
    average = total / len(random_numbers)
    print(f"➕ Total: {total}")
    print(f"📈 Average: {average:.2f}")
    print(f"🔺 Highest Number: {max(random_numbers)}")
    print(f"🔻 Lowest Number: {min(random_numbers)}")

if __name__ == '__main__':
    main()
