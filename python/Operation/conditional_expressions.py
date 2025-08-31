# conditional_expressions.py
# This program demonstrates conditional expressions (also called ternary operators) in Python

# Example 1: Simple conditional expression
age = 18
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# Example 2: Checking even or odd
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

# Example 3: Maximum of two numbers
a = 10
b = 20
max_num = a if a > b else b
print(f"Maximum of {a} and {b} is {max_num}")

# Example 4: Nested conditional expression
marks = 85
grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 50 else "F"
print(f"Marks: {marks}, Grade: {grade}")

# Example 5: Using conditional expression in a print statement
temperature = 30
print("It's hot" if temperature > 25 else "It's cool")

# Example 6: Conditional expression with boolean
is_raining = True
activity = "Stay indoors" if is_raining else "Go outside"
print(f"Weather activity: {activity}")
