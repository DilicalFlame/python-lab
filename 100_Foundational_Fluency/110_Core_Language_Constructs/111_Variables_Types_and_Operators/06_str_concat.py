"""
Combining strings in Python can be done using several methods. Here are some common ways to concatenate strings:
1. Using the `+` operator:
2. Using the `join()` method:
3. Using f-strings (formatted string literals):
4. Using the `format()` method:
5. Using the `%` operator (old-style formatting):
6. Using `str.format_map()`:
"""

# 1. Using the `+` operator
str1 = "Hello"
str2 = "World"
str_concat_plus = str1 + " " + str2
print("Using + operator:", str_concat_plus)

# 2. Using the `join()` method
str_list = ["Hello", "World"]
str_concat_join = " ".join(str_list)
print("Using join() method:", str_concat_join)

# 3. Using f-strings (formatted string literals)
name = "World"
str_concat_fstring = f"Hello {name}"
print("Using f-strings:", str_concat_fstring)

# 4. Using the `format()` method
str_concat_format = "Hello {}".format(name)
print("Using format() method:", str_concat_format)

# 5. Using the `%` operator (old-style formatting)
str_concat_percent = "Hello %s" % name
print("Using % operator:", str_concat_percent)

# 6. Using `str.format_map()`
str_map = {"name": "World"}
str_concat_map = "Hello {name}".format_map(str_map)