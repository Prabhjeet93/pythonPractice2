"""
    Rules and Naming Convention for Variables and constants
        * Constant and variable names should have a combination of letters in
          lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
        * Use capital letters possible to declare a constant.
"""


num = 10
print(num) # 10
num2=1.1
print(num2)
count_num = 4
str1='apple'
str2 = "banana"
print(str1)
num=11 # value of num variable is changed now

print(num) # 11

#Assigning multiple values to multiple variables
a, b, c = 2.1, 7, "Tree"

print (a)
print (b)
print (c)

# If we want to assign the same value to multiple variables at once, we can do this as:

x = y = z = "same"

print (x)
print (y)
print (z)

"""
    Constants
        * A constant is a type of variable whose value cannot be changed
        * In Python, constants are usually declared and assigned in a module. Here, the module is a 
        new file containing variables, functions, etc which is imported to the main file. 
        Inside the module, constants are written in all capital letters and underscores separating the words.
"""

#Create a constant.py:
#PI = 3.14
#GRAVITY = 9.8
#Create a main.py:
import constant

print(constant.PI)
print(constant.GRAVITY)