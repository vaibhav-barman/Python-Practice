li = [9,1,8,2,7,3,6,4,5]

# Sort Method - Works specifically on Lists

# Sorting in Ascending Order
# Sorted Function - Doesn't modifies li directly - Returns a new sorted function
s_li = sorted(li)
print('Sorted Variable:\t', s_li)

li.sort() # Modifies li directly - changes in place
print('Original Variable:\t', li)

# Descending Order Sorting
rs_li = sorted(li, reverse=True)
print('Reverse Sorted:\t', rs_li)

# Can also revese sort using sort method
# li.sort(reverse=True)


# Sorting a Tuple
tup = (9,1,8,2,7,3,6,4,5)

s_tup = sorted(tup)
print('Sorted Tuple: \t', s_tup)


# Sorting a Dictionary
di = {'name': 'Vaibhav', 'job': 'SDE-3', 'age': None, 'os': 'Windows'}
s_di = sorted(di)

print('Sorted Dictionary:\t', s_di) # Sorting Keys only


# What if i had a list of integers here and want to sort them based on their absolute values
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print('Sorted List: \t',s_li) # Negative are less than Positive Like you'd expect

as_li = sorted(li, key=abs)
print('Abs Sorted: \t', as_li) # Sorting based on their absolute values


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, ${self.salary})'

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

# Writing a Custom Function in order to sort these
# def e_sort(emp):
#     return emp.salary

# Method 1
# s_employees = sorted(employees, key=e_sort, reverse=True)

# Method 2   Lambda Function - so no need of def e_sort()
# s_employees = sorted(employees, key=lambda e: e.age, reverse=True)

# Method 3   Using attrgetter from operator module
from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('salary'))

print(s_employees) # Descending Sorting based on their Salary