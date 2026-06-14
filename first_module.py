
# print(f"First Module's Name: {__name__}") # Output: First Module's Name: __main__

# What is happening here?

# When Python runs a program, it always creates special variables and assigns them initial values. The variable (__name__) is one of these special variables. When python runs the program directly, the value of the variable (__name__) is set to __main__

# def main():
#     print(f"First Module's Name: {__name__}")

# if __name__ == '__main__':
#     main()

# Running directly
# Output: First Module's Name: __main__

# 

if __name__ == '__main__':
    print("Run Directly!")
else:
    print("Run From Import")


# 

print("This will always run")

def main():
    print("First Module's Main Method")

if __name__ == '__main__':
    main()