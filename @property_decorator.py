class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # @property decorator - getter
    # We're defining our email in our class like it's a method but we're able to access it like its an attribute
    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'
    
    # @property decorator - getter
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    # @property.setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    # @property.deleter
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

emp_1.fullname = 'Corey Schafer' # AttributeError - use a setter to solve this 

print(emp_1.first) # first attribute
print(emp_1.email)
print(emp_1.fullname) # fullname method

# whenever we set emp_1.fullname = 'Corey Schafer' , it came into our @fullname.setter here and it parsed the names from that value that we set and then it set our first name and last name 

# Calling the @property.deleter
del emp_1.fullname