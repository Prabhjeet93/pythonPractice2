"""

    Python (Tuple)
        A tuple in Python is similar to a list.
        The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
        Methods that add items or remove items are not available with tuple.
        A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

    tuple packing-:
        A tuple can also be created without using parentheses. This is known as tuple packing.

    Creating a tuple with one element is a bit tricky.
    Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.

    Access Tuple Elements:
        1. Indexing
        2. Negative Indexing
        3. slicing

    Changing a Tuple:
        Unlike lists, tuples are immutable.
        This means that elements of a tuple cannot be changed once they have been assigned.
        But, if the element is itself a mutable data type like a list, its nested items can be changed.
        We can also assign a tuple to different values (reassignment).

    concatenation and repeat:
        concatenation: use + operator to combine two tuples.
        repeat: We can also repeat the elements in a tuple for a given number of times using the * operator.
        Both + and * operations result in a new tuple.

    Deleting a Tuple:
        Deleting a tuple entirely, however, is possible using the keyword del.
        We cannot delete or remove items from a tuple.

    tuple.count(item) -> return the count the ocuurrence of given item in the tuple.
    tuple.index(item) -> return the position of the given item in the tuple.

    Tuple Membership Test:
        We can test if an item exists in a tuple or not, using the keyword in.

    Iterating Through a Tuple
        We can use a for loop to iterate through each item in a tuple.

    Advantages of Tuple over List
        * Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list.
        Below listed are some of the main advantages:
         * We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
         * Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
         * Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
         * If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.





"""

# Creating a Tuple
# Empty tuple
my_tuple1=()
print(my_tuple1)  #-> ()
# Tuple having integers
my_tuple1=(1,2,3)
print(my_tuple1)   #-> (1, 2, 3)

# Different types of tuples

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple) #->  (1, 'Hello', 3.4)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)  #-> ('mouse', [8, 4, 6], (1, 2, 3))


# tuple packing-:
#         A tuple can also be created without using parentheses. This is known as tuple packing.

my_tuple=3.4, 'hello', 5
print(my_tuple)
# tuple unpacking is also possible
a, b, c = my_tuple
#a,b,c,d  = my_tuple

print(a) # 3.4
print(b)  # hello
print(c)  # 5
#print(d)  #-> ValueError: not enough values to unpack (expected 4, got 3)


# Creating a tuple with one element is a bit tricky.
# Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.

my_tuple=("hello")
print((type(my_tuple)))  #-> <class 'str'>

# Creating a tuple having one element
my_tuple1 = ("hello",)
print((type(my_tuple1)))  #-> <class 'tuple'>

# Parentheses is optional
my_tuple2 = "hello",
print((type(my_tuple2)))  #-> <class 'tuple'>

# Access Tuple Elements

# 1. Indexing
# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p'
print(my_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]
# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

# 2. Negative Indexing
# Negative indexing for accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

# Output: 't'
print(my_tuple[-1])   # t

# Output: 'p'
print(my_tuple[-6])  # p

# 3. Slicing :
# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','e','r')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'e', 'r')
print(my_tuple[:])


#### Changing tuple values - we can not change tuple value but if any list is an item in the tuple that we can change.
my_tuple = (4, 2, 3, [6, 5])

# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'e', 'r')
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)


### concatenation and repeat:
# + operator and * operator
# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)



#### Deleting a Tuple:
# Deleting tuples
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple
# NameError: name 'my_tuple' is not defined
#print(my_tuple)


# Tuple Methods -> count and index
my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3



# Tuple Membership Test:
#        We can test if an item exists in a tuple or not, using the keyword in.

# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple) # True
print('b' in my_tuple)  # False

# Not in operation
print('g' not in my_tuple)  # True


# Iterating Through a Tuple
#         We can use a for loop to iterate through each item in a tuple.

# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)

# Hello John
# Hello Kate

