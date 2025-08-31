# format_specifiers.py
# This program demonstrates different ways to format strings in Python

# ---------------------
# 1. Using f-strings (Python 3.6+)
# ---------------------
name = "Alice"
age = 25
height = 5.7

print(f"My name is {name}, I am {age} years old and my height is {height} feet.")

# ---------------------
# 2. Using format() method
# ---------------------
print("My name is {}, I am {} years old and my height is {} feet.".format(name, age, height))
print("My name is {0}, I am {1} years old and my height is {2} feet.".format(name, age, height))
print("My name is {n}, I am {a} years old and my height is {h} feet.".format(n=name, a=age, h=height))

# ---------------------
# 3. Using % formatting (old style)
# ---------------------
print("My name is %s, I am %d years old and my height is %.2f feet." % (name, age, height))

# ---------------------
# 4. Formatting numbers
# ---------------------
pi = 3.14159265359
print(f"Value of pi up to 2 decimals: {pi:.2f}")  # f-string
print("Value of pi up to 3 decimals: {:.3f}".format(pi))  # format()
print("Value of pi up to 4 decimals: %.4f" % pi)  # % formatting

# ---------------------
# 5. Padding and alignment
# ---------------------
text = "Python"
print(f"{text:<10} left aligned")   # Left aligned in width 10
print(f"{text:>10} right aligned")  # Right aligned in width 10
print(f"{text:^10} center aligned") # Center aligned in width 10

# ---------------------
# 6. Adding leading zeros
# ---------------------
num = 42
print(f"Number with leading zeros: {num:05}")  # Output: 00042
