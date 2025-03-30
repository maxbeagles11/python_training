"""This is called a top-level docstring. We include these to provide
developers (you) with a brief description of the contents of this script.
If you are using VS Code, I highly recommend installing the 'autoDocstring' extension so that
you can automatically generate docstrings (this is especially useful for functions).

In this script, we will cover simple functions (like print), how to properly document
sections of a script, and how things should generally be organized.

I will include more advanced concepts in this, but only to provide better
examples. We'll go more in-depth on these in later sections.
"""

# This is a comment. The Python interpreter will ignore these during execution.
# Developers use these to provide extra context into what their code is doing.
# These are crucial, but it's not the best idea to spam these too much.
# Your code should be simple enough to follow without excessive comments being used.


# ----------------------------------------------
# ----------------------------------------------
# Imports
# ----------------------------------------------
# ----------------------------------------------

# This is called a module import
import os

# Python comes with pre-installed ones like 'os', but you can install
# external ones in your Python environment and then import those as well.
# With this, you have access to ALL 'os' objects and functions.
# Note: All import should always be done at the top of the script.

# This is an explicit import. Unlike 'import os', this will only specifically
# import the objects and functions described by the developer.
from sys import exception  # noqa

# Here are more examples of imports
from datetime import datetime, date, UTC  # noqa
from time import sleep, asctime  # noqa

# If for some reason you want to rename the import, you can do so like this:
from pprint import pprint as pretty_print  # noqa


# ----------------------------------------------
# ----------------------------------------------
# Constants
# ----------------------------------------------
# ----------------------------------------------

# Sometimes our script might require hard-coded values or 'constants'
# to be used. Rather than just using the value itself throughout the script,
# it's good practice to define it at the top of the script, below the module imports.
# That way if we ever need to change it, we only need to modify one line instead of
# each instance of that value.

# Example of a constant. Note: It is best practice to make this in all caps
# to differentiate it from the rest of the code.
ITERATIONS = 10

# Example of this constant being used:
for iteration in range(ITERATIONS):
    print(iteration)

print(f"The number of iterations is: {ITERATIONS}")

double_iterations = ITERATIONS * 2

# Instead of changing '10' at all locations, we can just modify the 'ITERATIONS' once
# to affect the logic of the rest of our code.


# ----------------------------------------------
# ----------------------------------------------
# Docstrings
# ----------------------------------------------
# ----------------------------------------------

# This is called a function. We'll cover these in section 03, but for now
# let's look at how we document one. Don't worry about the syntax or operations
# either.


def add_two_numbers(x: int, y: int) -> int:
    """Add two integers and return their sum.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The sum of x and y.
    """
    return x + y


# Notice how we show the 'type' of the arguments passed into the function.
# This is called 'type annotation' and it helps with readability.
# Note: This does not enforce type checking at runtime, though.
#
# We also do the same for the output (denoted by the '-> int').
#
# We use a docstring to show the following:
#   - Function summary.
#   - Function arguments.
#   - Function return.
#
# This makes it a whole lot easier for developers to follow what your code is doing.
# This is critical when working on a team since it reduces complexity and improves
# readability. You don't want to be the guy that doesn't properly document his code...


# Now let's look at a simple class definition.
# Note: The following is a really dumb class, but it illustrates the
# documentation pretty well.


class Animal:
    """A class abstracting the properties of an animal."""

    def __init__(self, animal_type: str) -> None:
        """The constructor for the Animal class.
        Initializes the type of the Animal.

        Args:
            animal_type (str): The type of the animal.
        """
        self.animal_type = animal_type.lower()
        print("The type of this animal is: " + self.animal_type)

        self._get_animal_info(self.animal_type)

    def _get_animal_info(self, animal_type: str) -> None:
        """Set attributes for the Animal class based on the
        type passed in.

        Args:
            animal_type (str): The type of the animal.
        """
        match animal_type:
            case "dog":
                self.age = 14
                self.breed = "Beagle"
                self.name = "Max"
            case "cat":
                self.age = 1
                self.breed = "Russian Blue"
                self.name = "June"
            case "snake":
                self.age = 3
                self.breed = "King Cobra"
                self.name = "Jormungandr"
            case _:  # default case
                print("Enter a supported animal: dog, cat, or snake.")


# Notice how we put a docstring under the class name as well as each class method.
# Also notice that we didn't use a lot of comments either. This is because the code
# is simple and the docstrings are concise.


# ----------------------------------------------
# ----------------------------------------------
# Simple prints.
# ----------------------------------------------
# ----------------------------------------------

# We use the built-in 'print' function to convey information of our code's execution.
# This can be useful for when we are trying to fix our code (called 'debugging').
# They can also be used for letting the user know what's going on.

print("This is a valid print.")
print(120)  # This is also a valid print.

# Debugging example:
for iteration in range(ITERATIONS):
    if iteration == 5:
        print("The fifth iteration was hit!")

# Sometimes we want to dynamically modify a string we're printing. This is called
# 'formatting the string', which can be done in several ways.
# Note: the '\n' is a newline. There are other things you can do like this, but we
# won't cover those in this training.

# This is my preferred method...but the other ones can also be nice to use.
print(f"I am going to show the number of iterations like so: {ITERATIONS} \n")

print("My iterations are here: {} \n".format(ITERATIONS))

print("The number of iterations are: " + str(ITERATIONS))

# You can include logic in the formatting as well
print(f"The number of iterations doubled is {ITERATIONS * 2} \n")
print(f"The current working directory is: {os.getcwd()} \n")
