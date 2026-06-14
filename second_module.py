import first_module
# No output

# Running main method() in second module from first module
first_module.main()

print(f"Second Module's Name: {__name__}") 
# Output: Second Module's Name: __main__