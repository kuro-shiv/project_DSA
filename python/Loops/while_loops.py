# while_loops.py
# This program demonstrates the use of while loops in Python

# ---------------------
# 1. Simple while loop
# ---------------------
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # increment to avoid infinite loop

# ---------------------
# 2. Using while loop with condition
# ---------------------
num = 10
while num > 0:
    print(f"Countdown: {num}")
    num -= 2

# ---------------------
# 3. Infinite loop with break
# ---------------------
i = 1
while True:
    print(f"i = {i}")
    i += 1
    if i > 5:
        break  # exit the loop

# ---------------------
# 4. Using continue in while loop
# ---------------------
j = 0
while j < 10:
    j += 1
    if j % 2 == 0:
        continue  # skip even numbers
    print(f"Odd number: {j}")

# ---------------------
# 5. Using while loop with else
# ---------------------
k = 1
while k <= 3:
    print(f"Loop iteration: {k}")
    k += 1
else:
    print("While loop completed successfully")

