no_of_item = 12 # This is an integer data-type, usually whole number
height = 175.8  # This is a float data-type, this are usually decimal digit
is_sunny = False # This is a bool datatype, checks if true or false
item = "pizza" # This is a string data-type, usually written words.

print(no_of_item)
print(height)
print(is_sunny)
print(item)

###Casting( change a data-type to another,) nb: can't change string to int or float

item = str(is_sunny)
is_sunny = int(height)
height = bool(not is_sunny)
no_of_item = float(no_of_item)

print(is_sunny)
print(item)
print(no_of_item)
print(height)
