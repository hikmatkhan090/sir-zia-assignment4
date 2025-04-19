def main():
    animal = input("🐾 What's your favorite animal? ").upper()

    print("\n" + "*" * 50)
    print(f"\033[1m**🔥 MY FAVORITE ANIMAL IS ALSO {animal}! 🔥**\033[0m")
    print("*" * 50 + "\n")

if __name__ == "__main__":
    main()
