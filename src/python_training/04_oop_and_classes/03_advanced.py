"""In this script, we will cover advanced class concepts such as:

1. Decorators -> Including `@property` to make methods behave like attributes.
2. Class Methods -> Methods that are bound to the class and not the instance.
3. Class Variables -> Variables that are shared by all instances of the class.
4. Static Methods -> Methods that do not depend on class or instance data.
5. Method Chaining -> Returning `self` from methods for fluent interfaces.

These concepts will help you write more flexible, efficient, and readable Python code.

"""

# ------------------------------
# 1. Property Decorators
# ------------------------------


class Circle:
    """A class representing a circle with a radius."""

    def __init__(self, radius: float) -> None:
        """Initializes a circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self._radius = radius  # Private attribute

    @property
    def radius(self) -> float:
        """Gets the radius of the circle.

        Returns:
            float: The current radius of the circle.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """Sets the radius of the circle with validation.

        Args:
            value (float): The new radius value to set.

        Raises:
            ValueError: If the radius value is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("Radius must be positive!")
        self._radius = value

    @property
    def area(self) -> float:
        """Calculates and gets the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14159 * (self._radius**2)


circle = Circle(5)
print(f"Circle radius: {circle.radius}")  # Calls the getter
print(f"Circle area: {circle.area}")  # Calls the property getter for area

circle.radius = 10  # Calls the setter
print(f"Updated circle radius: {circle.radius}")
print(f"Updated circle area: {circle.area}")

# ------------------------------
# 2. Class Methods
# ------------------------------


class Dog:
    """A class representing a dog."""

    species = "Canis familiaris"  # Class variable

    def __init__(self, name: str, breed: str) -> None:
        """Initializes a dog with a name and breed.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
        """
        self.name = name
        self.breed = breed

    @classmethod
    def from_string(cls, dog_str: str) -> "Dog":
        """Creates a Dog instance from a string in the format 'name-breed'.

        Explanation of `cls`:
        The `cls` parameter is a reference to the class itself, similar to how `self` refers to the instance.
        It is used in class methods to interact with the class itself rather than individual instances.
        In this case, we use `cls` to create a new instance of the `Dog` class.
        Note: 'cls' and 'self' are just *conventions*. However, it's best practice not to deviate from these
        as it makes code more universally readable.

        Args:
            dog_str (str): A string containing the dog's name and breed separated by a hyphen.

        Returns:
            Dog: A new Dog instance.
        """
        name, breed = dog_str.split("-")
        return cls(name, breed)

    @classmethod
    def get_species(cls) -> str:
        """Gets the species of the dog.

        Returns:
            str: The species of the dog.
        """
        return cls.species


# Create a Dog instance using the class method
dog1 = Dog.from_string("Max-Beagle")
print(f"Dog name: {dog1.name}, Breed: {dog1.breed}")

# Access the class method
print(f"Dog species: {Dog.get_species()}")

# ------------------------------
# 3. Class Variables
# ------------------------------


class Cat:
    """A class representing a cat."""

    species = "Felis catus"  # Class variable

    def __init__(self, name: str) -> None:
        """Initializes a cat with a name.

        Args:
            name (str): The name of the cat.
        """
        self.name = name  # instance variable
        self.age = 0  # instance variable

    def birthday(self) -> None:
        """Increases the cat's age by 1 year."""
        self.age += 1

    @classmethod
    def get_species(cls) -> str:
        """Gets the species of the cat.

        Returns:
            str: The species of the cat.
        """
        return cls.species


# Create instances of Cat
cat1 = Cat("Luna")
cat2 = Cat("Whiskers")

cat1.birthday()
print(f"{cat1.name} is {cat1.age} years old.")
print(f"{cat2.name} is {cat2.age} years old.")

# All instances share the class variable 'species'
print(f"Species of cat1: {cat1.species}")
print(f"Species of cat2: {cat2.species}")
print(f"Species of Cat class: {Cat.species}")

# ------------------------------
# 4. Static Methods
# ------------------------------


class MathUtils:
    """A class with static methods for mathematical operations."""

    @staticmethod
    def add(x: int, y: int) -> int:
        """Adds two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The sum of x and y.
        """
        return x + y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        """Multiplies two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The product of x and y.
        """
        return x * y


# Static methods can be called on the class itself without creating an instance
print(MathUtils.add(2, 3))  # Output: 5
print(MathUtils.multiply(2, 3))  # Output: 6

# ------------------------------
# 5. Method Chaining
# ------------------------------


class Builder:
    """A builder class that demonstrates method chaining."""

    def __init__(self) -> None:
        """Initializes the builder with a starting value of 0."""
        self.value = 0

    def add(self, x: int) -> "Builder":
        """Adds x to the current value and returns the object itself.

        Args:
            x (int): The value to add.

        Returns:
            Builder: The builder instance, allowing method chaining.
        """
        self.value += x
        return self

    def subtract(self, x: int) -> "Builder":
        """Subtracts x from the current value and returns the object itself.

        Args:
            x (int): The value to subtract.

        Returns:
            Builder: The builder instance, allowing method chaining.
        """
        self.value -= x
        return self

    def get_value(self) -> int:
        """Returns the current value of the builder.

        Returns:
            int: The current value.
        """
        return self.value


# Method chaining in action
builder = Builder()
result = builder.add(5).subtract(2).add(10).get_value()
print(f"Result after chaining: {result}")

# ------------------------------
# Advanced Class Concepts Recap
# ------------------------------
# 1. @property (example of a decorator): Makes methods behave like attributes and allows you to control access.
# 2. Class Methods: Methods bound to the class, often used for factory methods.
# 3. Class Variables: Variables shared by all instances of a class.
# 4. Static Methods: Methods not bound to instances or the class, useful for utility functions.
# 5. Method Chaining: Allows multiple method calls on a single object in a fluent style.
