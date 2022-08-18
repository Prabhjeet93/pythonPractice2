
"""
    Python provides numerous built-in functions that are readily available to us at the Python prompt.
    for example - : input() and print() are  used for standard input and output operations respectively.

     1. Output Using print() function -: print() function to output data to the standard output device (screen).
            Syntax -
                    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
                        * objects is the value(s) to be printed.
                        * The sep separator is used between the values. It defaults into a space character.
                        * After all values are printed, end is printed. It defaults into a new line.
                        * The file is the object where the values are printed and its default value is sys.stdout (screen).

            Output formatting: use str.format() method. This method is visible to any string object.
               x=5, y=6, print('The value of x is {} and y is {}'.format(x,y)) -> The value of x is 5 and y is 6

     2. Input using input() function : -
                           To allow flexibility, we might want to take the input from the user.
                           Syntax - :
                                  input([prompt])

     3. Import : When our program grows bigger, it is a good idea to break it into different modules.
                 A module is a file containing Python definitions and statements.
                 Python modules have a filename and end with the extension .py
                 Definitions inside a module can be imported to another module or the interactive interpreter in Python.
                  We use the import keyword to do this. eg. -> import math,  from math import pi
                  While importing a module, Python looks at several places defined in sys.path. It is a list of directory locations.


"""

 ## print () method
print('Hello')  # Hello
a=2
print("This number is : ", a)


# Syntax - : print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1, 2, 3, 4)   # 1 2 3 4
print(1, 2, 3, 4, sep='*') # 1*2*3*4
print(1, 2, 3, 4, sep='#', end='&')  # 1#2#3#4&


## Output formatting: use str.format() method. This method is visible to any string object.
x = 5; y =6
print("The value of x is {} and y is {}" .format(x,y) ) #-> The value of x is 5 and y is 10

# we can use index also
print("I love {0} but not {1}" .format("python","C#"))   # I love python but not C#

print("I love {1} but not {0}" .format("python","C#"))    # I love C# but not python

# We can even use keyword arguments to format the string.

print("Hello {name}, I'm a {profession}" .format(name='Patrick', profession='Mentalist')) # -> Hello Patrick, I'm a Mentalist

# using % operator

x= 12.34567
print("The value of x is %.2f" %x)  # ->  The value of x is 12.35
print("The value of x is %.4f" %x)  # ->  The value of x is 12.3457

## input () -> To allow flexibility, we might want to take the input from the user.
num = input('Enter a number')   #-> it will open a prompt with this  and thn we will enter values and click on enter button. Enter a number10
print(num)  # 10

# type conversion
print(int('10')) #-> 10
print(float('10'))  #-> 10.0

print(int('2+3'))  # -> ValueError: invalid literal for int() with base 10: '2+3'

# we can use eval () also
print(eval('2+3')) #- -> 5


import math
print(math.pi)   #-> 3.141592653589793

## Now all the definitions inside math module are available in our scope.
# We can also import some specific attributes and functions only, using the from keyword
from math import pi
print(pi)  #-> 3.141592653589793

#sys.path is a list of directory locations.
import sys
print(sys.path)

# output
# ['',
#  'C:\\Python33\\Lib\\idlelib',
#  'C:\\Windows\\system32\\python33.zip',
#  'C:\\Python33\\DLLs',
#  'C:\\Python33\\lib',
#  'C:\\Python33',
#  'C:\\Python33\\lib\\site-packages']
