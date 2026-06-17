# First-Class Functions
# "A programming language is said to have first-class functions if it treats functions as first-class citizens."

# First-Class Citizen (Programming):
# A first-class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable

# i.e. You should be able to treat functions just like any other object or variable

def square(x):
    return x * x

# f = square()

# Assigning function as a variable
f = square
# Taking out the parentheses, if you put parenthesis in a function then it will execute and we dont want to execute so we removed the parenthesis

print(square)
print(f) # f = square function
# i.e. we can treat f as square function now

print(f(5)) # 25

def cube(x):
    return x * x * x

# Function as arguments
# If a function accepts other functions as arguments or returns functions as their results , it is called as a higher order function

# Custom built map function which is gonna behave like built in map function
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

# We dont want to execute our square function hence we wrote it like this - square, not square()
squares = my_map(square, [1,2,3,4,5])
print(squares)


cubes = my_map(cube, [1,2,3,4,5])
print(cubes)


# Return a function from another function
def logger(msg):
    
    def log_message():
        print('Log:', msg)

    # No parenthesis so function didnt get executed this time
    return log_message

log_hi = logger('hi')
# This is what we call "Closures"
log_hi()


def html_tag(tag):

    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text

print_h1 = html_tag('h1')
print(print_h1) # Function html_tag.wrap_text at --- ---
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print(print_p) # Function html_tag.wrap_text at --- ---
print_p('Test paragraph!')
print_p('Another paragraph!')