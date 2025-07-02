"""
A simple Read-Eval-Print Loop that takes two numbers and an operator from the user and prints the result.
"""

def basic_arithmetic_repl():
    print("Welcome to the Basic Arithmetic REPL!")
    print("You can perform operations like +, -, *, /, %, ** (exponentiation). Type 'exit' to quit.")

    while True:
        user_input = input("Enter an expression (e.g., 2 + 3) or 'exit' to quit: ")

        if user_input.lower() == 'exit':
            print("Exiting the REPL. Goodbye!")
            break

        try:
            result = eval(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid expression.")

if __name__ == "__main__":
    basic_arithmetic_repl()