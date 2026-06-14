# Syntax
try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass


# Example 1 - FileNotFoundError
try:
    f = open('tst.txt')
    var = bad_var # NameError
except FileNotFoundError as e: # this Exception is kind of vague 
# This General Exception is not just gonna find FileNotFoundError but also other Errors
    print(e)
except Exception:
    print('Sorry, something went wrong')
# # OR
except Exception as e:
    print(e)

# NOTE: If you're putting multiple excepts then make sure to put more specific errors on top and general one on bottom


# Example 2 - Else Block
try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else: # If no error
    print(f.read())
    f.close()


# Example 3 - Finally
# Usecase - Closing a database - regardless if the query is successful or not
# Finally runs either way - whether the code is successful or whether it is not 
try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else: # If no error
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')


# You can raise exceptions on your own, it doesn't have to be something Python would have caught on its own
try:
    f = open('test.txt')
    if f.name == 'test.txt':
        raise Exception # Raising Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else: # If no error
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')