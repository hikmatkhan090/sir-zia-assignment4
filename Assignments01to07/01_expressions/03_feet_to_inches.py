"""
A simple program that uses a constant to convert feet to inches.
"""

INCHES_IN_FEET: int = 12 
def main():
    feet: float = float(input("Enter the number of feet: ")) 
    inches: float = feet * INCHES_IN_FEET  
    print("That's equal to", inches, "inches!")

if __name__ == '__main__':
    main()
