# Decorators with arguments
# Nesting the decorator_function() within prefix_decorator(prefix) function()
# And then adding Prefix_decorator(arg) decorator to display_info(name, age) function

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix,'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__)
            return result
        return wrapper_function
    return decorator_function # returning decorator_function unexecuted

@prefix_decorator('TESTING:')
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('John', 25)
display_info('Travis', 30)