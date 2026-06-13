nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums

# Method - 1
# my_list = [] # Empty List
# for n in nums:
#     my_list.append(n)
# print(my_list)

# Method 2 (List Comprehension)
my_list = [n for n in nums] 
print(my_list)


# I want 'n*n' for each 'n' in nums

# Method 1
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)


# Method 2 (List Comprehension)
# my_list = [n*n for n in nums]
# print(my_list)


# Method 3 
# Using a map + lambda

# Map - Runs everything in the list through a certain function
# map(function, iterable, ...)
# The map() function is a built-in Python tool used to apply a specific transformation function to every item inside an iterable (like a list, tuple, or dictionary) without using an explicit for loop.
# map() is a direct alternative to a for loop (for iterating over collections).
# A for loop executes its code immediately and actively pushes data through. map() is lazy. It prepares the blueprint for the transformation but does not actually execute the loop until you force it to (by looping over it or wrapping it in list()).
# The map() function has exactly one job: Data Transformation. It says: "Take this list, transform every single item using this formula, and give me the new stream of data."

# Lambda - Anonymous function
# lambda arguments: expression
# A lambda function is a small, anonymous (unnamed) function that you can define in a single line of code. They are designed for quick, one-off operations where writing a full standard function using the def keyword feels unnecessary.
# lambda is a direct alternative to def (for creating functions).
# A def function can hold any amount of Python code. A lambda function can only hold a single expression. You cannot write loops, use if/elif/else blocks (unless compressed into a one-line ternary operator), or assign new variables inside a lambda.
# The lambda keyword is designed for immediacy. Use it when you need a simple, one-line mathematical formula or string modification that you will only use once inside another tool (like map()).

my_list = list(map(lambda n: n*n, nums))
print(my_list)


# I want 'n' for each 'n' in nums if 'n' is even

# Method 1
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# Method 2   List comprehension - even
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# Method 3  Filter + Lambda

# filter() is a specialized alternative to a for loop combined with an if statement.
# The filter() function is a built-in Python tool used to extract specific items from an iterable (like a list, tuple, or set) based on a condition. It acts like a literal sieve or strainer: it checks every item against a testing function and keeps only the ones that pass the test.
# filter(function, iterable)
# Just like map(), filter() does not return a new list immediately. It returns a lazy iterator called a filter object.

my_list = list(filter(lambda n: n%2==0, nums))
print(my_list)


# I want a (letter, num) pair for each letter in 'abcd' and each number in '1234'
# Method 1
# my_list = []
# for letter in 'abcd':
#     for num in range(1,5):
#         my_list.append((letter, num))
# print(my_list)

# Method 2   List Comprehension
my_list = [(letter, num) for letter in 'abcd' for num in range(1,5)]
print(my_list)




# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']


# Method 1 - Zip() in for loop
# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero
# print(my_dict)

# Method 2 - Zip() inside dict()
# Zip Function - All of these match up one to one, name[0] to heroes[0] and so on
# If any Iterable (lists, tuples, strings, sets, or dictionaries) has extra then they simply wont be added to the master list
# hero_dict = dict(zip(names, heroes))
# print(hero_dict)

# Method 3 - Dictionary Comprehension
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

# If name not equal to Peter - ie - without Peter: Spiderman
# my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
# print(my_dict)


# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

# Method 1
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# Method 2   Set Comprehension
# my_set = set()
# my_set = {n for n in nums}
# print(my_set)

# Method 2   Set Comprehension without empty set 
# my_set = set(n for n in nums)
# print(my_set)

# Method 3   Map and Lambda without empty set
my_set = set(map(lambda n: n,nums))
print(my_set)


# Generator Expressions


# I want to yield 'n*n' for each 'n' in nums
# Method 1 
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n
# return (Traditional): A standard function computes a value, gives it back to you, and destroys its entire local state. It is a one-and-done operation.
# yield (Generator): When Python sees yield, it treats the function differently. Instead of exiting permanently, the function freezes, pauses execution, and remembers its current spot. It hands over the current value (n*n) and waits patiently until it is asked for the next one.

my_gen = gen_func(nums)
# What happens: Python reads this line but does not run the code inside your function yet. It will not execute the for n in nums loop at this point.
# The Result: It initializes a lazy generator object and saves it in the variable my_gen.

for i in my_gen:
    print(i)

# 3. Why Use Generators? (The Memory Superpower)
# Imagine your nums list didn't have 10 items, but 10 billion items.If you used a standard List Comprehension ([n*n for n in nums]), Python would try to calculate all 10 billion values simultaneously and force them into your system's RAM. Your computer would immediately freeze and crash with a MemoryError.
# Because your Generator yields only one item at a time on-demand, it requires almost zero memory. It calculates a value, prints it, throws it away, and moves to the next. It uses the exact same tiny amount of RAM for 10 items as it does for 10 billion items.

print()

# Method 2 - Generator Expression
my_gen = (n*n for n in nums) # This single line replaces your entire 'def gen_func' block!
# Python treats the parentheses ( ) around a comprehension as a special syntax trigger that creates a generator under the hood without needing the word yield.
for i in my_gen:
    print(i)

# NOTE: Once your for i in my_gen loop finishes running, the generator is exhausted. If you try to run a second for loop right below it using the same my_gen variable, it will print absolutely nothing. To reuse it, you must rebuild it.


# Proof: Verifying the Lazy Behavior

# Evidence 1: The Print Test
nums = [1, 2, 3]
# Shorthand expression
my_gen = (n * n for n in nums)
print(my_gen)
# Output: <generator object <genexpr> at 0x...>


# Evidence 2: The next() Test
nums = [1, 2, 3]
my_gen = (n * n for n in nums)
# It calculates ONLY the first item and stops
print(next(my_gen))  # Output: 1
# It resumes, calculates ONLY the second item, and stops
print(next(my_gen))  # Output: 4