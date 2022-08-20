"""
    What is for loop in Python?
        The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
        Iterating over a sequence is called traversal.

        Syntax -:
                for val in sequence:
                    loop body

    range() function :-
            *Generate a sequence of numbers using range() function.
            *range(10) will generate numbers from 0 to 9 (10 numbers).
            *We can also define the start, stop and step size as range(start, stop,step_size). step_size defaults to 1 if not provided.
            *The range object is "lazy" in a sense because it doesn't generate every number that it "contains" when we create it. However, it is not an iterator since it supports in, len and __getitem__ operations.
            *This function does not store all the values in memory; it would be inefficient.
             So it remembers the start, stop, step size and generates the next number on the go.
            *To force this function to output all the items, we can use the function list().
            *We can use the range() function in for loops to iterate through a sequence of numbers.
             It can be combined with the len() function to iterate through a sequence using indexing.

    for loop with else
        A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
        The break keyword can be used to stop a for loop. In such cases, the else part is ignored.
        Hence, a for loop's else part runs if no break occurs.

"""

str1 = "Canada"
for char in str1:
    print(char)
#output:-
# C
# a
# n
# a
# d
# a

lst1 = ['Hello', 1, 4.5, [1,'world', 3]]
for val in lst1:
    print(val)

# Hello
# 1
# 4.5
# [1, 'world', 3]

lst1 = ['Hello', [1,'world', 3]]
for val in lst1:
    print(val)
    for val1 in val:
        print(val1)

# Hello
# H
# e
# l
# l
# o
# [1, 'world', 3]
# 1
# world
# 3

# find sum of given numbers

nums = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum=0
for val1 in nums:
    sum +=val1

print(sum)  #-> 48

#range() method, we use list method to print the values

print(range(10)) #-> range(0, 10)
print(list(range(10)))  #-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2,8)))   #-> [2, 3, 4, 5, 6, 7]
print(list(range(2,20, 3)))  #-> [2, 5, 8, 11, 14, 17]

# We can use the range() function in for loops to iterate through a sequence of numbers.
# It can be combined with the len() function to iterate through a sequence using indexing.

locations = ["toronto", "ottawa", "mississauga"]

#for city in range(locations):
 #   print(city)

# TypeError: 'list' object cannot be interpreted as an integer
for city in range(len(locations)):
    print(city)
    print("I travel to ", locations[city])

# 0
# i travel to  toronto
# 1
# i travel to  ottawa
# 2
# i travel to  mississauga


# for loop with else
#         A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
#         The break keyword can be used to stop a for loop. In such cases, the else part is ignored.
#         Hence, a for loop's else part runs if no break occurs.

digits = [1,3,7]

for i in digits:
    print(i)
# else will be executed when for loop exhausted.
else:
    print("Nothing Left")

# 1
# 3
# 7
# Nothing Left


# for loop on Dictionary and using break statement

city = 'toronto'

data1 = {'ottawa':1000, 'toronto':100, 'bellevile':10000}
for val in data1:
    if val == city:
        print(val+" has ",str(data1[val]) +' people')
        break
    else:
        print(" No data match")






