# determine if a given year is a leap year

def is_leap_year(yy):
    if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
