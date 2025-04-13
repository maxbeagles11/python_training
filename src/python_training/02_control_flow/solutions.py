"""The solutions to the problems in 'try_these_problems.py'."""

# -------------------------
# 01_logic.py
# -------------------------

# Simulated inputs
age = 20
number = 7
temperature = 98.6

# Solution 1: Age check
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Solution 2: Even or odd
if number % 2 == 0:
    print("That number is even.")
else:
    print("That number is odd.")

# Solution 3: Temperature check
if temperature > 99.5:
    print("You might have a fever.")
elif temperature >= 97:
    print("You're fine.")
else:
    print("You might be cold.")


# -------------------------
# 02_loops.py
# -------------------------

# Solution 1: For loop
for i in range(1, 11):
    print(i)

# Solution 2: While loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Solution 3: Print even numbers from a list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in num_list:
    if num % 2 == 0:
        print(num)

# Solution 4: Simulated continuous input for sum
entries = ["5", "3.2", "7.8", "done"]
total = 0
for entry in entries:
    if entry.lower() == "done":
        break
    total += float(entry)
print(f"The total sum is: {total}")


# -------------------------
# 03_exceptions.py
# -------------------------

# Simulated input values
test_values = [5, 0, "abc", 10]

# Solution 1 and 2: Try individual values
try:
    number = test_values[0]
    result = 100 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    integer = int(test_values[2])  # this will raise ValueError
    print(f"You entered: {integer}")
except ValueError:
    print("That's not an integer!")

# Solution 3: Combined handling
for val in test_values:
    try:
        number = float(val)
        result = 100 / number
        print(f"Result: {result}")
        break  # Only break if successful
    except ValueError:
        print(f"'{val}' is not a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")
