"""
    List Comprehension :
        List comprehension is an elegant and concise way to create a new list from an existing list in Python.
        A list comprehension consists of an expression followed by for statement inside square brackets.
        pow2 = [2 ** x for x in range(10)]
        print(pow2)   #-> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

        Above code is equivalent of below code.
        pow2 = []
        for x in range(10):
            pow2.append(2 ** x)

        A list comprehension can optionally contain more for or if statements. An optional if statement can filter out items for the new list.

        List comprehension is generally more compact and faster than normal functions and loops for creating list.
"""


## List Comprehension :
# List comprehension is an elegant and concise way to create a new list from an existing list in Python.
#
# A list comprehension consists of an expression followed by for statement inside square brackets.

# Suppose, we want to separate the letters of the word human and add the letters as items of a list.
# The first thing that comes in mind would be using for loop.

h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)   #-> ['h', 'u', 'm', 'a', 'n']

# Iterating through a string Using List Comprehension
h_letters = [ letter for letter in 'human' ]
print( h_letters)


pow2 = [2 ** x for x in range(10)]
print(pow2)   #-> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# A list comprehension can optionally contain more for or if statements. An optional if statement can filter out items for the new list.

pow2 = [2**x for x in range(10) if x>5]
print(pow2)   # [64, 128, 256, 512]

odd = [x for x in range(20) if x%2==1]
print(odd)  # -> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)  #-> [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#  if...else With List Comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj) #-> ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

# List Comprehensions vs Lambda functions
## 1.  Using Lambda functions inside List
letters = list(map(lambda x: x, 'human'))
print(letters)    #-> ['h', 'u', 'm', 'a', 'n']


# Nested Loops in List Comprehension
## Example of Transpose of Matrix

# 1. Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)  # [[1, 4], [2, 5], [3, 6], [4, 8]]

# 2. Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)   # -> [[1, 3, 5, 7], [2, 4, 6, 8]]

