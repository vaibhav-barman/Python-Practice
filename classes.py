# Python Object-Oriented Programming

# Why should we even use classes?
# They allow us to logically group our data and functions in a way that's easy to reuse and also easy to build upon if need be.
# NOTE: When i say data and functions that are associated with a specific class, we call those attributes and methods
# Method - Function that is associated with a class


# Creating a Class
class Employee:
    pass

# Difference between a class and an instance of a class
# So our class is basically a blueprint for creating instances and each unique employee that we create using our employee class will be an instance of that class

# These below statements are called instances of Employee class
emp1 = Employee()
emp2 = Employee()
# Each of these are going to be their own unique instances of the employee class

print(emp1) # Output: <__main__.Employee object at 0x0000026617786E40>
print(emp2) # Output: <__main__.Employee object at 0x0000026617A14CD0>

# Instance variables contains data that is unique to each instance

emp1.first = 'Corey'
emp1.last = 'Schafer'
emp1.email = 'corey.schafer@company.com'
emp1.pay = 50000

emp2.first = 'Test'
emp2.last = 'User'
emp2.email = 'test.user@company.com'
emp2.pay = 60000

print(emp1.email)
print(emp2.email)

# We dont get much benefit of using classes this way 25-36 lines

class Employee:
    def __init__(self, first, last, pay):
        self.first = first # can also write self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self): # Dont forget this self argument
        return f'{self.first} {self.last}'

# Whenever i say that self is an instance, what i mean by that is that we set self.first = first here, its going to be the same as above's (emp.first = 'Corey') except now instead of doing it manually it will be done automatically when we create employee objects
# We can now specify the values that we passed in __init__ method
# __init__ method takes the instance which we called self and the first name and last name and pay as arguments

# But when we create Employee down here the instance is passed automatically so we can leave self off, we only need to provide the names and the pay so we could create these by passing in "corey", 'schafer' etc

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)
# When we run these Employee the __init__ method will run automatically
# So emp1 will be passed as self and then it will set all of these attributes, emp1.first = 'Corey'

print(emp1)
print(emp2)

print(emp1.email)
print(emp2.email)

# Printing the full name of the emp1 and emp2
# Method 1
print(f'{emp1.first} {emp1.last}') 
print(f'{emp2.first} {emp2.last}')

# Instead let's create a method within our class that allows us to put this functionality in one place, so within our class here
# Lines 48-49

# We need parenthese here because it is a method instead of an attribute
# NOTE: One common mistake people does in creating method is forgetting the self argument
# We can also run these methods using the class name itself ie Employee which makes it a bit more obvious of what's going on in the background

print(emp1.fullname()) # dont need to pass an instance
print(Employee.fullname(emp1)) # need to pass in instance

print(emp2.fullname())
print(Employee.fullname(emp2))

