"""In this script, we will cover all the available built-in data types
and data structures in Python.

Data types define the kind of data a variable can store. Again, Python is
dynamically typed, so you don't need to explicitly state the type/structure of a variable
when declaring it (which is a huge plus for beginners!).

This is part of the reason I love Python over languages like C and C++. Less annoying BS
to deal with...

Data structures are ways to organize and store data for efficient access
and modification. In Python, some data structures are considered built-in data types.
This includes: lists, dictionaries, tuples, sets (which we'll cover here).

There are other types than those shown here, but for simplicity this is all we'll
cover in this training.

"""

# --------------------------------
# NoneType
# --------------------------------
# 'None' is a unique object in that it represents the absence of a value
# or in other words a 'null' value.
# It is often used to show that a variable has nothing assigned to it or
# that a function does not return anything explicitly.
none_type = None


# --------------------------------
# Numeric types (int, float, complex)
# --------------------------------
x = 10  # int -> This is easy...it's just an integer (whole number).
y = -10  # int -> Just a negative whole number...

pi = 3.14  # float -> A number with decimal points

z = 2 + 3j  # complex -> Real and imaginary components (most people don't use these...)


# --------------------------------
# Boolean (bool)
# --------------------------------
# True or false values...pretty straightforward.
is_active = True
bad_flag = False
# These follow all rules in logic (we won't cover it all here, I suggest watching a YouTube
# video on this subject - it's very interesting and useful!).

# Additionally, some values are 'truthy' or 'falsey' meaning they evaluate to either
# True or False in logical expressions.
example0 = 0  # This is False
example1 = 1  # This is True (same for all nonzero numbers)

non_empty_string = "This is truthy"
empty_string = ""  # This is falsey

non_empty_list = [0, 1, 2]  # This is truthy
empty_list = []  # This is falsey

non_empty_dict = {"a": 10}  # This is truthy
empty_dict = {}  # This is falsey

none_value = None  # This is falsey


# --------------------------------
# Sequence types (str, list, tuple)
# --------------------------------
# These types are used to store collections of items.
# Note: Everything in Python is zero-indexed, meaning that the first element is always
# addressed with '0'.
# Example: my_str = "Hello" -> my_str[0] -> 'H'
# You can also access elements using a negative index to move from the end
# Example: my_str = "Hello World" -> my_str[-1] -> 'd'


# Strings -> Text enclosed in quotes or apostrophes (can be either).
# Strings are immutable, meaning they cannot be modified in place.
# Note: You can grab specific ranges of a string like you would a list (see below).
boy_name = "Bugothan"
girl_name = "Lisa"
# boy_name[0] = "b" # this would fail since you can't modify the string


# Lists -> They are ordered, mutable collections of objects.
# They can include any type of object, including other lists (called a 'nested list').
# The order of elements (or 'positions') are maintained and can be accessed by their 'index'.
numbers = [1, 2, 3]
numbers[0] = 7  # lists are mutable, so this works. Output: [7, 2, 3]
new_list = [1, 1, "a", {}, "n"]  # duplicates are allowed


# Tuples -> They are ordered, immutable collections of objects.
# They have all the same properties as lists, but they cannot be modified just like
# strings. These are useful for when you don't want some data to be modified at all.
my_tuple = (1, "a", [-1, 0])
# my_tuple[0] = 7 # this would fail


# --------------------------------
# Set types (set)
# --------------------------------
# Sets -> They are kind of similar to lists, but they are unordered and do not allow
# duplicates. This means they are mutable, but indexing is not allowed.
# Note: All elements must be 'hashable' (immutable) in a set. You cannot have things like
# lists in a set.
my_set = {1, 2, 3, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

my_set = set([1, 2, 3, 3, 5])  # also valid
print(my_set)  # Output: {1, 2, 3, 5}


# --------------------------------
# Mapping types (dict)
# --------------------------------
# A dictionary (dict) is similar to a hashmap in C++. It is an unordered collection
# of key-value pairs. Dicts are extremely flexible and useful data structures that
# allow for very easy organization of data. Dictionaries are mutable.
# Note: Each key in a dictionary is unique and must be associated with a value.
my_dict = {"key": "value"}
new_dict = {"name": "Bugothan", "age": 72}
print(new_dict["name"])  # Output: "Bugothan"

new_dict["age"] = 45  # this overrides the 72 from before
new_dict["job"] = "engineer"  # adds an element to the dict

# Keys must be immutable/hashable (str, int, float, tuple)
# my_dict = {["a", "b"]: 1}  # TypeError: unhashable type: 'list'


# --------------------------------
# Tips and tricks
# --------------------------------
# If you ever need to know the type of a variable, you can use Python's built-in
# 'type' function!
x = 10
print(type(x))  # Would print 'int' in the terminal.

my_list = [1, "a"]
print(type(my_list))  # Would print "list" in the terminal

# All types in Python are objects, which mean they contain both 'attributes' and
# 'methods' that the developer can access.
# Example:
my_list = ["a", 1, [1, 2, 3]]
my_list.append(
    "Add this",
)  # the 'append' method can be used to add an element to the end
print(my_list)  # Output: ["a", 1, [1, 2, 3], "Add this"]
