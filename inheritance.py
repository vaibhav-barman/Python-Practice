class Employee:

    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# Subclass - Inheritance
class Developer(Employee): # Inheriting Employee class's functionality

    raise_amt = 1.10 # Changing the raise_amt to 10%
    # NOTE: We can make these changes in the subclasses without breaking anything in the parent class
    # pass # walk up the chain of inheritance ie Employee in this case

    def __init__(self, first, last, pay, prog_lang):
        # Method 1 - Super() - More maintainable and necessary when you start using multiple inheritance
        super().__init__(first, last, pay)
        # Method 2
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
            # Never pass mutuable objects as default arguments like lists, dictionaries, why? in another video
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

# Instantiating Developers 
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Vaibhav', 'Barman', 60000, 'JavaScript')

# print(help(Developer))
# Output:  Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# print(dev_2.pay)
# dev_1.apply_raise() # raise_amt = 1.04 - when Instantiating using Employee class
# dev_2.apply_raise() # raise_amt = 1.10
# print(dev_1.pay)
# print(dev_2.pay)

print(dev_1.prog_lang)
print(dev_2.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


# Python Builtin functions
# 1) isinstance function
print(isinstance(mgr_1, Manager)) # Checks if mgr_1 is an instance of Manager - Output: True
print(isinstance(mgr_1, Developer)) # Output: False


# 2) issubclass function
print(issubclass(Developer, Employee)) # Checks if Developer is a subclass of Employee - Output: True
print(issubclass(Manager, Employee)) # Output: True
print(issubclass(Manager, Developer)) # Output: False

# Practical Example 
# Check exceptions.py module