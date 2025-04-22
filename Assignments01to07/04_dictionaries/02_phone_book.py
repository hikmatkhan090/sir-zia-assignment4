def display_header():
    """Show a stylish welcome banner for the phonebook app"""
    print("\n" + "=" * 50)
    print("||" + " " * 46 + "||")
    print("||         📞 PHONEBOOK APPLICATION          ||")
    print("||" + " " * 46 + "||")
    print("=" * 50 + "\n")


def read_phone_numbers(phonebook):
    """
    Prompt user to add contacts (name and number) to the phonebook.
    """
    print("\n" + "-" * 50)
    print("📝 ADD NEW CONTACTS (Leave name empty to finish)")
    print("-" * 50)

    while True:
        name = input("\nName: ").strip()
        if not name:
            break
        number = input("Phone Number: ").strip()
        phonebook[name] = number
        print(f"✅ '{name}' has been saved to your phonebook.")
    
    return phonebook


def print_phonebook(phonebook):
    """
    Display all contacts stored in the phonebook.
    """
    if not phonebook:
        print("\n📭 Your phonebook is currently empty.")
        return

    print("\n" + "-" * 50)
    print("📖 SAVED CONTACTS")
    print("-" * 50)

    for name, number in sorted(phonebook.items()):
        print(f"\n👤 {name.upper():<20} 📞 {number}")

    print("\n" + "-" * 50)
    print(f"Total Contacts: {len(phonebook)}")
    print("-" * 50)


def lookup_numbers(phonebook):
    """
    Let user search for a contact by name.
    """
    if not phonebook:
        print("\n⚠️  Phonebook is empty. Add contacts first!")
        return

    print("\n" + "-" * 50)
    print("🔍 LOOKUP CONTACT (Leave input blank to return)")
    print("-" * 50)

    while True:
        name = input("\nSearch for name: ").strip()
        if not name:
            break

        if name in phonebook:
            print(f"✅ Found: {name} → 📞 {phonebook[name]}")
        else:
            print(f"❌ '{name}' was not found in the phonebook.")


def display_menu():
    """Display main menu and return user's choice"""
    print("\n" + "-" * 50)
    print("📱 MAIN MENU")
    print("-" * 50)
    print("1. ➕ Add a new contact")
    print("2. 📋 View all contacts")
    print("3. 🔎 Find a contact")
    print("4. 🚪 Exit")
    print("-" * 50)
    return input("Choose an option (1-4): ").strip()


def main():
    phonebook = {}
    display_header()

    while True:
        choice = display_menu()

        if choice == "1":
            read_phone_numbers(phonebook)
        elif choice == "2":
            print_phonebook(phonebook)
        elif choice == "3":
            lookup_numbers(phonebook)
        elif choice == "4":
            print("\n" + "=" * 50)
            print("👋 Thanks for using the Phonebook App. Goodbye!")
            print("=" * 50 + "\n")
            break
        else:
            print("\n⚠️  Invalid option. Please select between 1 and 4.")


if __name__ == '__main__':
    main()
