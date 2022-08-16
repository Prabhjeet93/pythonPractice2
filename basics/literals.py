"""
    Literals
        Literal is a raw data given in a variable or constant.
        1. Numeric Literals
        2. String literals
        3. Boolean literals
        4. Special literals - e.g. - None
        5. Literal Collections - List literals, Tuple literals, Dict literals, and Set literals.
"""

""" 1. Numeric Literals """
#   Numeric Literals are immutable (unchangeable).
#   Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

a = 0b1010   #Binary Literals
b = 100      #Decimal Literal
c = 0o310    #Octal Literal
d = 0x12c    #Hexadecimal Literal

#Float Literal
float_1 = 10.5

#exponential and is equivalent to 1.5 * 102.
float_2 = 1.5e2

#Complex Literal
x = 3.14j

#When we print the variables, all the literals are converted into decimal values.
print(a, b, c, d)
print(float_1, float_2)

# use imaginary literal (x.imag) and real literal (x.real) to create imaginary and real parts of complex numbers.
print(x, x.imag, x.real)

"""
Ouput of number literals
10 100 200 300
10.5 150.0
3.14j 3.14 0.0
"""

"""2. String literals"""
#  A string literal is a sequence of characters surrounded by quotes. We can use both single, double, or triple quotes for a string.
#  And, a character literal is a single character surrounded by single or double quotes.

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)   # Unicode literal which supports characters other than English. In this case, \u00dc represents Ü and \u00f6 represents ö.
print(raw_str)

"""
Ouput of String literals

This is Python
C
This is a multiline string with more than one line code.
Ünicöde
raw \n string
"""

""" 3. Boolean literals """
# A Boolean literal can have any of the two values: True or False.

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

"""
Output of Boolean literals.

x is True
y is False
a: 5
b: 10
"""

""" 4. Special literals """
# Python contains one special literal i.e. None. We use it to specify that the field has not been created.

drink = "Available"
food = None

#creating method menu and passing one variable
def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink) # calling method
menu(food)  # calling method

""" output 
Available
None
"""


""" 5. Literal Collections """
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

""" 
OUTPUT :- 
['apple', 'mango', 'orange']
(1, 2, 3)
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
{'e', 'a', 'u', 'i', 'o'}
"""