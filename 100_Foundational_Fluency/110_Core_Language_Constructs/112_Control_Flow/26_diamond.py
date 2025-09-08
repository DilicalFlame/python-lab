# Combine two pyramids to form a diamond shape.

def print_diamond(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Upper pyramid
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    # Lower pyramid
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the number of rows for the diamond (half pyramid height): "))
        print_diamond(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")