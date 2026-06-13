'''
LEGB
Local, Enclosing, Global, Built-in
'''

# Variable Scope - This is what determines where our variables can be accessed from within the program and what values those variables hold in different contexts.

# Example of Global Variable and Local Variable
x = 'global x' # Global scope

def test():
    y = 'local y' # Local scope - within a variable
    # global x # Modify the Global variable instead of creating a new local variable and we dont even need to have the above x = 'global x' defined now
    # Don't use this global statement often 
    x = 'local x'
    # print(y)
    print(x)

test()
# print(y) # NameError because y variable doesnt live outside that test function
print(x) # Works Fine!



def new_test(z): # this z is not gonna exist outside of new_test() function
    # The only difference is that as a function parameter it can now be assigned values that are passed into our function
    x = 'local x'
    print(z)

new_test('local z') # You call the function and pass the string 'local z' into it
# print(z) # NameError : z doesnt live outside of new_test() function


# Built-in scope

# Importing Builtin functions
import builtins

# print(dir(builtins))

# you can overwrite the builtin functions - python doesnt stop you from doing it
# def min():
#     pass

def my_min():
    pass

m = min([5,1,4,2,3]) # TypeError - if you overwrite the built in function
print(m)



# Enclosing Scope - related to function within a function

def outer():
    x = 'outer x' # local to outer()

    def inner():
        nonlocal x # this will allow us to work with local variables of enclosing functions ie we are affecting x which is local to outer()
        x = 'inner x' # local to inner()
        print(x) # first it check if it has any local variable x in inner() then it check outer() for the same

    inner()
    print(x)

outer()

# NOTE: nonlocal is used more than global statement because nonlocal can be used for in order to change closures and decorators as well. 


print()


# Using Global, Local and Enclosing Scope together

a = 'global a'

def new_outer():
    a = 'outer a'

    def new_inner():
        a = 'inner a' # if you comment out this then print within this function will print 'outer a'
        print(a)

    new_inner()
    print(a)

new_outer()
print(a)