# Iterators and Iterables

# Take a list for an example, it is an iterable but it is not an interator

# 1 - Iterables
# It is something that can be looped over 
# ex - list

nums = [1,2,3]

for num in nums:
    print(num)

# How can we tell if something can be looped over or not? OR Something is an iterable or not?
# If something is an iterable, it needs to have a special method called __iter__

# Dunder Iter Method
print(dir(nums)) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# So our list does have __iter__ method

# Now what makes something an iterator?
# An iterator is an object with a state so that it remembers where it is during iteration
# Iterators also know how to get their next value
# They get their next value with a dunder next method

# If you see print(dir(nums)), it doesnt have __next__() so it is not an iterator that means our list doesnt have a state and it doesnt know how to get its next value
print(next(nums)) # TypeError: 'list' object is not an iterator

i_nums = nums.__iter__()
# OR
i_nums = iter(nums)

print(i_nums) # <list_iterator object at 0x000001AD97CA7A90>

print(dir(i_nums)) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']

# Now we can see we have __iter__() and __next__() for i_nums
# Iterators are also Iterables

print(next(i_nums)) # Output: 1 - An iterator is an object with a state so that it remembers where it is during iteration, so if we run next on this again it will output 2 and then 3
print(next(i_nums))
print(next(i_nums))
print(next(i_nums)) # StopIteration Exception - Iterator has been exhausted and has no more values

# For Loop background working
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


# Another characterstic of iterators is that they can only go forward, there is no backwards resetting it or making a copy of it, you can only (next) it


# So why does all of this matter? - What are its practical uses?
# We can add these methods to our own classes and make them iterable as well

# Let's create a class that basically behaves like the built in range function

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
# Now we want to make this class iterable  
    def __iter__(self):
        return self
    
# Now we want to make this class iterator
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
nums = MyRange(1,10)

# for num in nums:
#     print(num)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

print()

# Generators are iterators as well
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1,10)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

for num in nums:
    print(num)

# NOTE: Iterators dont need to end, they can simply go on forever
# As long as there is a next value, it will work it