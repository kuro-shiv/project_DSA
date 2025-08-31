# if_statements.py
# This program demonstrates the usage of if, elif, and else statements in Python

# Example 1: Simple if statement
age = 18
if age >= 18:
    print("You are an adult.")

# Example 2: if-else statement
temperature = 30
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's a cool day.")

# Example 3: if-elif-else statement
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Example 4: Nested if statements
num = 10
if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")
else:
    print(f"{num} is zero or negative.")

# Example 5: Checking multiple conditions with logical operators
a = 20
b = 15
if a > 10 and b > 10:
    print("Both a and b are greater than 10.")

if a > 10 or b > 20:
    print("At least one of a or b satisfies the condition.")

# if_statements_extended.py
# More examples of if, elif, else statements in Python

# Example 6: Checking string input
color = input("Enter your favorite color: ").lower()
if color == "red":
    print("Red is the color of energy!")
elif color == "blue":
    print("Blue is calm and peaceful.")
elif color == "green":
    print("Green represents nature.")
else:
    print(f"{color.capitalize()} is a unique color!")

# Example 7: Multiple conditions using nested if-else
number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print(f"{number} is a positive even number.")
    else:
        print(f"{number} is a positive odd number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

# Example 8: Using not operator
is_raining = input("Is it raining? (yes/no): ").lower()
if not is_raining == "yes":
    print("You can go outside!")
else:
    print("Take an umbrella!")

# Example 9: Checking age for multiple categories
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Example 10: Combining multiple conditions
marks = int(input("Enter your marks: "))
attendance = int(input("Enter attendance percentage: "))
if marks >= 50 and attendance >= 75:
    print("You have passed the course!")
else:
    print("You did not meet the passing criteria.")


# if_statements_different_data_types.py
# Demonstrates if, elif, else statements using different data types in Python

# ---------------------
# 1. Integer
# ---------------------
num = 15
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

# ---------------------
# 2. Float
# ---------------------
temperature = 37.5
if temperature > 37:
    print("You have a fever.")
else:
    print("Temperature is normal.")

# ---------------------
# 3. String
# ---------------------
language = "Python"
if language == "Python":
    print("You are learning Python!")
elif language == "Java":
    print("You are learning Java!")
else:
    print(f"You are learning {language}.")

# ---------------------
# 4. Boolean
# ---------------------
is_raining = True
if is_raining:
    print("Take an umbrella!")
else:
    print("No need for umbrella.")

# ---------------------
# 5. List
# ---------------------
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list.")
else:
    print("Banana is not in the list.")

# ---------------------
# 6. Dictionary
# ---------------------
person = {"name": "Alice", "age": 25}
if "name" in person:
    print(f"Person's name is {person['name']}.")
else:
    print("Name not found.")

# ---------------------
# 7. Combining Data Types
# ---------------------
score = 85
passed = True
if score >= 50 and passed:
    print("You passed the exam.")
else:
    print("You did not pass.")
