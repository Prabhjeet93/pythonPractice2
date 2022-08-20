"""
    What is recursion?
        Recursion is the process of defining something in terms of itself.
        In Python, we know that a function can call other functions. It is even possible for the function to call itself.
        These types of construct are termed as recursive functions.
        e.g -> factorial code

        base condition:
            it will help in ending the functiona calls.
            if it is not defined then recursive function calls go into infinite loop, but in python its count is defined to 1000.
            e.g. - [Previous line repeated 996 more times]
                    RecursionError: maximum recursion depth exceeded

    Advantages of Recursion
        Recursive functions make the code look clean and elegant.
        A complex task can be broken down into simpler sub-problems using recursion.
        Sequence generation is easier with recursion than using some nested iteration.

    Disadvantages of Recursion
        Sometimes the logic behind recursion is hard to follow through.
        Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
        Recursive functions are hard to debug.
"""

def factorial(num):
    """"This is a recursive function
    to find the factorial of an integer"""
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

p = 6
fact = factorial(p)
print("factorial is",fact)  # factorial is 720


# recursion error if base cndtion is not defined.
def recursor():
    recursor()
recursor()

# recursor()
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


