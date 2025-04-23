# Define gravity constants (relative to Earth's gravity)
GRAVITY_CONSTANTS = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19
}

def main():
    # Prompt the user for their Earth weight
    weight_input = input("🌍 Enter your weight on Earth (e.g., 70 or 70kg): ").strip().lower()
    
    try:
        earth_weight = float(weight_input.replace("kg", ""))
    except ValueError:
        print("❌ Invalid weight input. Please enter a number (e.g., 70 or 70kg).")
        return

    # Prompt the user for a planet name
    planet = input("🪐 Enter the name of a planet: ").strip().capitalize()

    # Check if the planet is valid
    if planet not in GRAVITY_CONSTANTS:
        print("❌ Unknown planet. Please enter one of the following:")
        print(", ".join(GRAVITY_CONSTANTS.keys()))
        return

    # Calculate weight on the selected planet
    gravity = GRAVITY_CONSTANTS[planet]
    planetary_weight = round(earth_weight * gravity, 2)

    # Display the result
    print(f"✅ On {planet}, you would weigh approximately {planetary_weight} kg.")

if __name__ == "__main__":
    main()
