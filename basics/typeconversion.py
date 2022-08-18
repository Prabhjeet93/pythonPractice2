
"""
    Type Conversion:
        The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion.
        Python has two types of type conversion.

            1. Implicit Type Conversion -: Python automatically converts one data type to another data type.
                                            This process doesn't need any user involvement.
                                            Convert from lower data type to higher.
                                            Python avoids the loss of data in Implicit Type Conversion.

            2. Explicit Type Conversion or Type casting -:
                                           Users convert the data type of an object to required data type.
                                           We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
                                           This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.
                                           Syntax :
                                                    <required_datatype>(expression)
                                           Typecasting can be done by assigning the required data type function to the expression.
                                           In Type Casting, loss of data may occur as we enforce the object to a specific data type.
"""


### 1. Implicit Type Conversion -: Python automatically converts one data type to another data type. This process doesn't need any user involvement.

#Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))   #datatype of num_int: <class 'int'>
print("datatype of num_flo:",type(num_flo))   #datatype of num_flo: <class 'float'>

print("Value of num_new:",num_new)    #Value of num_new: 124.23
print("datatype of num_new:",type(num_new))  #datatype of num_new: <class 'float'>

#Addition of string(higher) data type and integer(lower) datatype

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))  # Data type of num_int: <class 'int'>
print("Data type of num_str:",type(num_str))   #Data type of num_str: <class 'str'>

print(num_int+num_str)    # TypeError: unsupported operand type(s) for +: 'int' and 'str' - For this we use explicit type conversion.

### 2. Explicit Type Conversion -: users convert the data type of an object to required data type.

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)    # converted num_str from string(higher) to integer(lower) type using int() function to perform the addition.
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

#### output -
## datatype of num_int: <class 'int'>
# datatype of num_flo: <class 'float'>
# Value of num_new: 124.23
# datatype of num_new: <class 'float'>
# Data type of num_int: <class 'int'>
# Data type of num_str: <class 'str'>