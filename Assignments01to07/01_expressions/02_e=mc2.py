C: int = 299792458 
def main():
    mass_in_kg: float = float(input("Enter mass in kilograms: "))

    energy_in_joules: float = mass_in_kg * (C ** 2)

    
    print("\ne = m × c²")
    print("Mass (m) = " + str(mass_in_kg) + " kg")
    print("Speed of light (c) = " + str(C) + " m/s")
    
    print("\nTotal energy = " + str(energy_in_joules) + " joules")

if __name__ == '__main__':
    main()
