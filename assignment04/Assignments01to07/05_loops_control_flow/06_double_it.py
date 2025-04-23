# 🔢 Doubling a number until it's at least 100

# Ask the user for a starting number
curr_value = int(input("Enter a number to start doubling: "))

# Handle case where no doubling is needed
if curr_value >= 100:
    print("✅ The number is already 100 or greater. No doubling needed.")
else:
    print("⏩ Doubling the number until it reaches at least 100:")
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=' ')
    print("\n🎯 Done!")
