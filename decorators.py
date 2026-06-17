# DECORATORS
from functools import wraps
# First-class functions allow us to treat functions like any other objects.

# Closures allows us to take advantage of first class functions and return an inner function that remembers and has access to variables local to the scope in which they were created.

def outer_function(msg):
    def inner_function():
        # message variable wasnt created in inner_function but the inner function does have access to it, this is what we call a free variable.
        print(msg)
    return inner_function


# That's what a closure is it remembers message variable even though the outer function is finished executed

# my_func = outer_function()

# my_func()
# my_func()

hi_func = outer_function('hi')
hello_func = outer_function('hello')
hey_func = outer_function('hey')

hi_func()
hello_func()
hey_func()

# A decorator is just a function that takes another function as an argument, adds some kind of functionality and then returns another function
# I.E., A decorator adds some decorations to a function, returning a decorated function
# All of this without altering the source code of the original function that you passed in

# Method 1 - Decorator function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before: {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


# Method 2 - Decorator Class
# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwargs): # Call method (Dunder call)
#         print(f'call method executed this before {self.original_function.__name__}')
#         return self.original_function(*args, **kwargs)


# This is how we usually see decorators - @decorator_function
# This is the same thing as setting our original function equal to the function wrapped within our decorator
@decorator_function # this means that i want my display function equal to decorator_function(display) with this display function passed in
# @decorator_class
def display():
    print('display function ran')

# The decorator function wouldn't work if our original function took in some argument
@decorator_function # TypeError - decorator_function.<locals>.wrapper_function() takes 0 positional arguments but 2 were given
# How to not get this TypeError is by adding *args and **kwargs to our original wrapper function
# @decorator_class
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('John', 25)

# Calling With Decorators
display()



# Calling Without Decorator  
# decorated_display = decorator_function(display)
# decorated_display() # display function ran

# Decorating our functions allows us to easily add functionality to our existing functions by adding that functionality inside a wrapper


# Probably one of the most common usecases of decorators in python is logging


# Practical Examples for Decorators
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func) # wraps decorator
    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args: {args}, and kwargs: {kwargs}'
        )
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print(f'display_info ran with arguments: ({name}, {age})')

display_info('Hank', 30)



# Another example - Timing how long functions run

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result
    
    return wrapper

import time

# Applying both of these decorators to one function - just stack them
@my_logger # display_info = my_logger(display_info)
@my_timer # display_info = my_timer(display_info)
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran with arguments: ({name}, {age})')


display_info = my_timer(display_info)
print(display_info.__name__) # now it is changed to display_info due to @wraps(orig_func)
# display_info('Hank', 30) # display_info ran in: 1.0006935596466064 sec - without @my_logger

# With @my_logger
# display_info('Hank', 30) # wrapper ran in: 1.0012316703796387 sec
# But we dont want wrapper here, we want display_info, so switch the order of my_logger and my_timer

# With @my_logger on top and @my_timer on bottom
display_info('Tom', 22) # display_info ran in: 1.0007667541503906 sec

# What is the stacked version of both the decorators equal to? - 121 and 122 - lower one gets executed first and the higher one get executed after that
# display_info = my_logger(my_timer(display_info))