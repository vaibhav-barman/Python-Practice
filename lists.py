# List of values - [] Square Brackets are used to store values in a list
# Mutable and Ordered

courses = ['History', 'Maths', 'Physics', 'CompSci']
courses_2 = ['Civics', 'Education']

print(courses)
print(len(courses)) # Number of items in a list

print(courses[0]) # Accessing the values in a list
print(courses[2]) # Accessing 2nd index from courses list

print(courses[-1]) # Access the last item of the list : [-1]

# print(courses[4]) # IndexError - List index out of range

# Slicing values from a list
print(courses[0:2]) # first index is inclusive, but the second index is not 
print(courses[:2]) # Same as above

print(courses[2:4])
print(courses[2:]) # Same as above

# List methods

# Adding a value in the end of the list - Append method
courses.append('Art')
# courses.append(courses_2) # Gonna append a list in the end not values
# print(courses)

# Adding a value in a specific position - Insert method
courses.insert(0, 'Economics')
print(courses)

# Adding a list in front via Insert Method
# courses.insert(0, courses_2) # List within a list
# print(courses)

# Adding a list values of a list to another list in the end - Extend Method
courses.extend(courses_2) # Appending list items of courses_2 to courses list
print(courses)

# Removing an item from list - remove()
courses.remove('Physics')
print(courses)

# Removing the last value from the list - pop()
popped = courses.pop() # This returns the variable it removes

# Useful if we want to use our list like a stack or a queue
print(popped) # Output: Education

print(courses)


# Sorting

# Reversing the list
courses.reverse()
print(courses)

# Sorting in Alphabetical Order
courses.sort()
print(courses)


nums = [5,3,2,4]
# Sorting in ascending order 
# Sorted function - doest sort the list in place - original will not change
sorted_nums = sorted(nums) # Use sorted() if you want to print right away

# Sorting in ascending order
# Sorting method - sort the list in place - original list will change
# nums.sort() # If we print this right away it will return None
# print(nums)

# Reversing a sorted list
# nums.sort(reverse=True)
# print(nums)

print(nums)
print(sorted_nums)

# Minimum value of a list - min() - Built in function
print(min(nums)) 
print(min(courses)) # Returns Art cuz A comes before M H C etc

# Maximum value of a list - max() - Built in function
print(max(nums))
print(max(courses)) # Returns Maths cuz M comes after A H C etc

# Sum of the entire list
print(sum(nums))
# print(sum(courses)) # TypeError - cant use sum for strings

print(courses)

# Printing index of a value
print(courses.index('CompSci')) # Output: 2
# print(courses.index('Comp')) # ValueError if it isnt in the list

# Finding if a value exists in a list or not - 
print('Art' in courses) # Output: True
print('DSA' in courses) # Output: False

print()

courses = ['History', 'Maths', 'Physics', 'CompSci']

# Loop

# Printing each Value in separate line
for course in courses: # Iterable variable is course - you can name it whatever you like
    print(course)

print()

# Enumerate function - printing value and index together
# Enumerate function Behind the scenes, enumerate(courses) generates a series of pairs (tuples) where the index is always the first item and the value is always the second item.If your list is ["Math", "Science"], enumerate() generates: (0, "Math")   (1, "Science")
for index, course in enumerate(courses):
    print(index, course)

print()

for index, course in enumerate(courses, start=1): 
    print(index, course)


# Let's say we want to turn our list of courses into a string of csv
course_str = ' - '.join(courses) # Making the list into one long string
print(course_str)
# NOTE : the join method only works on strings, on numeric values it will crash with a TypeError

# Splitting the values of the string back to a list
new_list = course_str.split(' - ') # Exact opposite of Join method
print(new_list)
