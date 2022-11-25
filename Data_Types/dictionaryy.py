"""
    Dictionary:- {key:value}
        Dictionaries to Store key/value Pairs.
        Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.
        Dictionaries are optimized to retrieve values when the key is known.

        While the values can be of any data type and can repeat,
        keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.

    Accessing Elements from Dictionary
        While indexing is used with other data types to access values, a dictionary uses keys.
        Keys can be used either inside square brackets [] or with the get() method.

        if key is not present in the dictionary and try to access with key indexing, it ill throw error
        and if e try with get() method then it will not throw error , instead it will return None.

    Changing and Adding Dictionary elements:
        Dictionaries are mutable. We can add new items or change the value of existing items using an assignment operator.
        If the key is already present, then the existing value gets updated. In case the key is not present, a new (key: value) pair is added to the dictionary.

    Removing elements from Dictionary:
        pop() -> This method removes an item with the provided key and returns the value.
        popitem() -> This method can be used to remove and return an arbitrary (key, value) item pair from the dictionary
        clear() -> All the items can be removed at once
        del keyword -> This keyword use to remove individual items or the entire dictionary itself.


    Python Dictionary Methods:
        Method	        Description
        clear()	        Removes all items from the dictionary.
        copy()	        Returns a shallow copy of the dictionary.
        fromkeys(seq[, v])	Returns a new dictionary with keys from seq and value equal to v (defaults to None).
        get(key[,d])	Returns the value of the key. If the key does not exist, returns d (defaults to None).
        items()	        Return a new object of the dictionary's items in (key, value) format.
        keys()	        Returns a new object of the dictionary's keys.
        pop(key[,d])	Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
        popitem()	    Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
        setdefault(key[,d])	Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).
        update([other])	Updates the dictionary with the key/value pairs from other, overwriting existing keys.
        values()	    Returns a new object of the dictionary's values


            Function	Description
            all()	    Return True if all keys of the dictionary are True (or if the dictionary is empty).
            any()	    Return True if any key of the dictionary is true. If the dictionary is empty, return False.
            len()	    Return the length (the number of items) in the dictionary.
            cmp()	    Compares items of two dictionaries. (Not available in Python 3)
            sorted()	Return a new sorted list of keys in the dictionary


    Python Dictionary Comprehension:
        Dictionary comprehension is an elegant and concise way to create a new dictionary from an iterable in Python.
        Dictionary comprehension consists of an expression pair (key: value) followed by a for statement inside curly braces {}.
        # Dictionary Comprehension
        squares = {x: x*x for x in range(6)}
        syntax -> dictionary = {key: value for vars in iterable}

    Dictionary Membership Test:
        We can test if a key is in a dictionary or not using the keyword in.
        Note:- that the membership test is only for the keys and not for the values.

    Iterating Through a Dictionary:
        We can iterate through each key in a dictionary using a for loop.


"""

# Create Dictionary using {} or dict()

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)


# Accessing Elements from Dictionary
# using key indexing or get()
# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}
# Output: Jack
print(my_dict['name'])
# Output: 26
print(my_dict.get('age'))
# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))
# KeyError
# print(my_dict['address'])  # KeyError: 'address'


###  Changing and Adding Dictionary elements
# we can change value of dictionary using = operator

my_dict = {'name': 'Jack', 'age': 26}
# update value existing value
my_dict['age'] = 27
#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)   # {'name': 'Jack', 'age': 27
# add item, new key and value added
my_dict['address'] = 'Downtown'
# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)    # {'name': 'Jack', 'age': 27, 'address': 'Downtown'}

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# remove a particular item, returns its value
print(squares.pop(4))  # Output: 16
print(squares) # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# remove an arbitrary item, return (key,value)
print(squares.popitem())  # Output: (5, 25)
print(squares)   # Output: {1: 1, 2: 4, 3: 9}
squares.clear()  # remove all items
print(squares) # Output: {}
del squares  # delete the dictionary itself
# Throws Error
#print(squares)   # NameError: name 'squares' is not defined


# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)  # Output: {'English': 0, 'Math': 0, 'Science': 0}
for item in marks.items():
    print(item)
# ('Math', 0)
# ('English', 0)
# ('Science', 0)
print(list(sorted(marks.keys())))  # Output: ['English', 'Math', 'Science']


# Python Dictionary Comprehension
#
squares = {x: x*x for x in range(6)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# This code is equivalent to
squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)

# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)   # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

#item price in dollars - Comprehension
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)  # {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}

# Nested Dictionary with Two Dictionary Comprehensions
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)
# {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
# 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
# 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}
# above code is equivalent to this one.
dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print(dictionary)

# OR
dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = dict()
    for k2 in range(1, 6):
        dictionary[k1][k2] = k1*k2
print(dictionary)

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares)
# Output: True
print(2 not in squares)
# membership tests for key only not value
# Output: False
print(49 in squares)

# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

# 1
# 9
# 25
# 49
# 81

# Dictionary Built-in Functions
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: False
print(all(squares))
# Output: True
print(any(squares))
# Output: 6
print(len(squares))
# Output: [0, 1, 3, 5, 7, 9]
print(sorted(squares))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))   # {1: 'one', 2: 'two'} length is 2

testDict = {}
print(testDict, 'length is', len(testDict))  # {} length is 0

## all() works with Python dictionary - f all keys (not values) are true or the dictionary is empty, all() returns True. Else, it returns false for all other cases..
s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))


# any()
# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))