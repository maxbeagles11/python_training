"""In this script we will cover how to define a class.

A class is comprised of two main components:
1. Attributes -> Class-specific variables/properties.
2. Methods -> Class-specific functions.

A class is basically what we've come to know as an "object".
Spoiler: You've already been using Python's built-in classes!

Let's take a look at a list variable for example:
my_list = [0,1,2]

my_list.append() <- this is a the 'list' class append method!
my_list.__len__ <- this is a private attribute showing how many elements are in the list

------------------------------------------

We will focus on these key areas:
1. Defining attributes and methods.
2. Using constructors and destructors.
3. Private vs public attributes.

"""

# -------------------------
# 01. Defining a simple class
# -------------------------

# Similar to function names, classes also have rules for naming as well.
# 1. Class names typically use CamelCase (e.g., Dog, Car, Person)
# 2. Class names should be descriptive of what the class represents.


class Dog:
    """
    A simple class to demonstrate the concepts of attributes, methods,
    constructors, destructors, and private vs public attributes.
    """

    # Constructor (__init__): Used to initialize attributes when an object is created
    def __init__(self, name: str, age: int) -> None:
        """
        Constructor method. This is automatically called when a new object is created.

        Args:
        ----
            name (str): The dog's name.
            age (int): The dog's age.
        """
        # Public attributes
        self.name = name
        self.age = age

        # Private attribute (name prefixed with an underscore)
        # Technically this is still accessible, but should be avoided!
        self._private_info = (
            "This is private and not directly accessible outside the class."
        )

        # In Python, privacy is just a convention. A leading underscore means
        # "don't touch this unless you know what you're doing".

        # Name mangling with double underscores
        # This makes it harder (but not impossible) to access from the outside.
        self.__more_private_info = "This is name-mangled to discourage external access."

        print(f"Dog object created: {self.name}, {self.age} years old.")

    # __str__ helps define how your object should look when printed.
    # It’s what Python calls when you use print(my_object).
    # Ex: print(dog1)
    def __str__(self) -> str:
        """Returns a string representation of the Dog object."""
        return f"{self.name} is {self.age} years old."

    # Method: An example method that prints a greeting
    def greet(self) -> None:
        """Prints a greeting from the dog."""
        print(f"Woof! I'm {self.name}, and I'm {self.age} years old!")

    # Public method to access private information (getter)
    def get_private_info(self) -> str:
        """Returns the private info of the dog."""
        return self._private_info

    # Method to increment the dog's age (example of a method that modifies attributes)
    def have_birthday(self) -> None:
        """Increases the dog's age by 1 year."""
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

    # Destructor (__del__): Called when an object is about to be destroyed
    def __del__(self) -> None:
        """
        Destructor method. Automatically called when the object is deleted or goes out of scope.
        """
        print(f"{self.name} is being deleted.")


# Be sure to use triple-quoted strings below class and method definitions to describe
# what they do. These docstrings are helpful for documentation and tools like help().
print(help(Dog))

# -------------------------
# 03. Understanding 'self'
# -------------------------

# You may have noticed that every method inside the class has 'self' as its first parameter.

# In Python, when you define a method inside a class, it automatically becomes an *instance method*.
# That means it operates on an instance (or object) of the class.

# The keyword 'self' is a reference to the current instance of the class.
# It lets you:
# - Access or modify the object’s attributes (like self.name, self.age)
# - Call other methods inside the class (like self.greet())

# You can think of 'self' as "this particular dog" when you're talking about the object.
# It's required in method definitions, but when calling the method, Python passes it automatically.


# Here's an example.
class Example:
    """A quick example showing how 'self' works in a class."""

    def __init__(self, value: int = 0) -> None:
        """The constructor of the Example class.

        Args:
            value (int, optional): The value passed into the class. Defaults to 0.
        """
        # Note: Methods, including the constructor, can have default values like functions can.
        self.value = (
            value  # 'self.value' refers to the attribute of the specific object
        )

    def show_value(self) -> None:
        """Print the value entered in the constructor."""
        print("Value is:", self.value)


# Now, we create an object:
ex = Example(42)

# This will output: Value is: 42
ex.show_value()

# Even though we called 'ex.show_value()', Python behind the scenes does:
# Example.show_value(ex)
# That’s why we don’t pass 'self' when calling the method — it’s implicit.


# -------------------------
# 03. Creating and interacting with an object
# -------------------------

# Creating an object of the Dog class
dog1 = Dog("Buddy", 5)

# Calling the greet method
dog1.greet()

# Accessing the public attribute directly
print(f"{dog1.name} is {dog1.age} years old.")

# Accessing a private attribute using a method
print(dog1.get_private_info())

# Incrementing the dog's age using the have_birthday method
dog1.have_birthday()

# Accessing a single underscore private attribute (not recommended, but possible)
print(dog1._private_info)  # This will work, though it’s considered bad practice

# Accessing a double underscore name-mangled attribute
# This will raise an error:
# print(dog1.__more_private_info)

# But you can still access it like this:
print(dog1._Dog__more_private_info)  # Name mangling: _ClassName__attribute
# Double underscores trigger name mangling, which changes the attribute name internally.
# It's not true privacy — just a stronger deterrent than a single underscore.

# Inspecting an object's class
print(type(dog1))  # <class '__main__.Dog'>
print(isinstance(dog1, Dog))  # True

# Class objects are mutable by default
dog1.age = 10  # We just modified the instance's attribute
print(dog1)  # Buddy is now 10 years old

# Deleting the object explicitly to trigger the destructor
# We normally don't do this ourselves since Python's garbage collection
# does it automatically.
del dog1


# -------------------------
# 📝 Summary: What We Learned About Classes
# -------------------------


# Here's what we covered in this lesson on classes and objects:
#
# ✅ Classes are blueprints for creating objects.
#     - They define *attributes* (variables) and *methods* (functions tied to the object).
#
# ✅ The `__init__` method (constructor) sets up the initial state of an object when it's created.
#
# ✅ The `self` keyword refers to the current instance of the class.
#     - It allows you to access and modify the object's attributes and call its methods.
#
# ✅ You can create *public* and *private* attributes.
#     - A single underscore (_) is a convention to signal "private" use.
#     - Double underscores (__) trigger *name mangling*, which makes the attribute harder to access from outside the class.
#
# ✅ The `__str__` method controls what happens when you print an object.
#     - It lets you customize how your object appears as a string.
#
# ✅ The `__del__` method (destructor) runs when an object is deleted or goes out of scope.
#     - Usually handled automatically by Python's garbage collector.
#
# ✅ Objects are mutable by default.
#     - You can update their attributes at any time unless explicitly restricted.
#
# ✅ You can inspect objects using:
#     - `type(obj)` to see its type
#     - `isinstance(obj, ClassName)` to check if it's a specific type
#
# 🎉 Congrats! You've just seen your first custom Python class built from scratch and explored what makes OOP in Python so # powerful and flexible.
