# """
#     What is String in Python?
#         A string is a sequence of characters.
#
#         Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0s and 1s.
#         This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encodings used.
#
#         A string is a sequence of Unicode characters.
#         Unicode was introduced to include every character in all languages and bring uniformity in encoding.
#
#         How to create a string in Python?
#             Strings can be created by enclosing characters inside a single quote or double-quotes.
#             Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.
#
#         How to access characters in a string?
#             We can access individual characters using indexing and a range of characters using slicing.
#             For indexing we use only integers. If we try to access an index out of the range or use numbers other than an integer, we will get errors.
#
#         How to change or delete a string?
#             Strings are immutable. This means that elements of a string cannot be changed once they have been assigned.
#             We can simply reassign different strings to the same name.
#
#             We cannot delete or remove characters from a string. But deleting the string entirely is possible using the del keyword.
#
#         Python String Operations:-
#             1. Concatenation of Two or More Strings -> +, * operator
#             2. Iterating Through a string - using for loop
#             3. String Membership Test
#             4. Built-in functions to Work with Python -> enumerate() and len()
#             5. Python String Formatting
#
#         Escape Sequence	   Description
#             \newline	   Backslash and newline ignored
#                 \\	        Backslash
#                 \'	        Single quote
#                 \"	        Double quote
#                 \a	        ASCII Bell
#                 \b	        ASCII Backspace
#                 \f	        ASCII Formfeed
#                 \n	        ASCII Linefeed
#                 \r	        ASCII Carriage Return
#                 \t	        ASCII Horizontal Tab
#                 \v	        ASCII Vertical Tab
#                 \ooo    	Character with octal value ooo
#                 \xHH    	Character with hexadecimal value HH
#
#          5. Raw String to ignore escape sequence
#          6. The format() Method for Formatting Strings
#          7. Common Python String Methods ->
#                    lower(), upper(), split(), find(), replace()
#
# """

# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)
my_string = "Hello"
print(my_string)
my_string = '''Hello'''
print(my_string)
# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


#Accessing string characters in Python
str = 'programmer'
print('str = ', str)   #-> str =  programmer

#first character
print('str[0] = ', str[0])  # -> str[0] =  p

#last character
print('str[-1] = ', str[-1])  # -> str[-1] =  r

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])  # -> str[1:5] =  rogr

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])   # -> str[5:-2] =  amm

my_string = 'programmer'
#print(my_string[5] = 'a')    # TypeError: 'str' object does not support item assignment
my_string = 'Python'
print(my_string)   #'Python'

# del keyword to delete entire string
# del my_string[1]   #TypeError: 'str' object doesn't support item deletion
del my_string
#print(my_string)   # NameError: name 'my_string' is not defined


## Concatenation of Two or More Strings
# Concatenation -> +
# repeat -> *

# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)  #-> str1 + str2 =  HelloWorld!
# using *
print('str1 * 3 =', str1 * 3)   #->  str1 * 3 = HelloHelloHello

# two string literals together
print('Hello ''World!')  #'Hello World!'

# using parentheses
s = ('Hello '
      'World')
print(s)  #'Hello World'

# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')   #-> 3 letters found


#String Membership Test
print('a' in 'program')   #-> True
print('at' not in 'battle')  #-> False



#  Built-in functions to Work with Python ->
#  enumerate() -> The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
#  len()  -> len() returns the length (number of characters) of the string.
str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)  #-> list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]

#character count
print('len(str) = ', len(str))  #-> len(str) =  4


# Python String Formatting
# If we want to print a text like He said, "What's there?", we can neither use single quotes nor double quotes.
# This will result in a SyntaxError as the text itself contains both single and double quotes.
#print("He said, "What's there?"")

# Solutions of above problem -> use triple quotes, use escape sequence
# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")

# escape sequence
print("C:\\Python32\\Lib")   #-> C:\Python32\Lib

print("This is printed\nin two lines")
# This is printed
# in two lines

print("This is \x48\x45\x58 representation")  #-> This is HEX representation


# Raw String to ignore escape sequence
# Sometimes we may wish to ignore the escape sequences inside a string. To do this we can place r or R in front of the string.
# This will imply that it is a raw string and any escape sequence inside it will be ignored.

print("This is \x61 \ngood example")
# This is a
# good example
print(r"This is \x61 \ngood example")
# This is \x61 \ngood example


# The format() Method for Formatting Strings
#       The format() method that is available with the string object is very versatile and powerful in formatting strings.
#       Format strings contain curly braces {} as placeholders or replacement fields which get replaced.
#       We can use positional arguments or keyword arguments to specify the order.

# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')  #-> John, Bill and Sean
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)  #-> Bill, John and Sean

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)  #-> Sean, Bill and John


# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
# 'Binary representation of 12 is 1100'

# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
# 'Exponent representation: 1.566345e+03'

# round off
print("One third is: {0:.3f}".format(1/3))
# 'One third is: 0.333'

# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
 # '|butter    |  bread   |       ham|'



# Old style formatting
x = 12.3456789
print('The value of x is %3.2f' %x)
# The value of x is 12.35
print('The value of x is %3.4f' %x)
# The value of x is 12.3457



## Common Python String Methods ->
#         lower(), upper(), split(), find(), replace()

print("PrOgRaMmeR".lower())
# 'programmer'
print("PrOgRaMmeR".upper())
# 'PROGRAMMER'
print("This will split all words into a list".split())
# ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
# 'This will join all words into a string'
print('Happy New Year'.find('ew'))
# 7
print('Happy New Year'.replace('Happy','Brilliant'))
# 'Brilliant New Year'


