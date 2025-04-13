"""In this script we will cover how to gracefully handle
errors and failures using Python's 'try' and 'except' mechanism.

This is part of control flow because it lets your program decide *what to do* when
something goes wrong.

Sometimes, your program may encounter unexpected situations — like dividing by zero,
reading a missing file, or working with a bad user input. Normally, these would crash
your script. But with `try` and `except`, you can control how your program reacts
to those errors.

Key concepts:
1. `try` block -> Code that might cause an error goes here.
2. `except` block -> What to do *if* an error happens.
3. `else` block -> Runs *only* if there were no exceptions.
4. `finally` block -> Runs *no matter what*, whether an error occurred or not.

"""

# TODO: Add a reference of all exception types

# ********************************************************************
# Basic try/except example
# ********************************************************************

print("Let's try dividing numbers:")

try:
    x = 10
    y = 0
    result = x / y  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")

# ********************************************************************
# Catching multiple types of exceptions
# ********************************************************************

print("\nTrying multiple error types:")

try:
    my_list = [1, 2, 3]
    index = 5
    print(my_list[index])  # This will raise an IndexError
except IndexError:
    print("That index doesn't exist in the list!")
except Exception as e:  # the 'as e' is just renaming the 'Exception' object
    print(f"Something else went wrong: {e}")

# ********************************************************************
# Using else and finally
# ********************************************************************

print("\nUsing else and finally:")

try:
    a = 5
    b = 2
    print(f"Result: {a / b}")
except ZeroDivisionError:
    print("Division by zero detected!")
else:
    print("Division successful!")
finally:
    print("This code runs no matter what.")

# ********************************************************************
# Manually raising exceptions
# ********************************************************************

# There might be times where you want to control *when* an exception happens.
# This can be useful for flagging issues with your script and/or user input.


def validate_age(age):
    if age < 0:
        raise ValueError("Age can't be negative.")
    print(f"Your age is {age}")


print("\nValidating user input:")

try:
    user_age = -1
    validate_age(user_age)
except ValueError as err:
    print(f"Invalid age: {err}")

# ********************************************************************
# Summary
# ********************************************************************

# try       -> Attempt to run code that might cause an error.
# except    -> Handle what to do if an error occurs.
# else      -> Run this if no exception was raised.
# finally   -> Always run this block, whether or not there was an error.

# Common exceptions you might encounter:
# - ZeroDivisionError: Dividing by zero
# - IndexError: List index out of range
# - KeyError: Accessing a non-existent dict key
# - ValueError: Wrong type of value (e.g. int("abc"))
# - TypeError: Invalid operation for a data type
# - FileNotFoundError: File you're trying to open doesn't exist

# Avoid catching Exception or using 'except:' unless you really need to —
# it can hide useful error messages while debugging. It's also not very good
# practice in general.

# Use exception handling to make your code more robust and user-friendly.
# It’s better than letting your script crash!
