# File Objects

# Method 1 - Not recommened
# To open a file - default mode is reading, you can change it to wrting , appending or reading and writing
f = open('test.txt', 'r') # 2nd argument 'r' for reading
# 'w' for writing , 'a' for appending, 'r+ for reading and writing'

# Print the name of the file
print(f.name)

# Print the current mode of file
print(f.mode) # Output: r

# Closing the File
f.close()

# NOTE
# If you dont close then you can end up with leaks that cause you to run over the maximum allowed file descriptors on your system and your applications could throw an error
# So its always important to close the file that you open


# Method 2 - Context Managers - Best Practice
# Benefit of Context Managers - They allow us to work with files from within this block of with and after we exit that block of code then it'll automatically close the file for us - we dont have to write file_name.close()
with open('test.txt', 'r') as f:# variable name: f
    pass

print(f.mode) # Output: r - you can check the mode even if its closed
print(f.closed) # Output: True
print(f.read()) # Output: ValueError : I/O operation on closed file

with open('test.txt', 'r') as f:
    f_contents = f.read() # Grabs all of the lines of the file
    print(f_contents) 
    # This works well on small files

    # But what if we have extremely large files that we want to read but we dont want to load all of the contents of that file into memory ?
    f_contents = f.readlines() # Grabs all of the lines of the file in a list
    f_contents = f.readline() # Grabs the first line of the file
    print(f_contents, end='')
    f_contents = f.readline() # Grabs the second line of the file
    print(f_contents, end='')
    # Methods - read(), readlines(), readline()



# But what if we have extremely large files that we want to read but we dont want to load all of the contents of that file into memory ?
# we use this below
# Code
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Why for loop? Because this is efficient because it doesnt print all at once, its going to get one line at a time from the file



# How to specify the amount of data that we want?
# Code 59-64
with open('test.txt', 'r') as f:
    f_contents = f.read(100) # Read 100 characters in the file test.txt
    print(f_contents, end='')

    f_contents = f.read(100) # Reads 100 next characters after the before 100 characters
    print(f_contents, end='')


# Better way - to specify the amount of data
# Code 69-74
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read) # Reads Size_to_read variable for characters
    while len(f_contents)>0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)


# Code 78 - 89
# See the current postion - f.tell()
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0) # 0 - Starts from the beginning again 

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell()) # Reads current position: 10


# Writing a file

# test2.txt doesnt exist now but the below code will create it
# NOTE: if the file exists already then it will overwrite it 

# # Create a file 'test2.txt'
with open('test2.txt', 'w') as f:
    pass


# Writing 'TestTest' in 'test2.txt' and creating a file
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.write('Test')


# Writing 'Test' and overwriting 'T' in 'Test' with 'R' in 'test2.txt' and creating a file
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')


# Using Read and Write together - duplicating 'test.txt'
with open('test.txt', 'r') as rf: # rf - read file
    with open('test_copy.txt', 'w') as wf: # wf - write file
        for line in rf:
            wf.write(line)
# Output: test_copy.txt made 


# Duplicating 'bronx.png' image - rb and wb (readBinary and writeBinary)
# Method 1 - iterating over the line (not recommended for binary)
with open('bronx.png', 'rb') as rf: 
    with open('bronx_copy.png', 'wb') as wf: 
        for line in rf:
            wf.write(line)
# Output: bronx_copy.png made 

# Method 2 - Fixed-size chunks (Recommended for binary) - More efficient
with open('bronx.png', 'rb') as rf: 
    with open('bronx_copy.png', 'wb') as wf:
        chunk_size = 4096 # reads exactly 4096 bytes (4 KB) at a time.
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
# Output: bronx_copy.png made 


# Suppose the file size is 10,000 bytes.
# First read  → 4096 bytes
# Second read → 4096 bytes
# Third read  → 1808 bytes
# Fourth read → b'' (empty, EOF)

# The loop stops when:
# len(rf_chunk) == 0