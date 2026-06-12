# Sets - we use curly braces in sets {}
# Un-ordered
# Sets throw away duplicates

courses = {'History', 'Math', 'Physics', 'CompSci'}
courses_2 = {'History', 'Math', 'Art', 'Design'}

print(courses) # Orders change with each execution

# Membership tests - Special in sets
# Lists and Tuples are slow, but sets results are instant because it uses Hash Table, python can jump to the exact memory location of the item to see if it is there

# Time Complexivity 
# Sets - O(1) constant time complexivity, tuples/lists - O(n) time complexivity
# More efficient Membership tests in Sets
print('Math' in courses)

# Finding common courses between both sets
print(courses.intersection(courses_2)) # Output: {'Math', 'History'}/{'History', 'Math'}

# Finding different courses between both sets
print(courses.difference(courses_2)) # Output: {'CompSci', 'Physics'}/{'Physics', 'CompSci'}

# Combining all of the values between both sets without any duplicates
print(courses.union(courses_2))

# Sets are used for these kind of operations and are much more performant for these operations.

# Empty Set
empty_set = {} # This isn't right! It's a dictionary
empty_set = set() # Creates an emoty set