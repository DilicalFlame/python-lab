"""
This file demonstrates the use of the modulo operator (%) in Python.
"""

# Modulo operator example
a = 10
b = 3
result = a % b  # This will give the remainder of 10 divided by 3
print("The result of {} % {} is: {}".format(a, b, result))  # Output: 1

# Using modulo operator with negative numbers
c = -10
d = 3
result_negative = c % d  # This will give the remainder of -10 divided by 3
print("The result of {} % {} is: {}".format(c, d, result_negative))  # Output: 2

# Modulo operator with floats
g = 10.5
h = 3.2
result_float = g % h  # This will give the remainder of 10.5 divided by 3.2
print("The result of {:.1f} % {:.1f} is: {:.1f}".format(g, h, result_float))  # Output: 0.9
