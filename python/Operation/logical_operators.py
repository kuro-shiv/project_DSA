# logical_operators.py
# This program demonstrates the use of logical operators in Python: and, or, not

# ---------------------
# AND Operator
# ---------------------
age = 25
has_id = True

if age >= 18 and has_id:
    print("You are allowed to enter.")
else:
    print("You are not allowed to enter.")

# ---------------------
# OR Operator
# ---------------------
temperature = 30
raining = True

if temperature > 35 or raining:
    print("Stay indoors today.")
else:
    print("You can go outside.")

# ---------------------
# NOT Operator
# ---------------------
is_sunny = False

if not is_sunny:
    print("It is not sunny today.")
else:
    print("It is sunny today.")

# ---------------------
# Combining Logical Operators
# ---------------------
marks = 80
attendance = 70

if marks >= 50 and attendance >= 75:
    print("You passed the course.")
elif marks >= 50 or attendance >= 75:
    print("You need improvement.")
else:
    print("You failed the course.")

# ---------------------
# Logical operators with strings
# ---------------------
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Login failed.")
