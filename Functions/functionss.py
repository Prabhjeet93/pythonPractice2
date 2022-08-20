"""

    What is a function in Python?
        In Python, a function is a group of related statements that performs a specific task.
        Functions help break our program into smaller and modular chunks.
        As our program grows larger and larger, functions make it more organized and manageable.
        Furthermore, it avoids repetition and makes the code reusable.

        syntax:
        def function_name(parameters):
	        docstring
	        statement(s)

	How to call a function in python?
	    function_name(parameters)
	    Once we have defined a function, we can call it from another function, program, or even the Python prompt

	The return statement
	    The return statement is used to exit a function and go back to the place from where it was called.

	    syntax : return [expression_list]

	     If there is no expression in the statement or the return statement itself is not present inside a function,
	        then the function will return the None object.

	Scope of a variable
	    The lifetime of a variable is the period throughout which the variable exists in the memory.
	    The lifetime of variables inside a function is as long as the function executes.
        They are destroyed once we return from the function. Hence, a function does not remember the value of a variable from its previous calls.
        On the other hand, variables outside of the function are visible from inside. They have a global scope.
        We can read these values from inside the function but cannot change (write) them.
        In order to modify the value of variables outside the function, they must be declared as global variables using the keyword global.

    Types of Functions
        1. Built-in functions - Functions that are built into Python.
        2. User-defined functions - Functions defined by the users themselves.

"""
#greet("toronto")  # Error: name 'greet' is not defined

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Canada')  # Hello, Canada. Good morning!

# print the docstring iwth functiona name and __doc__
print(greet.__doc__)

# This function greets to
#     the person passed in as
#     a parameter


print(greet('toronto'))
# Output:
# Hello, toronto. Good morning!
# None -> If there is no expression in the statement or the return statement itself is not present inside a function, then the function will return the None object.


#Example of return
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >=0:
        return num
    else:
        return -num

print(absolute_value(-7)) #-> 7
print(absolute_value(3))  #-> 3


# Scope of a variable
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

# Value inside function: 10
# Value outside function: 20
# the value of x is 20 initially.
# Even though the function my_func() changed the value of x to 10, it did not affect the value outside the function.
