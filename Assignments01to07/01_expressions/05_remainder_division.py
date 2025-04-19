def main():
    dividend: int = int(input("Enter the dividend (number to be divided): "))
    divisor: int = int(input("Enter the divisor (number to divide by): "))

    quotient: int = dividend // divisor 
    remainder: int = dividend % divisor  
    
    print("Result: " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
    main()
