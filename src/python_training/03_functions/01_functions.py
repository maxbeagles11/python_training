"""In this script we will cover how to define and use functions.

We will cover:
    1. Defining simple functions
    2. Using arguments and return values
    3. Default arguments
    4. Keyword arguments
    5. Variable-length arguments (*args and **kwargs)
    6. Docstrings for documentation
    7. Scope
"""

# -------------------------
# 01. Defining a simple function
# -------------------------

# To define a function, we use Python's "def" keyword.
# Here are some rules to remember when naming a function:
#   - Function names should be lowercase with words separated by underscores (e.g., `calculate_total`).
#   - Must start with a letter or underscore (not a number).
#   - Can contain letters, digits, and underscores.
#   - Avoid using Python keywords (like `def`, `class`, `return`) as function names.
#   - Use descriptive names that make it clear what the function does.
#       - This one is very important as it makes it easier to read code.
#       - Be sure to avoid *overly* long names too.


def greet() -> None:
    """Prints a simple greeting."""
    print("Hello from a function!")


# Call the function using the name of the function
# followed by parentheses.
greet()


# -------------------------
# 02. Function with arguments and return values
# -------------------------


def add(x: int, y: int) -> int:
    """Returns the sum of x and y.

    Args:
    ----
        x (int): The first integer number.
        y (int): The second integer number.
    Returns:
    -------
        int: The sum of x and y.
    """
    return x + y


# Example usage
result = add(3, 4)
print(f"The sum is: {result}")


# -------------------------
# 03. Default arguments
# -------------------------

# We can "pass" arguments to a function by placing them within the parentheses
# of a function call (assuming it takes arguments).
# When we don't pass arguments, we expect there to either not be any needed
# or it has default arguments. Be careful when defining functions that expect arguments
# but have no defaults.


def greet_user(name: str = "Guest") -> None:
    """Greets a user by name, or uses 'Guest' if no name is provided.

    Args:
    ----
        name (str): The name of the guest. Defaults to "Guest".

    """
    print(f"Hello, {name}!")


greet_user("Alice")
greet_user()


# -------------------------
# 04. Keyword arguments
# -------------------------


def describe_pet(animal_type: str, pet_name: str) -> None:
    """Displays information about a pet.

    Args:
    ----
        animal_type (str): The type of animal the pet is.
        pet_name (str): The name of the pet.

    """
    print(f"I have a {animal_type} named {pet_name}.")


# These are called named or keyword arguments.
# They are more verbose, but they work great for
# more complex function calls. They also help with code
# readability since it makes it clearer what's going on.
describe_pet(animal_type="dog", pet_name="Buddy")
describe_pet(pet_name="Whiskers", animal_type="cat")

# These are called positional arguments.
# These can be useful if you're feeling lazy and don't
# want to type the argument every time.
describe_pet(animal_type="dog", pet_name="Buddy")
describe_pet(pet_name="Whiskers", animal_type="cat")

# Things to consider for arguments:
# 1. If you mix positional and keyword arguments in a function call
# then the positional *must come first*. Otherwise you *will* get an
# error with your function call.
# 2. Each parameter only gets one value.


# -------------------------
# 05. Variable-length arguments (*args and **kwargs)
# -------------------------


def print_args(*args):
    """Prints all positional arguments passed in."""
    for arg in args:
        print(f"Arg: {arg}")


print_args(1, 2, 3)


def print_kwargs(**kwargs):
    """Prints all keyword arguments passed in."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Alice", age=30)


# -------------------------
# 06. Using docstrings
# -------------------------


def square(n: int | float) -> int | float:
    """
    Returns the square of a number.

    Args:
    ----
        n (int or float): The number to square.

    Returns:
    ----
        int or float: The square of the input.
    """
    return n**2


print(f"Square of 5 is: {square(5)}")
help(square)

# -------------------------
# 07. Understanding Scope
# -------------------------

# Scope refers to the region of the code where a variable is recognized.
# Python uses what's known as the LEGB rule:
# Local -> Enclosing -> Global -> Built-in

# Here's a breakdown of scope types:

# - Local: Variables defined inside a function.
# - Enclosing: Variables in the local scope of enclosing functions (for nested functions).
# - Global: Variables defined at the top-level of a script/module.
# - Built-in: Predefined names in Python like `len`, `print`, etc.

# Example of local vs global scope:

global_var = "I'm a global variable"  # exists outside of functions, classes, and loops.


def my_function() -> None:
    """Example function."""
    local_var = "I'm a local variable"
    print(global_var)  # Accessing global variable inside a function
    print(local_var)


my_function()

# print(local_var)  # ❌ This will raise an error. local_var is not visible outside the function


# Example of variable shadowing:
name = "Alice"


def change_name():
    name = "Bob"  # This 'name' is local and does NOT affect the global one
    print("Inside function:", name)


change_name()
print("Outside function:", name)  # Still prints "Alice"

# To modify a global variable inside a function, use the 'global' keyword
count = 0


def increment():
    global count
    count += 1


increment()
print("Count is:", count)

# -------------------------
# Summary
# -------------------------


# In this script, we covered several important aspects of working with functions in Python:
#
# 1. How to define a simple function using the `def` keyword.
#   - Including best practices and rules for naming functions.
# 2. How to pass arguments and return values using function parameters and the `return` statement.
# 3. How to use default arguments to make parameters optional.
# 4. How to use keyword arguments for clarity and flexibility in function calls.
# 5. How to accept a variable number of arguments using *args (for positional) and **kwargs (for keyword).
# 6. How to write informative docstrings to document what your functions do, their arguments, and return values.
# 7. What scope is and how to work with variables in and out of functions.
#
# Understanding functions is essential for writing clean, reusable, and modular code.
