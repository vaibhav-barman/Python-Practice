my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9 -- index
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 -- index

print(my_list[5]) # 5th index of list
print(my_list[-1]) # last number of list
print(my_list[-10]) # first number of list 

# To extract a range of values from the list - we use SLICING
# List[start:end:step] - end is excluded 
# Default List - List[::1]

print(my_list[0:6]) # printing 0 to 5
print(my_list[3:8]) # 3 through 7
print(my_list[-7:-2]) # 3 through 7 (method 2)
print(my_list) # print full list 
print(my_list[:]) # print full list 
print(my_list[1:]) # print 1 to end
print(my_list[:8]) # print start to 7

print(my_list[1::2]) # printing odd numbers
print(my_list[::2]) # printing even numbers
print(my_list[::-1]) # reversing the list
print(my_list[2:-1:2]) # printing 2,4,6,8
print(my_list[9::-2]) # reverse printing odd numbers 
print(my_list[8::-2]) # reverse printing even numbers 
print(my_list[::1]) # default list
print(my_list[-2:1:-1]) # 8 to 2 reverse


# Slicing a String
sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])

# Get the TLD
print(sample_url[-4:])

# Print the URL without the http://
print(sample_url[7:])

# Print the URL without the http:// or the TLD
print(sample_url[7:-4])