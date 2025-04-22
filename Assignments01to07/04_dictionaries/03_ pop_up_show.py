def display_welcome():
    """Show a warm welcome and list of available fruits"""
    print("\n" + "=" * 50)
    print("||" + " " * 46 + "||")
    print("||         🍓 FRUIT SHOP CALCULATOR         ||")
    print("||" + " " * 46 + "||")
    print("=" * 50)
    print("\nHello and welcome to our Fruit Shop!")
    print("Check out our delicious fruits and their prices:\n")

def display_fruits(fruits):
    """Show the fruit selection and their prices"""
    for fruit, price in fruits.items():
        print(f"- {fruit.capitalize():<10} → ${price:.2f} each")
    print("\n" + "-" * 50 + "\n")

def calculate_total(fruits):
    """Prompt the user for quantities and calculate the total cost"""
    total = 0.0

    for fruit in fruits:
        while True:
            try:
                quantity = input(f"How many {fruit}(s) would you like to buy? ").strip()
                if quantity == "":
                    quantity = 0
                quantity = int(quantity)
                if quantity < 0:
                    print("⚠️ Please enter a number that's zero or more.")
                    continue
                total += quantity * fruits[fruit]
                break
            except ValueError:
                print("❌ That doesn't look like a number. Try again.")
    
    return total

def display_receipt(total):
    """Show the final total with a thank-you note"""
    print("\n" + "=" * 50)
    print("\n🧾 Generating your bill...\n")
    print(f"💰 Total Amount Due: ${total:.2f}")
    print("\n" + "=" * 50)
    print("🙏 Thank you for shopping with us!")
    print("✨ We hope to see you again soon! ✨\n")
    print("=" * 50)

def main():
    # Fruits available with their prices
    fruits = {
        'apple': 1.5,
        'durian': 15.0,
        'jackfruit': 10.0,
        'kiwi': 2.5,
        'rambutan': 5.0,
        'mango': 3.0
    }

    display_welcome()
    display_fruits(fruits)
    total = calculate_total(fruits)
    display_receipt(total)

if __name__ == '__main__':
    main()
