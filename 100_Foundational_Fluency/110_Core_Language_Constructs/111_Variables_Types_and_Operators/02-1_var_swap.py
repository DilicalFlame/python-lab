"""
This script demonstrates how to swap the values of two variables in Python using **a temporary variable**.
"""

a = 1
b = 2

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

temp = a                    # Store the value of 'a' in a temporary variable
a = b                       # Assign the value of 'b' to 'a'
b = temp                    # Assign the value of the temporary variable to 'b'

print("After swapping:")
print("a =", a)
print("b =", b)
