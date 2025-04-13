"""The solutions to the problems in 'try_these_problems.py'."""

# ----------------------------
# 01. Define a simple function
# ----------------------------

"""Write a Python function called `say_hello` that prints "Hello, World!" to the console.
Then, call the function to print the message.
"""


# Solution:
def say_hello() -> None:
    """
    Prints the greeting message "Hello, World!" to the console.

    Returns:
    -------
        None: This function does not return anything, it only prints to the console.
    """
    print("Hello, World!")


# Calling the function
say_hello()


# ---------------------------------------------
# 02. Function with arguments and return values
# ---------------------------------------------

"""Write a Python function called `multiply` that takes two arguments `x` and `y` (both integers)
and returns their product. Test the function with the numbers 5 and 4 and print the result.
"""


# Solution:
def multiply(x: int, y: int) -> int:
    """
    Multiplies two integers and returns their product.

    Args:
    ----
        x (int): The first integer.
        y (int): The second integer.

    Returns:
    -------
        int: The product of x and y.
    """
    return x * y


# Test the function with numbers 5 and 4
result = multiply(5, 4)
print(f"The result of multiplication is: {result}")


# -------------------------
# 03. Default arguments
# -------------------------

"""Write a function called `greet_person` that takes a name as an argument and prints a
greeting message. If no name is provided, the function should default to "Guest". Test the function by passing a name and then calling it without any arguments.
"""


# Solution:
def greet_person(name: str = "Guest") -> None:
    """
    Greets the person by name. If no name is provided, defaults to "Guest".

    Args:
    ----
        name (str): The name of the person. Defaults to "Guest".

    Returns:
    -------
        None: This function does not return anything, it only prints to the console.
    """
    print(f"Hello, {name}!")


# Test the function by passing a name
greet_person("Alice")

# Test the function without passing a name (using the default)
greet_person()


# -------------------------
# 04. Keyword arguments
# -------------------------

"""Write a function called `order_pizza` that accepts two keyword arguments: `size` and `toppings`.
The `size` argument should have a default value of "medium", and the `toppings` argument should have a default value of an empty list.

The function should print an order summary such as:
"Order placed: Size: medium, Toppings: ['cheese', 'tomato', 'olives']"

Test the function by calling it with no arguments, then with only a `size`, and finally with both `size` and `toppings`.
"""


# Solution:
def order_pizza(size: str = "medium", toppings: list = []) -> None:
    """
    Orders a pizza by specifying the size and toppings. If no arguments are passed,
    it defaults to a medium pizza with no toppings.

    Args:
    ----
        size (str): The size of the pizza (default is "medium").
        toppings (list): A list of toppings for the pizza (default is an empty list).

    Returns:
    -------
        None: This function does not return anything, it only prints to the console.
    """
    print(f"Order placed: Size: {size}, Toppings: {toppings}")


# Test the function with no arguments
order_pizza()

# Test the function with only a size
order_pizza(size="large")

# Test the function with both size and toppings
order_pizza(size="small", toppings=["cheese", "tomato", "olives"])


# --------------------------------------------------
# 05. Variable-length arguments (*args and **kwargs)
# --------------------------------------------------

"""Write a function called `sum_numbers` that accepts a variable number of positional arguments (*args) and returns the sum of all the numbers. Test the function by passing several numbers.
"""


# Solution:
def sum_numbers(*args) -> int:
    """
    Sums all the numbers passed as positional arguments.

    Args:
    ----
        *args (int): A variable number of integers to sum.

    Returns:
    -------
        int: The sum of all the numbers passed as arguments.
    """
    return sum(args)


# Test the function with several numbers
result = sum_numbers(1, 2, 3, 4, 5)
print(f"The sum of the numbers is: {result}")


# -------------------------
# 06. Using docstrings
# -------------------------

"""Write a function called `power` that returns the result of raising `base` to the power of `exponent`. Make sure to write a docstring that explains the arguments (`base` and `exponent`)
and the return value. Test the function by calling it with base 2 and exponent 3.
"""


# Solution:
def power(base: int, exponent: int) -> int:
    """
    Returns the result of raising the base to the power of the exponent.

    Args:
    ----
        base (int): The base number.
        exponent (int): The exponent to which the base is raised.

    Returns:
    -------
        int: The result of base raised to the power of exponent.
    """
    return base**exponent


# Test the function with base 2 and exponent 3
result = power(2, 3)
print(f"The result of 2 raised to the power of 3 is: {result}")
