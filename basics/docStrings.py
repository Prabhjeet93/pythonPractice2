"""
A docstring is short for documentation string.

Python docstrings (documentation strings) are the string literals that appear right after the definition of a function, method, class, or module.

Triple quotes are used while writing docstrings. For example:

The docstrings are associated with the object as their __doc__ attribute.

"""


def double(num):
    """Function to double the value"""    # Doc string
    return 2*num

# access doc string

def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)

# Output -> Function to double the value