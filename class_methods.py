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
    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.04)

    # Recommended Method (Using class variable from line 3)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Employee.raise_amount also works instead of self.raise_amount 

    # Class Method

# Regular methods in a class automatically take the instance as the first argument and by convention we were calling it self
# So if a regular method takes in the instance as the first argument then we can change it as to it takes class as the first argument instead of self, for doing this we use classMethod.
# Turning a regular method into a class method, its as easy as adding a decorator to the top called @classmethod
# Altering our functionality, to receiving class as our first argument instead of the instance (self) now by convention with a regular method we call this instance variable self and there's a common convention for class variables to called "cls"
# So now within the set_raise_amt method we are working with the class instead of the instance
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

# Class method as an alternative constructor and usually these starts with "from", its a convention
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)

# Two employee instances 
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Working with the set_raise_amt() method
Employee.set_raise_amt(1.05)

# You can also use set_raise_amt() class method with an instance but its not really useful because it doesnt update a single instance instead it updates the whole class and instances
emp1.set_raise_amt(1.06)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)


# 2nd example
# We have someone who is using our employee class and they said that they have specific usecases where getting employee information in the form of a string that is separated by hyphens and I'm constantly needed to parse the string before I create new employees, so is there a way to create a string that pass in a string and create an employee from that

emp_str_1 = 'John-Doe-70000'
emp_str_1 = 'Steve-Smith-80000'
emp_str_1 = 'Jane-Doe-90000'

# You are gonna have to parse the string everytime you create a new employee, so let's just create an alternative constructor that allows them to pass in the string and we can create the employee for them 
# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)

# Now instead of parsing the string yourself, with this from_string method we can call
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)