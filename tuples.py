# Tuples are very similar to list but with one difference, you cant modify a tuple
# Immutable but Ordered

# () Round Brackets / Parentheses are used in tuples

# Explaining the difference

# Mutable - Lists - use these if you want modification
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Immutable - Tuples - use these if you don't want modification
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # TypeError - 'tuple' object does not support item assignment

# print(tuple_1)
# print(tuple_2)

# Empty Tuple
empty_tuple = []
empty_tuple = tuple()