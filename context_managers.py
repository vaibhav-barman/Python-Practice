# f = open('sample.txt', 'w')
# f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
# f.close()

# Recommended way of working with files - Context Managers
# If we throw an error while working on the file, context manager will still close the file properly, that is why context managers are so useful
# It handles the teardown of the resources for us 
# How to know if its a context manager ? - with keyword

# with open('sample.txt', 'w') as f:
    # f.write('Lorem ipsum dolor sit amit, consectetur adipiscin elit.')

# Creating a context manager that opens the file for us and then automatically closes
# Method 1 - Class

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('sample.txt', 'w') as f:
    f.write('Testing') # Echo "Testing" in sample.txt

print(f.closed) # True - ie file is closed



# Method 2 - Function
from contextlib import contextmanager

#### Using contextlib ####
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode) # Open
        yield f
    finally:
        f.close() # Exit/Teardown

with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amit, consectetur adipiscin elit.')

print(f.closed) # True



#### CD Example ####
import os

# Method 1
# cwd = os.getcwd() # Get Current Working Directory
# os.chdir('Sample-Dir-One') # Changing Directory
# print(os.listdir()) # Listing Directory
# os.chdir(cwd) # Changing directory back to original

# cwd = os.getcwd()
# os.chdir('Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)


# Method 2
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield # So that we're ready to do whatever we want in that destination
    finally:
        os.chdir(cwd)

with change_dir('Sample_Dir_One'):
    print(os.listdir())

with change_dir('Sample_Dir_Two'):
    print(os.listdir())