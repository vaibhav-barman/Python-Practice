class Employee:

    # Class Variable
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Adding 1 to num_of_employees
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"
    
    # Hard Coded Method - Not recommended, that's why we use class variables
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

    # Recommended Method (Using class variable from line 3)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Employee.raise_amount also works instead of self.raise_amount 

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

# Instance variables can be unique for each instance like name, email and pay
# Class variables should be the same for each class , example, fixed annual raises

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# These below 2 statements do not exist, that's why we use class variables

# emp1.raise_amount
# Employee.raise_amount

# Printing Raise_amount 
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Print namespace of emp1
print(emp1.__dict__)

# Print namespace of Employee Class
print(Employee.__dict__)

# Changing the class variable using class
# Employee.raise_amount = 1.05

# Changing the class variable using instace of a class
emp1.raise_amount = 1.05

# Printing Raise_amount 
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Print namespace of emp1
print(emp1.__dict__) # raise_amount is added now after line 53 - emp1.raise_amount = 1.05

# Printing the total number of employees
print(Employee.num_of_employees)