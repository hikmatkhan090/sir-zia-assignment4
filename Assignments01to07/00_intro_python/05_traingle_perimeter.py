def main():
    print("\n\033[1m📐 Triangle Perimeter Calculator 🧮\033[0m\n")

    
    side1 = float(input("\033[1mEnter the length of side 1 of the triangle: \033[0m"))
    side2 = float(input("\033[1mEnter the length of side 2 of the triangle: \033[0m"))
    side3 = float(input("\033[1mEnter the length of side 3 of the triangle: \033[0m"))

    
    perimeter = side1 + side2 + side3

    
    print(f"\n\033[1mThe perimeter of the triangle is: {perimeter}\033[0m\n")

if __name__ == "__main__":
    main()

