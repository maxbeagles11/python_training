"""The solutions to the problems in 'try_these_problems.py'."""

# -------------------------
# 01_prints_and_docs.py
# -------------------------

"""Write a Python program that:

    1. Prints "Hello, world!" to the console.

    2. Prints your name and age (use variables).

    3. Print the Python documentation for the print() function (use help()).
"""

# Solution for Problem 1: Printing "Hello, world!"
print("Hello, world!")

# Solution for Problem 2: Print name and age
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Solution for Problem 3: Print documentation for print function
help(print)


# -------------------------
# 02_variables.py
# -------------------------

"""Write a Python program that:

    1. Creates a variable x and assigns it the value of 10.

    2. Creates another variable y and assigns it the value of 5.

    3. Calculate the sum of x and y and store it in a new variable sum_result using the '+' operator.

    4. Print the value of sum_result with a message saying "The sum of x and y is: ".

    5. Change the value of x to 20 and y to 15. Recalculate the sum and print the new result.
"""

# Solution for Problem 1: Assigning values to variables
x = 10
y = 5

# Solution for Problem 2: Calculating the sum of x and y
sum_result = x + y
print(f"The sum of x and y is: {sum_result}")

# Solution for Problem 3: Changing values of x and y
x = 20
y = 15

# Recalculate the sum with the new values
sum_result = x + y
print(f"The sum of x and y with the new values is: {sum_result}")


# -------------------------
# 03_data_types_and_structures.py
# -------------------------

"""Write a Python program that:

    1. Creates a list of numbers from 1 to 5 and prints it.

    2. Creates a tuple with the elements "apple", "banana", and "cherry", then prints the tuple.

    3. Creates a dictionary with keys "name", "age", and "city", and assigns values to each key. Print the dictionary.

    4. Create a set of unique numbers from the list of numbers and print it.
"""

# Solution for Problem 1: List of numbers
numbers = [1, 2, 3, 4, 5]
print(f"List of numbers: {numbers}")

# Solution for Problem 2: Tuple of fruits
fruits = ("apple", "banana", "cherry")
print(f"Tuple of fruits: {fruits}")

# Solution for Problem 3: Dictionary with personal information
person_info = {"name": "John", "age": 25, "city": "New York"}
print(f"Dictionary: {person_info}")

# Solution for Problem 4: Set of unique numbers from the list
unique_numbers = set(numbers)
print(f"Set of unique numbers: {unique_numbers}")
