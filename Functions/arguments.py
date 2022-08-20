"""

    Arguments:-
        variables passed in the function.
        e.g. -> def greet(name, msg):
        Functiona will throw error if less or more arguments passed in the function.

    default arguments:
        Any number of arguments in a function can have a default value.

        syntax -> def greet(name, msg="Good morning!"):

        But once we have a default argument, all the arguments to its right must also have default values.
        for example:- if we pass default value to name but not to the msg, it will throw error.

    keyword arguments:
        Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed.
         Following calls to the above function are all valid and produce the same result.
        # 2 keyword arguments
        greet(name = "Bruce",msg = "How do you do?")

        # 2 keyword arguments (out of order)
        greet(msg = "How do you do?",name = "Bruce")

        # 1 positional, 1 keyword argument
        greet("Bruce", msg = "How do you do?")

        Having a positional argument after keyword arguments will result in errors.
            greet(name="Bruce","How do you do?") -> SyntaxError: non-keyword arg after keyword arg

    Arbitrary Arguments:
        Sometimes, we do not know in advance the number of arguments that will be passed into a function.
        Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.

        SYNTAX - >
            def greet(*names):
            eg -> greet("Monica", "Luke", "Steve", "John")




"""

def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Canada", "Good morning!")

#greet("1", "Good morning!",2) #-> TypeError: greet() takes 2 positional arguments but 3 were given
#greet(1) #-> TypeError: greet() missing 1 required positional argument: 'msg'

# default argument

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")

# keyword arguments
# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce")

# 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")


# SyntaxError: non-keyword arg after keyword arg
# greet(name="Bruce","How do you do?")


# Arbitrary Arguments

def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")

# Hello Monica
# Hello Luke
# Hello Steve
# Hello John

def greet2(*names):
    """This function greets all
    the person in the names tuple."""
    print("Hello", names)


greet("Monica", "Luke", "Steve", "John")

# it will call function each time
# Hello Monica
# Hello Luke
# Hello Steve
# Hello John

