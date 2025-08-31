# calculator.py
# Simple calculator program in Python using if-elif-else statements

# Display menu
print("Simple Calculator")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (^)")

# Take user input for operation
choice = input("Enter choice (1/2/3/4/5/6): ")

# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation based on user choice
if choice == "1" or choice == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == "2" or choice == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == "3" or choice == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == "4" or choice == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif choice == "5" or choice == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
elif choice == "6" or choice == "^":
    result = num1 ** num2
    print(f"{num1} ^ {num2} = {result}")
else:
    print("Invalid input. Please select a valid operation.")
