# Conditionals

if True:
    print('Conditional was True') # Output: Conditional was True


# Comparisions:
# Equal:                  ==
# Not Equal:              !=
# Greater than:            >
# Less than:               <
# Greater or Equal to:    >=
# Less or Equal to:       <=
# Object Identity:        is - checking if values have the same id or they're the same object in memory

language = 'Python'

if language == 'Python':
    print('Conditional was True') # Output: Conditional was True

if language == 'C++':
    print('Language was C++') # This wont work because if is False
elif language == 'Java':
    print('Language was Java')
else:
    print("Conditional was False")

# Python doesn't have switch-case statement like other languages
# Because the if, elif, else statements are plenty clean enough to do this already

# Boolean operations
# and
# or
# not


user = 'Admin'
logged_in = False


if user == 'Admin' and logged_in:
    print(f'{user} page')
else:
    print(f'Not a {user}')


if user == 'Admin' or logged_in:
    print(f'{user} page')
else:
    print('Bad Creds')


if not logged_in: 
    print('Please log in')
else:
    print('Log in successful')


a = [1,2,3]
b = [1,2,3]

print(a==b) # Output: True

print(id(a))
print(id(b))

print(a is b) # Output: False - because both have different ids

a = b # assigning b's id to a

print(id(a))
print(id(b))

print(a is b) # Output: True

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example '', (), []
    # Any empty mapping. For example {}

condition = False
condition = 0
condition = None
condition = ()
condition = []
condition = ''
condition = {}
# All of these are false
# Opposite of all of these will evaluate to true

condition = {'key'}
condition = 283

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')