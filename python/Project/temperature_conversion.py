# temperature_conversion.py
# This program converts temperature between Celsius, Fahrenheit, and Kelvin

# Display menu
print("Temperature Conversion Program")
print("Select the conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

# Take user input for conversion choice
choice = input("Enter choice (1/2/3/4/5/6): ")

# Take temperature input
temp = float(input("Enter the temperature to convert: "))

# Perform conversion based on user choice
if choice == "1":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C = {converted:.2f}°F")
elif choice == "2":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F = {converted:.2f}°C")
elif choice == "3":
    converted = temp + 273.15
    print(f"{temp}°C = {converted:.2f}K")
elif choice == "4":
    converted = temp - 273.15
    print(f"{temp}K = {converted:.2f}°C")
elif choice == "5":
    converted = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F = {converted:.2f}K")
elif choice == "6":
    converted = (temp - 273.15) * 9/5 + 32
    print(f"{temp}K = {converted:.2f}°F")
else:
    print("Invalid input. Please select a valid conversion.")
