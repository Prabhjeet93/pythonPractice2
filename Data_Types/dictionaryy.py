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



