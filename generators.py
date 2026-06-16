# Generators save memory - only the iterator is saved in the memory
# Generators save memory and also saves time, hence increasing performance 

# How to make this code to generator 2-6
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

# Method 1 - Generator
def square_numbers(nums):
    for i in nums:
        yield (i*i) # Yield keyword initiates a generator

# Now the code with generator is much more readable as compared to the previous code

# And even better option is by using list comprehension
# Method 2 - List comprehension
my_nums = [x*x for x in [1,2,3,4,5]]

# Method 3 - Generator Short Form just use () instead of [] in list comprehension
my_nums = (x*x for x in [1,2,3,4,5])

my_nums = square_numbers([1,2,3,4,5])
my_nums = [x*x for x in [1,2,3,4,5]]

print(my_nums) # [1, 4, 9, 16, 25]

# 1 is the first value and we yielded out 1*1 and then 2*2

# Printing result
# Method 1 - Using next(function)
print(next(my_nums)) # 1
print(next(my_nums)) # 4
print(next(my_nums)) # 9
print(next(my_nums)) # 26
print(next(my_nums)) # 25


print(next(my_nums)) # StopIteration Error - Generator has been exhausted

# Method 2 - For loop to print result - Recommended
for num in my_nums:
     print(num)


# Printing List - But Performance is losed here because now it holds in memory and time also increase - Not recommended
print(list(my_nums))