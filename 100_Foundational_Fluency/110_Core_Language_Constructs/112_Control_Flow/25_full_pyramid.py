# An extension of the previous project to create a symmetrical pyramid.

def full_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")
        print()  # Move to the next line after each row

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the number of rows for the full pyramid: "))
        if user_input <= 0:
            print("Please enter a positive integer.")
        else:
            full_pyramid(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")