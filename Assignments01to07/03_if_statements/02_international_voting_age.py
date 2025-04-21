PETURKSBOUIPO_MIN_AGE: int = 16
STANLAU_MIN_AGE: int = 25
MAYENGUA_MIN_AGE: int = 48

def main():
    # Ask the user for their age
    user_age = int(input("Please enter your age: "))
    print("\n🔍 Checking where you're eligible to vote...\n")

    # Peturksbouipo check
    if user_age >= PETURKSBOUIPO_MIN_AGE:
        print(f"✅ You ARE eligible to vote in Peturksbouipo! (Minimum age: {PETURKSBOUIPO_MIN_AGE})")
    else:
        print(f"❌ You are NOT eligible to vote in Peturksbouipo. (Must be at least {PETURKSBOUIPO_MIN_AGE})")

    # Stanlau check
    if user_age >= STANLAU_MIN_AGE:
        print(f"✅ You CAN vote in Stanlau! (Voting age: {STANLAU_MIN_AGE})")
    else:
        print(f"❌ You CANNOT vote in Stanlau yet. (You need to be {STANLAU_MIN_AGE} or older)")

    # Mayengua check
    if user_age >= MAYENGUA_MIN_AGE:
        print(f"✅ Great! You're eligible to vote in Mayengua. (Minimum voting age: {MAYENGUA_MIN_AGE})")
    else:
        print(f"❌ Sorry, you're not old enough to vote in Mayengua. (Required age: {MAYENGUA_MIN_AGE})")

    print("\n🗳️ Stay informed, and make your vote count wherever you're eligible!")


if __name__ == '__main__':
    main()
