# Loops

nums = [1,2,3,4,5]

# For loops

for num in nums: # num is an iterable variable
    # after each loop execution, num will increase its index from 0 to end
    if num == 2:
        print('Found!')
        continue # skips this iteration 
    if num == 4:
        print('Found 4!')
        break # Exits the loop
    print(num)

# For exiting a loop we use - break
# For ignoring a single value we use - continue

# Example using for loop in a for loop
for num in nums:
    for letter in 'abc':
        print(num, letter) # output 1a, 1b, 1c , 2a ...

print()

# Range Built in function
for i in range(10): # starts from 0 and dont include 10
    print(i)

print()

for i in range(1,10): # starts from 1 and dont include 10
    print(i)


# While Loops
x = 0
while True:
    x += 1
    print(x)
    if x == 6:
        break

# Use break for avoiding Infinite Loop