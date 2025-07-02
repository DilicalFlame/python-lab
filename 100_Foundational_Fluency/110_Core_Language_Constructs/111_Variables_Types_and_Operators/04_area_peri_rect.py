"""
This script calculates the area and perimeter of a rectangle.
"""

def calculate_area(width: float, height: float) -> float:
    return width * height

def calculate_perimeter(width: float, height: float) -> float:
    return 2 * (width + height)

def main():
    width = float(input("Width: "))
    height = float(input("Height: "))
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)
    print(f"Area = {area:.2f}")
    print(f"Perimeter = {perimeter:.2f}")
    return 0

if __name__ == "__main__":
    main()