# for_loops.py
# This program demonstrates the use of for loops in Python

# ---------------------
# 1. Simple for loop with range
# ---------------------
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# ---------------------
# 2. Loop through a list
# ---------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# ---------------------
# 3. Loop through a string
# ---------------------
text = "Python"
for char in text:
    print(char)

# ---------------------
# 4. Using break in for loop
# ---------------------
print("Loop with break:")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop")
        break
    print(i)

# ---------------------
# 5. Using continue in for loop
# ---------------------
print("Loop with continue (skip even numbers):")
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# ---------------------
# 6. For loop with else
# ---------------------
print("For loop with else:")
for i in range(1, 4):
    print(f"Iteration {i}")
else:
    print("Loop completed successfully")
