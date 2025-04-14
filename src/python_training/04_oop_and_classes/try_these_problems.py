"""This script contains simple problems to help
you grasp all of the concepts in this section.

The solutions to each problem will be in the 'solutions.py'
script. Good luck!
"""

# IMPORTANT: Once again, be sure you're using docstrings and comments as needed!

# -------------------------
# 01_class.py
# -------------------------

"""Write a Python script that:

    1. Define a class `Person` with:
        - A constructor that initializes `name` and `age`.
        - A method `greet()` that prints "Hello, my name is {name} and I am {age} years old."
    2. Create an instance of the `Person` class and call the `greet()` method.

    3. Define a class `Rectangle` with:
        - Constructor that initializes `length` and `width`.
        - A method `get_area()` that returns the area (length * width).
        - A method `get_perimeter()` that returns the perimeter (2 * (length + width)).
    4. Create an instance of `Rectangle` and print the area and perimeter.
"""

# <Write your code here>


# -------------------------
# 02_inheritance.py
# -------------------------

"""Write a Python program that:

    1. Create a base class `Vehicle` with:
        - Constructor that initializes `make` and `model`.
        - Method `start()` that prints "The vehicle is starting".
        - Method `stop()` that prints "The vehicle is stopping".
    2. Create a subclass `Car` that:
        - Inherits from `Vehicle`.
        - Adds an additional attribute `seats` for the number of seats in the car.
        - Overrides the `start()` method to print "The car is starting".
    3. Create another subclass `Truck` that:
        - Inherits from `Vehicle`.
        - Adds an additional attribute `cargo_capacity` for the weight the truck can carry.
        - Overrides the `start()` method to print "The truck is starting".
    4. Create instances of `Car` and `Truck` and call the `start()` and `stop()` methods on them.

    5. Add a method `get_info()` to both `Car` and `Truck` that returns a string containing the make, model, and specific attributes (e.g., seats or cargo capacity).
    6. Use the `get_info()` method for both `Car` and `Truck` instances to display their information.
"""


# <Write your code here>


# -------------------------
# 03_advanced.py
# -------------------------

"""Write a Python program that:

    1. Define a class `Rectangle` with:
        - Private attributes `_length` and `_width`.
        - A method `get_area()` that calculates and returns the area (length * width).
        - Use the `@property` decorator to create `length` and `width` getter and setter methods.
        - Use the `@property` decorator for `area` to calculate the area on the fly.
    2. Create an instance of `Rectangle`, set the length and width, and print the area.

    3. Define a class `Book` with:
        - Class variable `category`.
        - Constructor that takes `title`, `author`, and `year`.
        - Class method `from_string(cls, book_str: str)` that creates a Book instance from a string.
        - Class method `get_category(cls)` that returns the category of the book.
    4. Create an instance of `Book` using the `from_string()` method and print the category.

    5. Define a class `Calculator` with the following static methods:
        - `add(x, y)` to add two numbers.
        - `subtract(x, y)` to subtract one number from another.
        - `multiply(x, y)` to multiply two numbers.
        - `divide(x, y)` to divide one number by another (handle division by zero).
    6. Create an instance of `Calculator` and use the static methods to perform calculations.

    7. Define a class `Car` with:
        - Class variable `total_cars`.
        - Constructor that initializes `make`, `model`, and `year`.
        - A class method `get_total_cars()` that returns the total number of cars.
    8. Create multiple `Car` instances and use the `get_total_cars()` method to display the total number of cars.

    9. Define a class `Account` with:
        - Constructor that initializes `balance`.
        - Methods `deposit(amount)` and `withdraw(amount)` that return the instance for method chaining.
        - Method `get_balance()` to return the current balance.
    10. Create an `Account` instance and use method chaining to deposit and withdraw money.
"""

# <Write your code here>
