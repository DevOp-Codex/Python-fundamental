### This is a comment, the '#' is used to begin a comment
## Variables 
# Declaration of variables

digit = 45
name = "Codex"
height = 17.5
is_rainy = True

# Multiple Declaration of variable

age, location, weight, eligible = 22, "Greater Accra", 67.91, False
# OR
cars = "bugatti","ferrari","toyota","camry"
user1, user2, user3, user4 = cars
# OR
rice = beans = onion = "$5000"
# Data Types

no_of_item = 12 # This is an integer data-type, usually whole number
height = 175.8  # This is a float data-type, this are usually decimal digit
is_sunny = False # This is a bool datatype, checks if true or false
item = "pizza" # This is a string data-type, usually written words.

# Casting( change a data-type to another,) nb: can't change string to int or float

item = str(is_sunny)
is_sunny = int(height)
height = bool(not is_sunny)
no_of_item = float(no_of_item)

# Input and Output
# Use "input()" to collect data from user and "Print()" to display output

print(name)
print(height)
print(digit)
print()    # Examples of output form declared variables.
print(user1)
print(user2)
print(user3)
print(user4)
           # Examples of output form declared variables.
print(no_of_item)
print(height)
print(is_sunny)
print(item)
           # Examples of output form declared variables.
print(type(is_sunny))
print(type(item))
print(type(no_of_item))
print(type(height))

day = input(" What day would you like to start?: ") # This takes input from the user.
print(day)
