class Employee:
    raise_amt = 1.04

    # This __init__ is called as Dunder init - Dunder means surrounded by double underscore __init__
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # More special methods other than __init__
    # 1) Dunder __repr__ - Unambiguous representation of an object and should be used for debugging and logging and things like that, it's really meant to be seen by other developers
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    # 2) Dunder __str__ - Readable representation of an object and is meant to be used as a display to the end user
    def __str__(self):
        return f'{self.fullname()} - {self.email}'
    
    # 3) Dunder __add__
    def __add__(self, other):
        return self.pay + other.pay
    
    # 4) Dunder __len__
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Vaibhav', 'Barman', 60000)

print(len('test')) # Output: 4
# This above statement uses dunder len method BTS
print('test'.__len__())

print(emp_1 + emp_2) # Combined salaries using dunder add
print(len(emp_1)) # Output: 13
print(len(emp_2)) # Output: 14

# print(emp_1.fullname())
# print(emp_2.fullname())

# Changing the object at 1234567890 to Readable Output
# print(emp_1) # Output: Employee('Corey', 'Schafer', '50000')
# print(emp_2) # Output: Employee('Vaibhav', 'Barman', '60000')

print(repr(emp_2))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_2.__repr__())
print(emp_2.__str__())

# Example
print(1+2) # This uses special method dunder add - __add__

# 3) Dunder add (__add__)
print(int.__add__(1,2))
print(str.__add__('a', 'b'))


# Practical example
# Search on datetime module (__add__)
# Search on datetime module (__repr__)
# Search on datetime module (__str__)


# Return NotImplemented - They don't want to throw an error because the other object might know how to handle that operation, if none of the object knows how to handle it then it'll eventually throw an error