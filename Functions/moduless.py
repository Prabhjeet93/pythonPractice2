"""
        What are modules in Python?
            Modules refer to a file containing Python statements and definitions.
            A file containing Python code, for example: example.py, is called a module, and its module name would be example.
            We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.
            We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

        Python Module Search Path
            While importing a module, Python looks at several places.
            Interpreter first looks for a built-in module.
            Then(if built-in module not found), Python looks into a list of directories defined in sys.path.

            The search is in this order.
                The current directory.
                PYTHONPATH (an environment variable with a list of directories).
                The installation-dependent default directory.

        The dir() built-in function:
            dir() function to find out names that are defined inside a module.
"""

# importing variables_scope.py module

import variables_scope
variables_scope.add()

# import statement
import math
print("The value of pi is", math.pi)  # -> The value of pi is 3.141592653589793

# Import with renaming
import math as m
print("The value of pi is", m.pi)
# print("The value of pi is", math.pi) # this will throw syntax error.

# Python from...import statement
from math import pi
print("The value of pi is", pi)

# multiple attributes imported.
from math import pi, e
print("The value of pi is", pi)   # -> The value of pi is 3.141592653589793
print("The value of e is", e)    # -> The value of e is 2.718281828459045


## Import all names
# we have imported all the definitions from the math module.
# This includes all names visible in our scope except those beginning with an underscore(private definitions).
from math import *
print("The value of pi is", pi)


##  Python Module Search Path
import sys
print(sys.path)


## Reloading a module
# import imp
# import my_module
# This code got executed
# import my_module
# imp.reload(my_module)
# This code got executed
# <module 'my_module' from '.\\my_module.py'>




# The dir() built-in function:
#             dir() function to find out names that are defined inside a module.
#             All other names that begin with an underscore are default Python attributes associated with the module (not user-defined).
print(dir(variables_scope))
# Output -> ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c', 'foo', 'outer', 'x']