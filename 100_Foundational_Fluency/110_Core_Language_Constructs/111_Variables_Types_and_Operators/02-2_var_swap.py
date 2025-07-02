"""
This script demonstrates how to swap the values of two variables in Python using tuple unpacking.
"""

a = 1
b = 2

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

a, b = b, a                   # Swapping values using tuple unpacking

print("After swapping:")
print("a =", a)
print("b =", b)