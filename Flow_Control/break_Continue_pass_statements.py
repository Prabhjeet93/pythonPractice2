"""

    What is the use of break and continue in Python?
        In Python, break and continue statements can alter the flow of a normal loop.
        Loops iterate over a block of code until the test expression is false,
            but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.
        The break and continue statements are used in these cases.

    1. break statement
        The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
        If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.

    2. continue statement
        The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
        Loop does not terminate but continues on with the next iteration.
    3. pass statement
        The pass statement is a null statement.
        The difference between a comment and a pass statement in Python is that while the interpreter ignores a comment entirely, pass is not ignored.
        However, nothing happens when the pass is executed. It results in no operation (NOP).

        Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future.
        They cannot have an empty body. The interpreter would give an error.
        So, we use the pass statement to construct a body that does nothing.
"""

# break statement
for i in "canada":
    if i=='d':
        break
    print(i)
print("End of the break statement loop")

# c
# a
# n
# a
# End of the break statement loop

# continue statement
for i in "canada":
    if i=='a':
        continue
    print(i)
print("End of the continue statement loop")

# c
# n
# d
# End of the continue statement loop


#pass statement
'''pass is just a placeholder for
functionality to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

def function(args):
    pass

class Example:
    pass



