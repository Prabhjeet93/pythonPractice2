""""
Data types
    Every value in Python has a datatype. Since everything is an object in Python programming,
    data types are actually classes and variables are instance (object) of these classes.

    1.  Numbers - Integers, floating point numbers and complex numbers
    2. [List] - List is an ordered sequence of items. All the items in a list do not need to be of the same type.
              - Lists are mutable, meaning, the value of elements of a list can be altered.
    3. (Tuple) - Tuple is an ordered sequence of items same as a list.
               - The only difference is that tuples are immutable. Tuples once created cannot be modified.
               - Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.
    4. "Strings" - String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings.
                 - Multi-line strings can be denoted using triple quotes, ''' or """ """
                 - Strings are immutable.
    5. {Set}    - Set is an unordered collection of unique items. Items in a set are not ordered.
                - We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.
    
    6. {Dictionary} - Key:value pair . Dictionary is an unordered collection of key-value pairs.
                    - It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data.
                    - We must know the key to retrieve the value.   
                    -  Key and value can be of any type.
                           
                           
    7. Conversion between data types - 
                We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.
               e.g.- float(5)-> 5.0 , int(10.6) -> 10

"""

#*************************************************************************************************88
## 1. Python Numbers - Integers, floating point numbers and complex numbers
#Integers can be of any length, it is only limited by the memory available.

#A floating-point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points.
# 1 is an integer, 1.0 is a floating-point number.

#Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part. Here are some examples.

"""  
    type() function to know which class a variable or a value belongs to. 
    Similarly, the isinstance() function is used to check if an object belongs to a particular class.
"""

a = 5
print(a, "is of type", type(a))   # 5 is of type <class 'int'>

a = 2.0
print(a, "is of type", type(a))  # 2.0 is of type <class 'float'>

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))  #(1+2j) is complex number? True


#********************************************************************************************************************

## 2. [List] - List is an ordered sequence of items. All the items in a list do not need to be of the same type.
### declared with square brackets -> []

a = [1, 2.2, 'python']

#We can use the slicing operator [ ] to extract an item or a range of items from a list. The index starts from 0 in Python.
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])   # print index 0 to 2

# a[5:] = [30, 35, 40]    #print from index 5 till last
print("a[5:] = ", a[5:])

#Lists are mutable, meaning, the value of elements of a list can be altered.
a = [1, 2, 3]
a[2] = 4
print(a)  #-> [1, 2, 4]


#********************************************************************************************************************

## 3.(Tuple) - Tuple is an ordered sequence of items same as a list.
 #              - The only difference is that tuples are immutable. Tuples once created cannot be modified.
#               - Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10    # TypeError: 'tuple' object does not support item assignment

#****************************************************************************************

# 4. "Strings" - String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings.
 #                - Multi-line strings can be denoted using triple quotes, ''' or """

s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)

# - Strings are immutable. Just like a list and tuple, the slicing operator [ ] can be used with strings
s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
s[5] ='d'   # -> TypeError: 'str' object does not support item assignment


#********************************************************************************************************
## 5. {Set}    - Set is an unordered collection of unique items. Items in a set are not ordered.

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)   #->  a =  {1, 2, 3, 4, 5}

# data type of variable a
print(type(a)) #-> <class 'set'>


#We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.
a = {1,2,2,3,3,3}
print(a) # {1,2,3}

print(a[1])   #-> TypeError: 'set' object does not support indexing


#****************************************************************************************************8

#6. {Dictionary} - Key:value pair . Dictionary is an unordered collection of key-value pairs.
 #                   - It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data.
 #                   - We must know the key to retrieve the value.
#                  -  Key and value can be of any type.

d = {1:'value','key':2}
print(type(d))   #-> <class 'dict'>

# We use key to retrieve the respective value.
print("d[1] = ", d[1])  #->  d[1] =  value

print("d['key'] = ", d['key'])   #-> d['key'] =  2

# Generates error
print("d[2] = ", d[2])


#    7. Conversion between data types -
#        We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.
#

print(float(5))   #-> 5.0
print(int(10.6))  #-> 10
print(int(-10.6))  #-> -10

# Conversion to and from string must contain compatible values.

print(float('2.5'))  #-> 2.5
print(str(25))   # -> '25'
print(int('1p'))   #-> ValueError: invalid literal for int() with base 10: '1p'

# We can even convert one sequence to another.
print(set([1,2,3]))   # -> {1, 2, 3}
print(tuple({5,6,7}))  #-> (5, 6, 7)
print(list('hello'))   # print -> ['h', 'e', 'l', 'l', 'o']

## To convert to dictionary, each element must be a pair:

print(dict([[1,2],[3,4]])) # ->{1: 2, 3: 4}
print(dict([(3,26),(4,44)]))   #-> {3: 26, 4: 44}


## example for the module
def add():
    return 3+4