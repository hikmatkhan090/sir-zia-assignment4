import time

def countdown_timer(time_in_seconds):
    print(f"Starting countdown for {time_in_seconds} seconds...\n")
    while time_in_seconds:
        mins, secs = divmod(time_in_seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_in_seconds -= 1
    print("00:00")
    print("Time's up!\a")  # System bell

def main():
    try:
        total_seconds = int(input("Enter the time in seconds for countdown: "))
        if total_seconds < 0:
            raise ValueError("Time must be non-negative.")
        countdown_timer(total_seconds)
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
