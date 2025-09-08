# Use a while loop and the time.sleep() function to create a simple countdown from a given number of seconds.

import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Countdown finished!")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the number of seconds for the countdown: "))
        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            countdown_timer(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")