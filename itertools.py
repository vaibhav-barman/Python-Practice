# Itertools Modules
# It is a collection of tools that allows us to work with iterators in a fast and memory efficient way 
# This module contains number of commonly used iterators as well as functions for combining several iterators

import itertools
# 1 to 5 are forever going itertools and after that are the ones which terminates

letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ['Corey', 'Nicole']

# 1 - count function

# counter = itertools.count(start=5, step=5)
counter = itertools.count(start=5, step=-2.5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Don't run this on a for loop, it will be a infinite loop



# 2 - zip longest - pairs together even after one of the function argument is exhausted

data = [100,200,300,400]

# daily_data = list(zip(itertools.count(start=1), data)) # [(1, 100), (2, 200), (3, 300), (4, 400)]

# daily_data = list(zip(range(10), data)) # [(0, 100), (1, 200), (2, 300), (3, 400)]
# Data is exhausted before its full use, so we can use zip longest

daily_data = list(itertools.zip_longest(range(10), data))

print(daily_data) # [(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]



# 3) cycle - loops through our list and cycles it

counter = itertools.cycle([1,2,3])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


counter = itertools.cycle(('On', 'Off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# 4) repeat

counter = itertools.repeat(2, times=3)

print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter)) # StopIteration - because times=3


squares = map(pow, range(10), itertools.repeat(2))
print(list(squares)) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 5) star map - similar to map, instead of taking arguments from iterables, it takes arguments that are already paired together as tuples

squares = itertools.starmap(pow, [(0,2), (1,2), (2,2)])
print(list(squares))


# 6) Combinations and Permutations
# Combinations are basically all the different ways that you can group a certain number of items where the order does not matter
# Permutations are all the different ways that you can group a certain number of items where the order does matter

# Both of these dont repeat like (a,a)
# Combinations
result = itertools.combinations(letters, 2) # combinations of 2 values
for item in result:
    print(item)
# ('a', 'b') is the same as ('b', 'a') in combinations, so it only writes 1

print()

result = itertools.permutations(letters, 2)
for item in result:
    print(item)
# ('a', 'b') is not the same as ('b', 'a') in permutations, so it writes both of them

# If you want to repeat values like (a, a) then use the Product function

#7) Product
result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)

print()

# 8) Combinations_with_replacement - Combinations with repeated values

result = itertools.combinations_with_replacement(numbers, 4) 
for item in result:
    print(item)


#  9) Chain function - allows us to chain intervals so that it will go through all the items in the first interval and after that has been exhausted then it'll go through all the items in the second intervals and so on

combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)


# 10) islice - slicing on an iterator
result = itertools.islice(range(10), 1, 9, 2)

for item in result:
    print(item)
# Useful if we have an iterator that is too large on memory

print()

# Files are actually iterators themselves 
with open('test.log', 'r') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end="")


# 11) compress - used in data science style problems
selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)

for item in result:
    print(item) # c wasnt included because its corresponding is False

print()


# 12) filterfalse - returns the opposite of filter function

def lt_2(n):
    if n < 2:
        return True
    return False

# result = filter(lt_2, numbers) # 0, 1
result = itertools.filterfalse(lt_2, numbers) # 2, 3

for item in result:
    print(item)


print()

# 13) Drop While function
numbers = [1,2,3,2,1,0]

result = itertools.dropwhile(lt_2, numbers)

for item in result:
    print(item)


print()

# 14) Take While 
result = itertools.takewhile(lt_2, numbers)

for item in result:
    print(item)


print()

# 15) Accumulate function - addition by default
result = itertools.accumulate(numbers)

for item in result:
    print(item)

print()

import operator
result = itertools.accumulate(numbers, operator.mul) # changing default to multiplication

for item in result:
    print(item)


# 16) GroupBy Function
# GroupBy expects the initial iterable to be sorted so that it can group properly
# Group value based on certain keys and then it will return a stream of tuples, tuples consist of keys that the items were grouped on and the second value of the tuple is an iterator that contains all of the items that were grouped by that key

def get_state(person):
    return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

# Let's say we want to group people by the state that they're from
person_group = itertools.groupby(people, get_state)

# for key, group in person_group:
#     print(key)
#     for person in group:
#         print(person)
#     print()

for key, group in person_group:
    print(key, len(list(group)))


# Replicate iterator
# 17) tee function

copy1, copy2 = itertools.tee(person_group)
# Now copy1 and copy2 will be their own iterators
# You should not use the original iterator after you make the copies 
# ie in this case person_group
print(copy1)
print(copy2)