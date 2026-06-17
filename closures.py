# Closures

# Wikipedia says, "A closure is a record storing a function together with an environment: a mapping associating each free variable of the function with the value or storage location to which the name was bound when the closure was created. A closure, unlike a plain function, allows the function to access those captured variables through the closure's reference to them, even when the function is invoked outside their scope"

# A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()

# A closure closes over the free variables from their environment and in this case message would be that free variable



# with no arguments in outer_func

# my_func = outer_func()
# print(my_func)
# print(my_func.__name__) # inner_func

# my_func()
# my_func()
# my_func()