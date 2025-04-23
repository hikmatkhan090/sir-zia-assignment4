def main():
    print("\n\033[1;36m🌡️  Welcome to the Temperature Converter!\033[0m\n")

    fahrenheit = float(input("\033[1m👉 Enter the Fahrenheit temperature: \033[0m"))

   
    celsius = (fahrenheit - 32) * 5.0 / 9.0

   
    print("\n" + "=" * 50)
    print(f"\033[1;3;33m***🔥 Temperature: {fahrenheit:.1f}°F = {celsius:.1f}°C 🔥***\033[0m")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
