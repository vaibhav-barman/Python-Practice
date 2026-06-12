# Functions

# Empty Function
def hello_func():  # Initializing a function using def
    pass


print(hello_func)  # Printing Hexadecimal number representing memory address where python function hello_func is stores in your computer's RAM
print(hello_func())  # Printing the output of hello_func()

# Hello function


def hello():
    print('Hello Function!')


hello()

# Why to use functions Explanation
print('Hello Function!')
print('Hello Function!')
print('Hello Function!')
print('Hello Function!')

print()

# Using functions will result in less repeated code
# DRY code - Don't Repeat Yourself
hello()
hello()
hello()
hello()
# And suppose you want to edit the text then in print('Hello Function!') you will have to edit it on each statement but in function, you have to edit it once only

print()


def hello():
    return 'Hello Function!'

# Return Statement explanation
# The main difference is that print() is for humans to see, while return is for the computer to use. When a function uses print(), it simply displays text on your screen so you can read it, but the computer immediately forgets that value and cannot use it for any future calculations. In contrast, when a function uses return, it stops running and hands a specific piece of data back to your main program. This allows you to catch that data, save it into a variable, and pass it into other functions or reuse it later in your code
# Example for return
# print(len('Test')) # This returns 4
# Hello() returns a string, so you can use methods on it
# NOTE: It instantly exits the function and The default is None


print(hello())
print(hello().upper())


# Default value of name is You (if you put any other value then You wont be printed)
def hello(greeting, name='You'):
    # greeting is a positional argument and name is a keyword argument
    return '{}, {} Function.'.format(greeting, name)


print(hello('Hey'))
print(hello('Hey', 'Sarah'))  # 'Sarah' overrides ie name = 'Sarah'


# *args and **kwargs - standard naming convention using args and kwargs - can use different names
# Accepting an arbitrary number of position/keyword arguments
def student_info(*args, **kwargs):
    # these are allowing us to accept a number of positional/keyword arguments
    print(args)  # tuple
    print(kwargs)  # dictionary

# Method 1
# student_info('Math', 'Art', name='John', age=22)

# Output : ('Math', 'Art')
#          {'name': 'John', 'age': 22}

# * and ** represents we dont know how many arguments will there be

# *args - positional arguments - Collects any number of positional arguments into a single tuple
# The magic symbol: The single asterisk * is what tells Python to pack the arguments. The word args is just a standard naming convention; you could name it *inputs.

# **kwargs - keyword arguments - Collects any number of named/keyword arguments into a single dictionary
# The magic symbol: The double asterisk ** tells Python to pack named pairs. The word kwargs stands for "keyword arguments."


# Method 2
courses = ["Maths", "Art"]
info = {'name': 'John', 'age': 22}

# Packs argumentions as a whole
student_info(courses, info)
# Without asterisks: The function receives 2 arguments (a single list and a single dict).

# Unpacking arguments into a function
student_info(*courses, **info)
# With asterisks: The function receives 4 arguments (two separate strings and two separate keyword pairs).


# Example from Python Standard Library

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# The month_days array lookup is a pattern called a Lookup Table or Direct Indexing

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    # This above line is called a docstring - this help document what a function or a class is supposed to do
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12: # this pattern is called Guard Clause - filtering out bad input immediately to keep the rest of the code clean
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month] # square brackets are for lookups and collections

# You cannot store a value in return 
# ex - return a = 4

print(is_leap(2020)) # round brackets are used to call functions 
print(days_in_month(2017, 2))
print(days_in_month(2020, 2))