"""
Calculate simple interest given principal, rate, and time.
This practices basic arithmetic operations and variable assignment.
"""

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate simple interest using the formula:\n
    `Simple Interest = Principal * Rate * Time`
    """
    return float(principal * rate * time)

def main():
    # Input values for principal, rate, and time
    principal = float(input("Enter principle amount: "))                   # Principal amount in INR
    rate = float(input("Enter Interest rate in percentages: "))/100        # Interest rate (5%)
    time = float(input("Enter number of years: "))                         # Time in years

    # Calculate simple interest
    interest = calculate_simple_interest(principal, rate, time)

    # Output the result
    print(f"The simple interest is: {interest:.2f} INR")

if __name__ == "__main__":
    main()