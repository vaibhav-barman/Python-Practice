# Integer is a whole number, float is a decimal
num = 3.14
print(type(num))

# Floor division
print(501//2) # Removes decimal

# Order of operations
# Parenthesis, exponentiation, unary sign/bitwise NOT, multiplication/division, addition/subtraction, bitwise shifts << >>, bitwise and xor or & ^ |, comparision & identity == != > < is in, logical NOT not, logical AND and, logical OR or


num = 1
# num = num + 1
# num += 1

num *= 10
print(num)

# Absolute Value
print(abs(-3)) # Ouput: 3
print(abs(5)) # Output: 5
print(abs(-4.75)) # Output: 4.75

# Round Value
print(round(3.75))
print(round(3.5)) # odd .50 rounds +1 - round up is called Ceil
print(round(4.5)) # even .50 round -1 - round down is called Floor

print(round(3.75, 1)) # Rounds to 1 digit after decimal

num_1 = '100'
num_2 = '200'

print(num_1 + num_2) # String concatenation
print(int(num_1) + int(num_2)) # Casting