# Use nested loops to print a right-angled triangle pattern of asterisks

def half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()  # Move to the next line after each row

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the number of rows for the half pyramid: "))
        if user_input <= 0:
            print("Please enter a positive integer.")
        else:
            half_pyramid(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")