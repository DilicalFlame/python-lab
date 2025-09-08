# For a given number, generate the Collatz sequence until it reaches 1

def collatz_sequence(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a positive integer to generate the Collatz sequence: "))
        if user_input <= 0:
            print("Please enter a positive integer.")
        else:
            result = collatz_sequence(user_input)
            print("Collatz sequence:", result)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")