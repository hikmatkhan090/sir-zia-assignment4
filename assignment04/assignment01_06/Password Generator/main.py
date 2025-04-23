import random
import string

def generate_password(length, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 60)
    print("🔐 WELCOME TO THE ULTIMATE PASSWORD GENERATOR 🔐".center(60))
    print("=" * 60)

    while True:
        try:
            length = int(input("\n🔢 Enter desired password length (minimum 4): "))
            if length < 4:
                print("❗ Oops! Password must be at least 4 characters long. Try again.")
                continue
            break
        except ValueError:
            print("❗ Please enter a valid numeric value.")

    choice = input("🔧 Would you like to include special characters? (yes/no): ").strip().lower()
    use_special = choice in ['yes', 'y']

    password = generate_password(length, use_special)

    print("\n" + "-" * 60)
    print("✅ Your Secure Password Has Been Successfully Generated!")
    print(f"🔑 Generated Password: {password}")
    print(f"🔒 Password Strength: {len(password)} characters long")
    print("-" * 60)
    print("💡 Tip: Save your password in a secure password manager.\n")

if __name__ == "__main__":
    main()
