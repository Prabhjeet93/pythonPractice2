"""
    Python Statement
        * Instructions that a Python interpreter can execute are called statements.
        * For example, a = 1 is an assignment statement. if statement, for statement, while statement, etc.

"""
#Multi-line statement
#In Python, the end of a statement is marked by a newline character.
# But we can make a statement extend over multiple lines with the line continuation character (\)
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
#This is an explicit line continuation.
print(a)   # 45
#Line continuation is implied inside parentheses ( ), brackets [ ], and braces { }.
b = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print(b) # 45
colors = ['red',
          'blue',
          'green']
print(colors)
#Print in Next Line
# with triple quotes we can write in new line
print("""Nothing
Permanent""")
#this is another way to print in next line
print("this"  
      " is the best")
# new line with /n
print("\n")
print("we have new line")

#We can also put multiple statements in a single line using semicolons, as follows:
a = 1; b = 2; c = 3

