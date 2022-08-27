"""

    Python Custom Exceptions:
        Python has numerous built-in exceptions that force your program to output an error when something in the program goes wrong.
        However, sometimes you may need to create your own custom exceptions that serve your purpose.

        Creating Custom Exceptions:
            Users can define custom exceptions by creating a new class.
            This exception class has to be derived, either directly or indirectly, from the built-in Exception class.
            Most of the built-in exceptions are also derived from this class.

        Customizing Exception Classes:


"""

## Creating Custom Exceptions:
#  we have created a user-defined exception called CustomError which inherits from the Exception class.
#  This new exception, like other exceptions, can be raised using the raise statement with an optional error message.

class customError(Exception):
    pass

#raise customError   # __main__.customError
#raise customError("This is a custom error")   # __main__.customError: This is a custom error

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

##### Customizing Exception Classes:
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)  # # __main__.SalaryNotInRangeError: Salary is not in (5000, 15000) range
else:
    print("Salary is in range")


# Another example
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)    # __main__.SalaryNotInRangeError: 17000 -> Salary is not in (5000, 15000) range