MINIMUM_HEIGHT: int = 50  

def main():
    """Checks if the user's height meets the ride requirement."""
    try:
        height = float(input("Enter your height in centimeters: "))
        
        if height >= MINIMUM_HEIGHT:
            print(f"\n🎉 Woohoo! You're {height}cm tall — that's tall enough to hop on the ride!")
        else:
            needed = MINIMUM_HEIGHT - height
            print(f"\n📏 You're {height}cm tall. Just {needed:.1f}cm more and you'll be ready to ride. Hang in there!")
    
    except ValueError:
        print("⚠️ Oops! Please enter a number for your height.")

if __name__ == '__main__':
    main()
