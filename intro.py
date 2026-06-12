# Importing modules
import my_module
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index_1 = my_module.find_index(courses, 'Math')
index_3 = my_module.find_index(courses, 'CompSci')
print(index_1)
print(index_3)

# Importing module as m (short name)
import my_module as mm

index_2 = mm.find_index(courses, 'Physics')
print(index_2)

# Importing a function from a module - best way
from my_module import find_index, test

index_0 = find_index(courses, 'History')
print(index_0)
print(test)

# Importing everything - not used often because then we wouldnt know if we created the function or is it imported 
# from my_module import * 


# print(sys.path) outputs a list of directory paths where the Python interpreter searches for modules and packages during an import statement.
print(sys.path)

# What if the module is not in the listed directories?????
# Couple of approaches we can take in this case
# 1) manually add the path to the sys.path list - C:\path
# sys.path.append(r'C:\path')
# print(sys.path)
# this isnt the best looking approach


# 2) Change into the next place where sys.path looks - python path environment variable
# Click the windows button -> search for 'edit the system environment variable' -> click on 'environment variables' -> click on 'New' -> write PYTHONPATH in Variable Name and location (C:\path) in Variable Value
# Checking it - Open CMD - write python -> import my_module -> Imported my_module... -> import sys -> sys.path -> 
# [
#   '', 
#   'C:\\path', 
#   'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13...\\python313.zip', 
#   'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13...\\DLLs', 
#   'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13...\\Lib', 
#   'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13...', 
#   'C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13...\\site-packages', 
#   'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13...\\Lib\\site-packages'
# ]
# Look at the [1] index




# Using Python Standard Libraries

# 1 - random library
import random

courses = ['History', 'Math', 'Physics', 'CompSci']
random_courses = random.choice(courses)
print(random_courses)

# 2 - math Module
import math

rads = math.radians(90) # pi/2 or 1.57079
print(rads) 
print(math.sin(rads))

# 3 - datetime and calendar modules
import datetime
import calendar

# Finding out Date Today
today = datetime.date.today()
print(today)

# Checking leap year or not
print(calendar.isleap(2021))
print(calendar.isleap(2020))

# 4 - os library - gives access to underlying operating system
import os

# Printing Current working directory (cwd)
print(os.getcwd())


# How to view location of these modules
# We use Dunder file attributes

# Location of os library
print(os.__file__)


# Location where all of these modules are -
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib

# Antigravity Module is a joke in python community on how easy it is to learn programming in python 
# import antigravity