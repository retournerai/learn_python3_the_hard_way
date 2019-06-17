# This is a script to better understand wow the operator: @ works
# The @ operator is called the 'At Decorator'

# Then you want to change something to that function, in that particular instance and you
# write a new function called 'decorate' to add something to the 'original_function' WITHOUT changing the original

# new function to decorate first function below
def decorate(func): # new function (parameter)
    print ("2. New Function") # Show message
    def nested_function(): # Nested function
        print("3. Nested function") # show message
        func() # call parameter included when calling decorate_original_function # in this case here you call 'original_function'
    return nested_function # end new_function and return outcome value (or function) from nested function

# original function   
@decorate # at decorator
def original_function(): # new function (parameter)
    print("1. Original Function.") # show message

# Then you use a variable to call the new function and use the original function as a parameter
# it will first 'decorate' and after it will call the original function
# Variable          = call: new_function (with 'first_function' as a parameter)
# original_function = decorate(original_function) 
            
original_function()

# Using @ decorator I must define the decorator first, before calling it above the original
# function, that is why the original function was moved down.
