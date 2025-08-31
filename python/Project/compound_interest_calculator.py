# compound_interest_calculator.py
# This program calculates compound interest

# Input principal amount, rate, time, and number of times interest is compounded per year
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Convert rate from percentage to decimal
rate = rate / 100

# Calculate compound interest
# Formula: A = P * (1 + r/n)^(n*t)
amount = principal * (1 + rate/n) ** (n * time)
compound_interest = amount - principal

# Display the result
print(f"Compound Interest = {compound_interest:.2f}")
print(f"Total Amount = {amount:.2f}")
