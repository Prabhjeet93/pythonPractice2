"""
    Python Exception Handling Using try, except and finally statement

            The critical operation which can raise an exception is placed inside the try clause.
            The code that handles the exceptions is written in the except clause.

            We print the name of the exception using the exc_info() function inside sys

    Catching Specific Exceptions in Python:
            This is not a good programming practice as it will catch all exceptions and handle every case in the same way.
            We can specify which exceptions an except clause should catch.

    A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs.
    We can use a tuple of values to specify multiple exceptions in an except clause.

    Raising Exceptions in Python:
            Exceptions are raised when errors occur at runtime. We can also manually raise exceptions using the raise keyword.
            We can optionally pass values to the exception to clarify why that exception was raised.

    Python try with else clause:
            In some situations, e might want to run a certain block of code if the code block inside try ran without any errors.
            For these cases, you can use the optional else keyword with the try statement.

            Note: Exceptions in the else clause are not handled by the preceding except clauses.

    try...finally:
            The try statement in Python can have an optional finally clause.
            This clause is executed no matter what, and is generally used to release external resources.

            For example, we may be connected to a remote data center through the network or working with a file or a Graphical User Interface (GUI).
            In all these circumstances, we must clean up the resource before the program comes to a halt whether it successfully ran or not.
            These actions (closing a file, GUI or disconnecting from network) are performed in the finally clause to guarantee the execution.






"""

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# The entry is a
# Oops! <class 'ValueError'> occurred.
# Next entry.
#
# The entry is 0
# Oops! <class 'ZeroDivisionError'> occurred.
# Next entry.
#
# The entry is 2
# The reciprocal of 2 is 0.5


##########################################
## Since every exception in Python inherits from the base Exception class, we can also perform the above task in the following way:
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)


# Multiple except are allowed with 1 try statement.
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

# raise KeyboardInterrupt  # KeyboardInterrupt
# raise MemoryError("This is an argument")   # MemoryError: This is an argument

try:
    a=-1
    if a<=0:
        raise ValueError("This is a negative no.")
except ValueError as ve:
    print(ve)

# This is a negative no.



#### Python try with else clause

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

# input - 3 -> Not an even number!
# input 4 -> 0.25
# input 0 -> ZeroDivisionError: division by zer0

######################################33

## Try and finally
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()