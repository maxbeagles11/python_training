"""In this script we will cover the basics of loops.
Loops are used to repeat actions within a script. They're a great way to
iterate over data structures and can be extremely useful for algorithms, data validation, or simply reducing repetitive code.

Python has two main types of loops:
1. 'for' loops -> used when you want to iterate over a sequence.
    a. Example sequences:
        i. list
        ii. string
        iii. range
2. 'while' loops -> used when you want to keep looping as long as a condition is True.
    a. This is very useful for when you want a script to keep running for a long time.
    b. Note: Be VERY careful with these loops — they can easily lead to
    infinite loops if your condition never becomes False.
    This can cause programs to hang or crash depending on the situation.

"""

# ********************************************************************
# FOR LOOPS
# ********************************************************************

# A for loop is useful when you know in advance how many times you want to loop.
# Commonly used with ranges and collections (like lists, strings, etc.).

# When using a for loop, note that you are defining a temporary variable
# that represents each member of the object you are looping through.
# This means that the `scope` of the variable is confined to the loop.
# We will cover scope more in the section 03_functions.

print("Counting from 1 to 5:")
for i in range(1, 6):  # range(start, stop) — goes up to but does not include stop
    print(i)

print("\nLooping through a list of fruits:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}")

# Looping through a string
print("\nCharacters in a word:")
for letter in "hello":
    print(letter)

# Looping with index using enumerate
print("\nIndexed loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Looping through a dictionary's keys
creds = {"bugothan": "bad_password", "chubbstin": "good_password2345gaws45t34"}

for username in creds.keys():
    print(f"The password for user {username} is {creds[username]}")

# Looping through all of the items within a dictionary
for username, password in creds.items():
    print(f"The password for user {username} is {password}")


# ********************************************************************
# WHILE LOOPS
# ********************************************************************

# A while loop is useful when you want to repeat something until a condition changes.

count = 0
print("\nUsing a while loop to count to 3:")
while count < 3:
    print(f"Count is {count}")
    count += 1  # Don't forget to update your condition or you'll get an infinite loop!

# A practical use: user input simulation
print("\nPretend user is entering a password...")
user_input = ""
correct_password = "secret"

while user_input != correct_password:
    user_input = "secret"  # In reality, you'd use input("Enter password: ")
    print("Trying again...")

print("Access granted!")


# ********************************************************************
# CONTROL FLOW KEYWORDS: break, continue, and else with loops
# ********************************************************************

# break: exit the loop early
print("\nFinding the first number divisible by 7:")
for i in range(1, 20):
    if i % 7 == 0:
        print(f"Found it: {i}")
        break  # stops the loop as soon as the condition is met

# continue: skip the current iteration
print("\nSkipping even numbers:")
for i in range(1, 6):
    if i % 2 == 0:
        continue  # skip the rest of the loop for this iteration
    print(i)

# else clause on loops: runs *only* if the loop wasn’t broken out of
print("\nChecking for prime numbers:")
number = 29

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number.")
        break
else:
    print(f"{number} is a prime number!")

# ********************************************************************
# Summary
# ********************************************************************
# - Use 'for' loops when working with collections or ranges.
# - Use 'while' loops when looping based on a condition.
# - 'break' exits a loop early, 'continue' skips to the next iteration.
# - 'else' on loops runs only if the loop wasn't broken out of.
#
# Note the use of the keyword `in` throughout this script. This simple
# operator makes Python extremely versatile since it works across many
# different structures. It's one of the best things about Python in my
# opinion :)
#
# Try changing some of the variables above or write your own loops
# to reinforce how control flow behaves in Python!
