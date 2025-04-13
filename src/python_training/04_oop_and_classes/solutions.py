"""The solutions to the problems in 'try_these_problems.py'."""

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


# 1. Define a class `Person`
class Person:
    """Class to represent a person with a name and age."""

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize the Person with a name and age.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def greet(self) -> None:
        """Print a greeting message with the person's name and age."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# 2. Create an instance of the `Person` class and call the `greet()` method.
person = Person("Alice", 30)
person.greet()  # Output: Hello, my name is Alice and I am 30 years old.


# 3. Define a class `Rectangle`
class Rectangle:
    """Class to represent a rectangle with length and width."""

    def __init__(self, length: float, width: float) -> None:
        """
        Initialize the rectangle with length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def get_area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)


# 4. Create an instance of `Rectangle` and print the area and perimeter.
rect = Rectangle(5, 3)
print(f"Area: {rect.get_area()}")  # Output: Area: 15
print(f"Perimeter: {rect.get_perimeter()}")  # Output: Perimeter: 16


# -------------------------
# 02_inheritance.py
# -------------------------

"""
Write a Python program that:

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


# 1. Create a base class `Vehicle`.
class Vehicle:
    def __init__(self, make: str, model: str) -> None:
        """
        Constructor to initialize make and model.

        Args:
            make (str): The make of the vehicle.
            model (str): The model of the vehicle.
        """
        self.make = make
        self.model = model

    def start(self) -> None:
        """
        Method to start the vehicle.

        Prints "The vehicle is starting".
        """
        print("The vehicle is starting.")

    def stop(self) -> None:
        """
        Method to stop the vehicle.

        Prints "The vehicle is stopping".
        """
        print("The vehicle is stopping.")


# 2. Define class Car that inherits from Vehicle.
class Car(Vehicle):
    def __init__(self, make: str, model: str, seats: int) -> None:
        """
        Constructor to initialize make, model, and seats.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            seats (int): The number of seats in the car.
        """
        super().__init__(make, model)
        self.seats = seats

    def start(self) -> None:
        """
        Override start method.

        Prints "The car is starting".
        """
        print("The car is starting.")

    def get_info(self) -> str:
        """
        Method to return info about the car.

        Returns:
            str: Information about the car (make, model, seats).
        """
        return f"Car - Make: {self.make}, Model: {self.model}, Seats: {self.seats}"


# 3. Define class Truck that inherits from Vehicle.
class Truck(Vehicle):
    def __init__(self, make: str, model: str, cargo_capacity: float) -> None:
        """
        Constructor to initialize make, model, and cargo capacity.

        Args:
            make (str): The make of the truck.
            model (str): The model of the truck.
            cargo_capacity (float): The cargo capacity of the truck.
        """
        super().__init__(make, model)
        self.cargo_capacity = cargo_capacity

    def start(self) -> None:
        """
        Override start method.

        Prints "The truck is starting".
        """
        print("The truck is starting.")

    def get_info(self) -> str:
        """
        Method to return info about the truck.

        Returns:
            str: Information about the truck (make, model, cargo capacity).
        """
        return f"Truck - Make: {self.make}, Model: {self.model}, Cargo Capacity: {self.cargo_capacity}"


# 4. Create instances of Car and Truck and call start() and stop() methods
car = Car("Toyota", "Corolla", 5)
truck = Truck("Ford", "F-150", 1000)

# Call start and stop methods
car.start()
car.stop()

truck.start()
truck.stop()

# 5. Add method get_info() to Car and Truck and display their information
# This is done above.
print(car.get_info())
print(truck.get_info())

# 6. Use the get_info() method for both Car and Truck instances to display their information
# (This is handled above in the get_info method usage)


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


# 1. Define a class `Rectangle'.
class Rectangle:
    """Class to represent a rectangle with private attributes and property decorators."""

    def __init__(self, length: float, width: float) -> None:
        """Initializes the Rectangle object with specified length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self._length = length
        self._width = width

    @property
    def length(self) -> float:
        """Gets the length of the rectangle.

        Returns:
            float: The length of the rectangle.
        """
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        """Sets the length of the rectangle.

        Args:
            value (float): The new length value.

        Raises:
            ValueError: If the length value is not positive.
        """
        if value > 0:
            self._length = value
        else:
            raise ValueError("Length must be positive")

    @property
    def width(self) -> float:
        """Gets the width of the rectangle.

        Returns:
            float: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """Sets the width of the rectangle.

        Args:
            value (float): The new width value.

        Raises:
            ValueError: If the width value is not positive.
        """
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be positive")

    @property
    def area(self) -> float:
        """Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle (length * width).
        """
        return self._length * self._width


# 2. Create an instance of `Rectangle`, set the length and width, and print the area.
rectangle = Rectangle(4, 5)

# Set the length and width using the setter methods
rectangle.length = 6  # Set the length to 6
rectangle.width = 3  # Set the width to 3

# Print the area using the 'area' property
print(f"Area: {rectangle.area}")  # Should print the area: 18 (6 * 3)


# 3. Define a class `Book`
class Book:
    """Class to represent a book."""

    category = "Fiction"  # Default category for all books

    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a Book instance with title, author, and year.

        Args:
        ----
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, book_str: str) -> "Book":
        """
        Creates a Book instance from a string in the format "title, author, year".

        Args:
        ----
            book_str: A string containing book details in "title, author, year" format.
        Returns:
        ----
            Book: A Book instance.
        """
        title, author, year = book_str.split(", ")
        return cls(title, author, int(year))

    @classmethod
    def get_category(cls) -> str:
        """
        Returns the category of the book.

        Returns:
        ----
            str: The category of the book.
        """
        return cls.category


# 4. Create an instance of `Book` using the `from_string()` method and print the category.
book_str = "The Great Gatsby, F. Scott Fitzgerald, 1925"
book = Book.from_string(book_str)

print(f"Book: {book.title} by {book.author}, published in {book.year}")
print(f"Category: {Book.get_category()}")


# 5. Define a class `Calculator`.
class Calculator:
    """A class to represent a calculator."""

    @staticmethod
    def add(x: float, y: float) -> float:
        """
        Adds two numbers together.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of x and y.
        """
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        """
        Subtracts the second number from the first number.

        Args:
            x (float): The number to subtract from.
            y (float): The number to subtract.

        Returns:
            float: The result of x - y.
        """
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """
        Multiplies two numbers together.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of x and y.
        """
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float:
        """
        Divides the first number by the second number.

        Args:
            x (float): The dividend.
            y (float): The divisor.

        Returns:
            float: The result of x divided by y.

        Raises:
            ZeroDivisionError: If y is 0.
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y


