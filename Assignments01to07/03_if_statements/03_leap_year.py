def main():
    year = int(input("Enter a year to check if it's a leap year: "))

    # A leap year is divisible by 4, but centuries must also be divisible by 400
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"✅ {year} is a leap year! (Divisible by 400)")
            else:
                print(f"❌ {year} is NOT a leap year. (Divisible by 100 but not by 400)")
        else:
            print(f"✅ {year} is a leap year! (Divisible by 4 but not by 100)")
    else:
        print(f"❌ {year} is NOT a leap year. (Not divisible by 4)")

    print("\n📅 Leap years help keep our calendar in sync with the Earth’s orbit!")


if __name__ == '__main__':
    main()
