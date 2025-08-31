# string_indexing.py
# This program demonstrates string indexing and slicing in Python

# Sample string
text = "Python"

# ---------------------
# 1. Accessing characters by index
# ---------------------
print(text[0])   # First character: 'P'
print(text[1])   # Second character: 'y'
print(text[-1])  # Last character: 'n'
print(text[-2])  # Second last character: 'o'

# ---------------------
# 2. Slicing strings
# ---------------------
print(text[0:4])   # Characters from index 0 to 3: 'Pyth'
print(text[2:])    # From index 2 to end: 'thon'
print(text[:4])    # From start to index 3: 'Pyth'
print(text[:])     # Entire string: 'Python'
print(text[-4:-1]) # From -4 to -2: 'tho'

# ---------------------
# 3. Slicing with step
# ---------------------
print(text[::2])   # Every 2nd character: 'Pto'
print(text[1::2])  # Every 2nd character starting from index 1: 'yhn'
print(text[::-1])  # Reverse the string: 'nohtyP'
print(text[::-2])  # Reverse every 2nd character: 'nhy'

# ---------------------
# 4. Using string indexing in operations
# ---------------------
first_char = text[0]
last_char = text[-1]
print(f"First: {first_char}, Last: {last_char}")

# Concatenate first and last character
new_text = text[0] + text[-1]
print(f"New text: {new_text}")
