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

    # Recommended Method (Using class variable from line 3)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Employee.raise_amount also works instead of self.raise_amount 
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

# Class method as an alternative constructor and usually these starts with "from", its a convention
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)
    
# Static method dont pass anything automatically they dont pass the instance or the class so really they behave just like regular functions except we include them in our classes because they have some logical connection with the class
# Let's say we want a simple function that takes in data and return whether or not that was a workday, it doesnt actually depend on any instance and class variable, so we use static method

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
# The method should be a static method is if you dont access the instance or the class anywhere within the function

# Two employee instances 
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)

import datetime # Importing datetime module

# Creating a date
my_date = datetime.date(2016, 7, 10) # Sunday
my_date = datetime.date(2016, 7, 11) # Monday

print(Employee.is_workday(my_date))