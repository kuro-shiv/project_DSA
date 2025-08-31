
# user_input.py
# This program demonstrates how to take input from the user in Python

# Taking string input
name = input("Enter your name: ")  # input() always returns a string
print(f"Hello, {name}!")

# Taking integer input
age = int(input("Enter your age: "))  # convert input string to integer
print(f"You are {age} years old.")

# Taking float input
height = float(input("Enter your height in feet: "))  # convert input string to float
print(f"Your height is {height} feet.")

# Taking boolean input (example using string comparison)
is_student_input = input("Are you a student? (yes/no): ")
is_student = True if is_student_input.lower() == "yes" else False
print(f"Student status: {is_student}")

# user_input.py (Extended Examples)

# Taking multiple inputs at once (all strings)
first_name, last_name = input("Enter your first and last name: ").split()
print(f"Full Name: {first_name} {last_name}")

# Taking multiple numeric inputs at once
x, y, z = map(int, input("Enter three numbers separated by space: ").split())
print(f"Numbers: x={x}, y={y}, z={z}")

# Taking float numbers as multiple inputs
a, b = map(float, input("Enter two decimal numbers separated by space: ").split())
print(f"Decimals: a={a}, b={b}")

# User input with type casting to boolean (custom logic)
response = input("Do you like Python? (yes/no): ").lower()
likes_python = True if response == "yes" else False
print(f"Likes Python: {likes_python}")

# Using input in calculations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_numbers = num1 + num2
print(f"Sum: {sum_numbers}")

# Input and string concatenation
city = input("Enter your city: ")
country = input("Enter your country: ")
location = city + ", " + country
print(f"You are from {location}")


print(f"Hello, {name}!")