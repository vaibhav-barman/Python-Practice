# Textual data in Python is represented by Strings

# Mnemonics naming

# message = 'Bobby\'s World'
message = "Bobby's World"

paragraph = """Bobby's World was a good
cartoon in the 1990s""" # Multi-line String

# Escaping ' with a backslack - (\')
print(message)
print(paragraph)

# Number of characters in a string
print(len(message))
print(len(paragraph))

# Accessing characters in a string
print(message[0])
print(message[4])
# print(message[13]) # Index out of range cuz index starts from 0


# String Slicing
print(message[0:7]) # 0 is inclusive but 7 is excluded in this case
print(message[:5])
print(message[8:])


# Functions and methods are basically the same thing
# Method is just a function that belongs to an object

# String Methods
print(message.lower())
print(message.upper())

print(message.count('')) # len(message)+1

# len() is a built in function and .count() is a method attached to a specific data type like strings or list, we can call it using dot notation

print(message.count('b'))
print(message.find('World')) # Returns the starting position of the given argument
print(message.find('Universe')) # Will return (-1) if it doesnt contains the given argument

# Replace
message = message.replace('World', 'Universe')
print(message)


greeting = 'Hello'
name = 'Michael'
# message = greeting + ', ' + name + '. Welcome!'

# String Formatting
message = '{}, {}. Welcome!'.format(greeting, name)

print(message)

# For embedding variables {} and expressions directly inside string literals we use f-string
# String Formatting
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)


# Finding all the attributes and methods that we can use on a variable
print(dir(message))

# How to know about the class - Help function
print(help(str.upper))