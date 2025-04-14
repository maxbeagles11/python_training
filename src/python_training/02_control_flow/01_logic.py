"""In this script we will cover the basics of logic and creating logical expressions to dictate the behavior of our scripts.

The two main concepts covered here are:
1. Conditional statements using control flow keywords.
    a. Logical expressions are used to make decisions in your code. Based on conditions, the program can choose to do one thing or another.
    b. The main "control flow" keywords for Python are:
        i. 'if' -> The first condition to check.
        ii. 'elif' -> Means "else if". Python combines the two words, unlike some other languages. These are subsequent conditions to check.
        iii. 'else' -> The default if no other conditions are met.

2. Logical operators.
    a. Logical operators serve to further define the expected behavior of the program/script. These are used in conjunction with conditional statements.
    b. The logical operator keywords for Python are the following:
        i. 'or' -> At least one condition must evaluate to True.
        ii. 'and' -> Both conditions must evaluate to True.
        iii. 'not' -> Invert a condition (True -> False, False -> True).
"""
# ********************************************************************
# Let's look at a simple control flow to understand the basics of conditional statements.
# ********************************************************************

temperature = 73

if temperature > 50:  # first condition to check
    print("The temperature is greater than 50!")
elif temperature < 20:  # second condition to check if the previous one is False
    print("The temperature is less than 20!")
else:  # The default if nothing before it evaluates to True
    print("The temperature is between 20 and 50.")

# Here's a better example.
temperature = 10

if temperature > 25:
    print("It's hot!")
elif temperature > 15:
    print("It's warm.")
elif temperature > 5:
    print("It's chilly.")
else:
    print("It's cold!")

# ********************************************************************
# Now lets look at how we can use logical operators in our conditional statements.
# ********************************************************************

is_sunny = True
is_weekend = False

# Using 'and'
if is_sunny and is_weekend:
    print("Great day for a picnic!")
else:
    print("Maybe stay indoors.")

# Using 'or'
if is_sunny or is_weekend:
    print("At least there's *something* to be happy about.")

# Using 'not'
if not is_sunny:
    print("Better bring an umbrella.")


# Combining conditions
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome to the concert!")
else:
    print("Sorry, you can't enter.")

# Boolean expressions can also use parentheses for clarity
if (age > 18 and has_ticket) or is_weekend:
    print("You're in!")
else:
    print("Nope, not today.")

# Reminder:
# Conditions evaluate to either True or False
# Comparison operators include:
#   ==  (equal)
#   !=  (not equal)
#   <   (less than)
#   >   (greater than)
#   <=  (less than or equal to)
#   >=  (greater than or equal to)

# Try changing values of the variables above and see how the script behaves!

# ********************************************************************
# Now lets look at a nice feature stemming from Python 3.10 and newer:
# The match-case statement.
# ********************************************************************

# Think of this like a switch-case in other languages
# It's a clean way to compare one value against many possible options
# Note: This looks a lot better than using a bunch of ugly if-else statements. Definitely keep this one in your toolbox!

day = "Saturday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Last day of the work week!")
    case "Saturday" | "Sunday":  # You can match multiple values with |
        print("It's the weekend!")
    case _:  # The '_' acts like the 'default' case
        print("Just another regular day.")
