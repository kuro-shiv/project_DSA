# string_methods.py
# This program demonstrates various commonly used string methods in Python

# Sample string
text = "  Hello, Python World!  "

# 1. Changing case
print(text.upper())        # Convert to uppercase
print(text.lower())        # Convert to lowercase
print(text.title())        # Capitalize each word
print(text.capitalize())   # Capitalize first character

# 2. Removing whitespace
print(text.strip())        # Remove leading and trailing spaces
print(text.lstrip())       # Remove leading spaces
print(text.rstrip())       # Remove trailing spaces

# 3. Searching in string
print(text.find("Python"))      # Returns index of substring, -1 if not found
print(text.index("Python"))     # Returns index of substring, error if not found
print(text.count("o"))          # Count occurrences of character/substring
print(text.startswith("  He"))  # Check if string starts with substring
print(text.endswith("World!  "))# Check if string ends with substring

# 4. Replacing and splitting
print(text.replace("Python", "Programming"))  # Replace substring
words = text.split()                          # Split by spaces into list
print(words)
print(text.split(","))                        # Split by comma

# 5. Joining list into string
word_list = ["Python", "is", "fun"]
joined_text = " ".join(word_list)
print(joined_text)

# 6. Checking string content
sample = "12345"
print(sample.isdigit())      # True if all characters are digits
print(sample.isalpha())      # True if all characters are letters
print(sample.isalnum())      # True if all characters are letters or digits
print(" ".isspace())         # True if all characters are whitespace
print("Hello".isupper())     # True if all characters are uppercase
print("hello".islower())     # True if all characters are lowercase
