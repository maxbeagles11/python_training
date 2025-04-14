"""In this script we will cover how the OOP concept 'inheritance'
works when dealing with multiple classes in a script.

Inheritance allows us to create a new class that is based on an
existing class. The new class, called the 'child' or 'subclass',
inherits the attributes and methods from the 'parent' or 'superclass'.
This helps avoid code repetition and allows us to build upon existing functionality.

In Python, inheritance is implemented by passing the parent class as
an argument to the child class. The child class can then access
or override methods and attributes from the parent class.

"""

# -------------------------
# Example 1: Basic Inheritance
# -------------------------


# Let's define a base class (Parent class) called Animal
class Animal:
    """Parent class that represents general properties of an animal."""

    def __init__(self, name: str, age: int = 1) -> None:
        """The constructor for the Animal class.

        Args:
            name (str): Name of the animal.
            age (int): Age of the animal. Defaults to 1.
        """
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Method that is common to all animals."""
        print(f"{self.name} makes a sound.")


# Now, let's create a child class that inherits from Animal
class Dog(Animal):
    """Child class that represents a Dog, inheriting from Animal."""

    def __init__(self, name: str, age: int, breed: str) -> None:
        """The constructor for the Dog class.

        Args:
            name (str): Name of the dog.
            age (int): Age of the dog.
            breed (str): Breed of the dog.
        """
        # Call the parent class constructor (super()) to initialize common attributes
        super().__init__(name, age)
        # For more on the super function, please look at the bottom of this script.
        self.breed = breed

    def speak(self) -> None:  # This is an example of Polymorphism!
        """Override the speak method to customize for dogs."""
        print(f"{self.name} barks!")


# Create instances of both Animal and Dog classes
animal = Animal("Generic Animal", 5)
dog = Dog("Rex", 3, "Beagle")

# Call methods
animal.speak()  # Output: Generic Animal makes a sound.
dog.speak()  # Output: Rex barks!

# -------------------------------
# Example 2: Multiple Inheritance
# -------------------------------

# Python allows multiple inheritance, where a class can inherit from more than one parent class.


class Runner:
    """A mixin class representing the ability to run."""

    def run(self) -> None:
        """Print that someone is running."""
        print(f"{self.name} is running!")


class Swimmer:
    """A mixin class representing the ability to swim."""

    def swim(self) -> None:
        """Print that someone is swimming."""
        print(f"{self.name} is swimming!")


class Athlete(Dog, Runner, Swimmer):
    """A class that inherits from Dog, Runner, and Swimmer."""

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)


# Create an instance of Athlete, which can both bark and perform running and swimming actions
athlete = Athlete("Bolt", 29, "Greyhound")
athlete.speak()  # Inherited from Dog class: Bolt barks!
athlete.run()  # Inherited from Runner class: Bolt is running!
athlete.swim()  # Inherited from Swimmer class: Bolt is swimming!

# -------------------------
# Inheritance Key Concepts
# -------------------------
# - Child classes inherit methods and properties from parent classes.
# - Methods in the child class can be overridden to provide specific behavior.
# - A child class can use the 'super()' function to call methods from the parent class.
# - Multiple inheritance allows a class to inherit from more than one parent class.

# -------------------------
# What is super()?
# -------------------------
# In the Dog class, we use `super().__init__(name, age)` to call the constructor
# of the parent class (Animal). This allows us to initialize the common
# attributes (name and age) in Animal without re-writing the same code in Dog.

# --------------------------------
# Multiple Inheritance and super()
# --------------------------------
# In the Athlete class, we are using multiple inheritance (from Dog, Runner, Swimmer).
# When we call `super().__init__(name, age, breed)`, Python follows the MRO
# (Method Resolution Order) to determine which class’s constructor to call.
# In this case, it first calls the `__init__` method of the Dog class because
# it is the first class in the MRO, which was determined by the class hierarchy.