# 6. Create an instance of `Calculator` and use the static methods to perform calculations.
calc = Calculator()

# Adding numbers
result = calc.add(5, 3)
print(f"5 + 3 = {result}")

# Subtracting numbers
result = calc.subtract(10, 4)
print(f"10 - 4 = {result}")

# Multiplying numbers
result = calc.multiply(2, 7)
print(f"2 * 7 = {result}")

# Dividing numbers
try:
    result = calc.divide(10, 2)
    print(f"10 / 2 = {result}")

    # Attempting division by zero
    result = calc.divide(10, 0)
    print(f"10 / 0 = {result}")
except ZeroDivisionError as e:
    print(e)


# 7. Define a class `Car`
class Car:
    """A class to represent a car."""

    total_cars = 0  # Class variable to keep track of the total number of cars

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Initializes a new car instance.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            year (int): The year the car was manufactured.
        """
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += (
            1  # Increment the total number of cars each time a new car is created
        )

    @classmethod
    def get_total_cars(cls) -> int:
        """
        Returns the total number of cars created.

        Args:
            cls: The class itself (automatically passed by Python).

        Returns:
            int: The total number of cars created.
        """
        return cls.total_cars


# 8. Create multiple `Car` instances and use the `get_total_cars()`
# method to display the total number of cars.
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Mustang", 2022)

# Display total number of cars created
print(f"Total cars created: {Car.get_total_cars()}")  # Output: Total cars created: 3


# 9. Define a class `Account'.
class Account:
    """A class to represent a bank account."""

    def __init__(self, balance: float) -> None:
        """
        Initializes an account instance with a given balance.

        Args:
            balance (float): The initial balance of the account.
        """
        self.balance = balance

    def deposit(self, amount: float) -> "Account":
        """
        Deposits a certain amount into the account.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            Account: The current account instance for method chaining.
        """
        if amount > 0:
            self.balance += amount
        return self

    def withdraw(self, amount: float) -> "Account":
        """
        Withdraws a certain amount from the account, if funds are available.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            Account: The current account instance for method chaining.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount.")
        return self

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.balance


# 10. Create an `Account` instance and use method chaining to deposit and withdraw money.
account = Account(1000.0)  # Create an account with an initial balance of 1000
account.deposit(200).withdraw(150)  # Deposit 200 and withdraw 150 using method chaining

print(f"Current balance: ${account.get_balance()}")  # Output: Current balance: $1050.0
