"""
     ********** Python Local and Global Variables***********

     1. Global Variables:
        A variable declared outside of the function or in global scope is known as a global variable.
        This means that a global variable can be accessed inside or outside of the function.

    2. Local Variables
        A variable declared inside the function's body or in the local scope is known as a local variable.

    3. Nonlocal Variables:
        Nonlocal variables are used in nested functions whose local scope is not defined.
        This means that the variable can be neither in the local nor the global scope.
        use nonlocal keywords to create nonlocal variables.

"""


x = "global"

def foo():
    print("x inside:", x)

foo()
print("x outside:", x)

# x inside: global
# x outside: global


"""if we try to change the value of global variable then it throws error
x = "global"
def foo():
    x = x * 2
    print(x)
foo()  -> UnboundLocalError: local variable 'x' referenced before assignment

We can use global keyword if we want to change the global variable value.
"""

c = 0  # global variable


def add():
    global c
    c = c + 2  # increment by 2
    print("Inside add():", c)


add()
print("In main:", c)

# Inside add(): 2
# In main: 2


#### Local variable
"""
# access local variable outside of the function

def foo():
    y = "local"


foo()
print(y)   #-> NameError: name 'y' is not defined
"""

def foo():
    y = "local"
    print(y)

foo() #-> local

# use local and global both in same code

x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
# global global
# local

################   Global variable and Local variable with same name
x = 5

def foo():
    x = 10  #-> if we want  to change the value of x in global so we have to use global keyword.
    print("local x:", x)


foo()
print("global x:", x)

# local x: 10
# global x: 5


## Create a nonlocal variable
x="outside"
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)
outer()
print(x)

# inner: nonlocal
# outer: nonlocal
# outside
# In the above code, there is a nested inner() function. We use nonlocal keywords to create a nonlocal variable.
# The inner() function is defined in the scope of another function outer().