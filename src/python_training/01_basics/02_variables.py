"""In this script we will cover how to define variables.

A variable is an object that refers to a value stored in memory.
They are created when we use the assignment operator '='.

Note: Assignment and equality operators are not the same.
    '=' -> assignment (assigns a value to an object)
    '==' -> equality (compares two values/objects)

"""

# The following are variables
x = 10
my_name = "Bugothan"
flag = False

# Python is dynamically typed, so unlike in C we don't need to specify a type
# when we declare a variable. More on types in the next section...

# There are rules for variable names.
#   1. The variable must start with a letter or an underscore.
#       a. valid_Var
#       b. _validVar
#       b 123_invalidVar
#   2. Variable names can contain numbers and underscores.
#   3. You cannot use Python keywords. These are explicitly prohibited.
#       a. if, else, def, class, etc. cannot be used to define a variable
#           i. Bad example -> def = "You can't do this in Python."
#   4. Names are case-sensitive. my_name and My_name are different variables.

# Variables can be reassigned to new values of any type.
x = 15
x = "Now it's a string"

# You can assign multiple variables at once.
a, b, c = 1, 2, 3
a = b = c = 10  # all have the value of '10'

# As we learned in the previous script, you can also have constants.
# Notice how we do not break any of the rules for variable names.
CONSTANT_VAL = 100

# If for some reason you need to clear memory explicitly (Python does this automatically
# at the end of execution), you can use the 'del' keyword.
x = 9
del x  # x can no longer be used

# Note: We can define variables with both 'snake case' or 'camel case'
snake_case = "An example of snake case"
camelCase = "An example of camel case"
# You can use either one you like, but just be sure you stick to one convention.
# Otherwise your code will get messy and ugly...
