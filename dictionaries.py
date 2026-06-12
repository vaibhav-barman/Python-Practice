# Dictionary
# Key-value pair
# Key is a unique identifier where we can find our data and value is the data 

# In other programming languages dictionaries may be called as associative arrays, hashmaps, hash, maps or key-value store

student = {
    'name': 'John Doe',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

print(student) # Prints the student dictionary

# Printing the value of one key
print(student['name']) # Output: John Doe
print(student['age']) # Output: 25
print(student['courses']) # Output: ['Math', 'CompSci']

# print(student[0]) # KeyError: 0 - doesnt exist

# Alternative
print(student.get('name')) # Output: John Doe
print(student.get(0)) # Output: None
# Better to use get method if the key doesn't exist, because it will return None not any error

# Changing the output from None to Not found
print(student.get(0, 'Not Found')) # Output: Not found

# Method - 1
# Adding a new entry to our dictionary 
student['phone'] = '555-555-5555'
student['name'] = 'Jane' # Over-writing (updating) the previous value of 'name'

print(student) # Output: {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-555-5555'}

# Method -2
student.update({'name': 'Jane', 'age': 26, 'phone': '555-444-3333'})

print(student) # Output: {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-444-3333'}

# Delete a specific key and its value
# del student['age']
# print(student)

# POP method - delete a key:value pair and return its value
age = student.pop('age')
print(student) # Output: {'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-444-3333'}
print(age) # Output: 26

# Printing the number of keys
print(len(student)) # Output: 3

# Printing keys of the dictionary
print(student.keys()) # Output: dict_keys(['name', 'courses', 'phone'])

# Printing values of the dictionary
print(student.values()) # Output: dict_values(['Jane', ['Math', 'CompSci'], '555-444-3333'])

# Printing key and value pairs
print(student.items())


print()

# Loop through keys
for key in student:
    print(key)

print()

# Loop through keys and values 
for key, value in student.items():
    print(key, value)