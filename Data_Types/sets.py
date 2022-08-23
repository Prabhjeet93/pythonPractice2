"""
        {Sets} :-
            A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
            However, a set itself is mutable. We can add or remove items from it.
            Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
            It can have any number of items and they may be of different types (integer, float, tuple, string etc.).
            But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

            Creating an empty set is a bit tricky.
            Empty curly braces {} will make an empty dictionary in Python.
            To make a set without any elements, we use the set() function without any argument.

        Modifying a set in Python:
            Sets are mutable. However, since they are unordered, indexing has no meaning.
            We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.
            We can add a single element using the add() method, and multiple elements using the update() method.
            The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

        Removing elements from a set:
            A particular item can be removed from a set using the methods discard() and remove().
            The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set.
            On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).
            we can remove and return an item using the pop() method. Since set is an unordered data type, there is no way of determining which item will be popped. It is completely arbitrary.
            We can also remove all the items from a set using the clear() method.

        Python Set Operations:
            Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference.
            A = {1, 2, 3, 4, 5}
            B = {4, 5, 6, 7, 8}
            union -> A | B, A.union(B)   -> a set of all elements from both sets.
            intersection - A & B, A.intersection(B)  -> a set of elements that are common in both the sets.
            set difference -> A - B, A.difference(B)   -> (A - B) is a set of elements that are only in A but not in B. and viceversa
            Symmetric difference -> A ^ B, A.symmetric_difference(B)  -> a set of elements in A and B but not in both (excluding the intersection).

        Methods:-
            Method	                  Description
            add()	                Adds an element to the set
            clear()	                Removes all elements from the set
            copy()	                Returns a copy of the set
            difference()	        Returns the difference of two or more sets as a new set
            difference_update() 	Removes all elements of another set from this set
            discard()	            Removes an element from the set if it is a member. (Do nothing if the element is not in set)
            intersection()	        Returns the intersection of two sets as a new set
            intersection_update()	Updates the set with the intersection of itself and another
            isdisjoint()                    Returns True if two sets have a null intersection
            issubset()	                   Returns True if another set contains this set
            issuperset()	                Returns True if this set contains another set
            pop()	                        Removes and returns an arbitrary set element. Raises KeyError if the set is empty
            remove()	                    Removes an element from the set. If the element is not a member, raises a KeyError
            symmetric_difference()	        Returns the symmetric difference of two sets as a new set
            symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
            union()	                         Returns the union of sets in a new set
            update()    	                Updates the set with the union of itself and others

"""

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)  # {1, 2, 3}

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)   # {1.0, 'Hello', (1, 2, 3)}

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)   # {1, 2, 3, 4}

# using set() method.
# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)   # {1,2,3}

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.
#my_set = {1, 2, [3, 4]}   # TypeError: unhashable type: 'list'

# Distinguish set and dictionary while creating empty set
# initialize a with {}
a = {}
# check data type of a
print(type(a))   # <class 'dict'>
# initialize a with set()
a = set()
# check data type of a
print(type(a))   # <class 'set'>


# Modifying sets
# initialize my_set
my_set = {1, 3}
print(my_set)  # {1, 3}
# my_set[0]   # as indexing not possible because they are unordered. TypeError: 'set' object does not support indexing
# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)
# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)
# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Difference between discard() and remove()
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)  # {1, 3, 4, 5, 6}
# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError
#my_set.remove(2)   #KeyError: 2

# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)  # {'W', 'H', 'r', 'o', 'l', 'd', 'e'}
# pop an element
# Output: random element
print(my_set.pop())   # W
# pop another element
my_set.pop()
print(my_set)  # {'r', 'o', 'l', 'd', 'e'}
# clear my_set
# Output: set()
my_set.clear()
print(my_set)   # set()



# Set operations - > Union, Intersection, Difference and symmetric difference.

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
# use union function
print(A.union(B))  # {1, 2, 3, 4, 5, 6, 7, 8}
# use union function on B
print(B.union(A))  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
# use & operator
# Output: {4, 5}
print(A & B)
# use intersection function on A
print(A.intersection(B))  # {4, 5}
# use intersection function on B
print(B.intersection(A))  # {4, 5}


# Difference of two sets
# use - operator on A
# Output: {1, 2, 3}
print(A - B)
# use difference function on A
print(A.difference(B)) # {1, 2, 3}
# use - operator on B
print(B - A) # {8, 6, 7}
# use difference function on B
print(B.difference(A))  # {8, 6, 7}

# Symmetric difference of two sets
# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
# use symmetric_difference function on A
print(A.symmetric_difference(B))   # {1, 2, 3, 6, 7, 8}
# use symmetric_difference function on B
print(B.symmetric_difference(A)) # {1, 2, 3, 6, 7, 8}