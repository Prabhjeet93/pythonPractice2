"""
    What is the global keyword
        In Python, global keyword allows you to modify the variable outside of the current scope.
        It is used to create a global variable and make changes to the variable in a local context.

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

"""   
        Global Variables Across Python Modules:

            for example: 
            Share a global Variable Across Python Modules
            1. Create a config.py file, to store global variables
                a = 0
                b = "empty"
            2. Create a update.py file, to change global variables

                import config

                config.a = 10
                config.b = "alphabet"
            3. Create a main.py file, to test changes in value

                import config
                import update

                print(config.a)
                print(config.b)
            4. When we run the main.py file, the output will be

            10
            alphabet
"""

"""
    Global in Nested Functions
        In the below program, we declared a global variable inside the nested function bar(). 
        Inside foo() function, x has no effect of the global keyword.
        Before and after calling bar(), the variable x takes the value of local variable i.e x = 20. 
        Outside of the foo() function, the variable x will take value defined in the bar() function i.e x = 25. 
        This is because we have used global keyword in x to create global variable inside the bar() function (local scope).
        If we make any changes inside the bar() function, the changes appear outside the local scope, i.e. foo().   
"""


def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main: ", x)
