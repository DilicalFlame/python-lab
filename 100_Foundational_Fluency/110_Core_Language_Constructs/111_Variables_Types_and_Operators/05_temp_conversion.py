"""
This script demonstrates converting temperatures between Celsius and Fahrenheit and vice versa.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit using the formula:\n
    `Fahrenheit = (Celsius * 9/5) + 32`
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius using the formula:\n
    `Celsius = (Fahrenheit - 32) * 5/9`
    """
    return (fahrenheit - 32) * 5/9

def main():
    # Input temperature and unit
    temp = float(input("Enter the temperature: "))
    unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    return 0

if __name__ == "__main__":
    main()