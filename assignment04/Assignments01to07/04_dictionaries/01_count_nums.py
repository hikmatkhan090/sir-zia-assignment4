def count_numbers():
    numbers = []
    frequency = {}

    print("🔢 Enter numbers one by one. Press Enter without typing anything to stop.")

    while True:
        entry = input("Enter a number: ")
        if entry == "":
            break
        try:
            number = int(entry)
            numbers.append(number)
        except ValueError:
            print("❌ That's not a valid number. Try again or press Enter to stop.")

    
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    print("\n📊 Number Frequencies:")
    for number, count in sorted(frequency.items()):
        times = "time" if count == 1 else "times"
        print(f"🔹 {number} appears {count} {times}.")


count_numbers()
