# Write a program to determine if a given number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a positive integer to check if it's prime: "))
        if user_input <= 0:
            print("Please enter a positive integer.")
        else:
            if is_prime(user_input):
                print(f"{user_input} is a prime number.")
            else:
                print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")