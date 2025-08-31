# arithmetic_math_final.py
# Complete Python program demonstrating arithmetic operations, math functions,
# area, perimeter, and circumference calculations (with and without math module)

# ---------------------
# 1. Basic Arithmetic Operations
# ---------------------
a = 15
b = 4
print("----- Basic Arithmetic -----")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# ---------------------
# 2. Using Math Module
# ---------------------
import math
print("\n----- Math Module Examples -----")
num = 16
print(f"Square root of {num} = {math.sqrt(num)}")
print(f"Ceil of 4.2 = {math.ceil(4.2)}, Floor of 4.7 = {math.floor(4.7)}")
neg = -10
print(f"Absolute value of {neg} = {abs(neg)}")
print(f"Rounded value of 3.14159 to 2 decimals = {round(3.14159, 2)}")
angle = math.radians(45)
print(f"sin(45°) = {math.sin(angle):.2f}, cos(45°) = {math.cos(angle):.2f}")

# ---------------------
# 3. Area Calculations (With Math Module)
# ---------------------
print("\n----- Area Calculations (with math module) -----")
length = 10
width = 5
area_rectangle = length * width
print(f"Area of rectangle = {area_rectangle}")

base = 8
height = 6
area_triangle = 0.5 * base * height
print(f"Area of triangle = {area_triangle}")

radius = 7
area_circle = math.pi * radius ** 2
circumference_circle = 2 * math.pi * radius
print(f"Area of circle = {area_circle:.2f}")
print(f"Circumference of circle = {circumference_circle:.2f}")

side = 9
perimeter_square = 4 * side
print(f"Perimeter of square = {perimeter_square}")

side1, side2, side3 = 5, 6, 7
perimeter_triangle = side1 + side2 + side3
print(f"Perimeter of triangle = {perimeter_triangle}")

perimeter_rectangle = 2 * (length + width)
print(f"Perimeter of rectangle = {perimeter_rectangle}")

# ---------------------
# 4. Area Calculations Without Math Module
# ---------------------
print("\n----- Area & Circumference Without Math Module -----")
pi = 3.14159
radius2 = 7
area_circle2 = pi * radius2 ** 2
circumference_circle2 = 2 * pi * radius2
sqrt_num2 = 25 ** 0.5

print(f"Area of circle = {area_circle2:.2f}")
print(f"Circumference of circle = {circumference_circle2:.2f}")
print(f"Square root of 25 = {sqrt_num2}")

# Rectangle, triangle, and square calculations without math module
length2 = 10
width2 = 5
area_rectangle2 = length2 * width2
perimeter_rectangle2 = 2 * (length2 + width2)
base2 = 8
height2 = 6
area_triangle2 = 0.5 * base2 * height2
side2 = 9
perimeter_square2 = 4 * side2

print(f"Area of rectangle = {area_rectangle2}")
print(f"Perimeter of rectangle = {perimeter_rectangle2}")
print(f"Area of triangle = {area_triangle2}")
print(f"Perimeter of square = {perimeter_square2}")
