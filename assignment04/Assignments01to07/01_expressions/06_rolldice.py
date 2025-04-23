import random


NUM_SIDES: int = 6

def main():
  
    
    
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
   
    total: int = die1 + die2
    
    
    print("🎲 Each die has", NUM_SIDES, "sides.")
    print("🎲 First roll:", die1)
    print("🎲 Second roll:", die2)
    print("🧮 Total of both dice:", total)

if __name__ == '__main__':
    main()
