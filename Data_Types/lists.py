"""
    What is [list]?
        A list can have any number of items and they may be of different types (integer, float, string, etc.).
        List is an ordered sequence of items.
        All the items in a list do not need to be of the same type.
        Lists are mutable, meaning, the value of elements of a list can be altered.

        e.g -> list1 = [1, 'hello', 2.3, [1,2]]

        Methods used in List :-

            Methods	    Descriptions
            list1[position] - To access the element at  position
            append()	adds an element to the end of the list
            extend()	adds all elements of a list to another list
            insert()	inserts an item at the defined index
            remove()	removes an item from the list
            pop()	    returns and removes an element at the given index
            clear() 	removes all items from the list
            index() 	returns the index of the first matched item
            count() 	returns the count of the number of items passed as an argument
            sort()	    sort items in a list in ascending order
            reverse()	reverse the order of items in the list
            copy() 	    returns a shallow copy of the list

        Negative indexing
                             'p', 'r', 'o', 'b', 'e'
             index            0,  1,    2,   3,   4
            Negative Index   -5, -4,  -3,   -2,  -1

"""

# create a list with mix datatypes and list inside a list
list1 = [1, 'hello', 2.3, [7,8,9]]

# create an empty list
list2 = []

# Access list items
print(list1[0])  #-> 1
print(list1[1])  #-> hello
print(list1[2])  # -> 2,3
print(list1[3])  # -> [7, 8, 9]

print(list1[1][2])   #-> it will print 3rd element of 1st element of the main the list -> 'l'
print(list1[3][1])   #-> 8

# Error! Only integer can be used for indexing
#print(list1[4.0])   #-> TypeError: list indices must be integers or slices, not float

# Negative Indexing

my_list = ['p','r','o','b','e']
# last item
print(my_list[-1]) # e
# fifth last item
print(my_list[-5])   # p

"""
                'p', 'r', 'o', 'b', 'e'
index            0,  1,    2,   3,   4
Negative Index   -5, -4,  -3,   -2,  -1
"""

###### List slicing in Python

my_list = ['p','r','o','g','r','a','m','e','r']

# elements from index 2 to index 4
print(my_list[2:5])   # -> ['o', 'g', 'r']

# elements from index 5 to end
print(my_list[5:])   # -> ['a', 'm', 'e', 'r']

# elements beginning to end
print(my_list[:])     # -> ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'e', 'r']

#### Add/Change List Elements
# Correcting mistake values in a list
odd = [2, 4, 6, 8]
# change the 1st item
odd[0] = 1
print(odd)    # -> [1,4,6,8]
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  # -> [1,3,5,7]
print(odd)


## append() - will add item in the last of the list.
# extend() -> use to append another list to the main list
# Appending and Extending lists in Python
odd = [1, 3, 5]
odd.append(7)
print(odd) #-> [1, 3, 5, 7]
odd.extend([9, 11, 13])
print(odd)  #  -> [1, 3, 5, 7, 9, 11, 13]


# Concatenating(+) -> to combine the list and repeating(*) lists

odd = [1, 3, 5]
print(odd + [9, 7, 5])  #-> [1, 3, 5, 9, 7, 5]
print(["re"] * 3)   # -> ['re', 're', 're']


### Insert() -> insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.

odd = [1, 9]
odd.insert(1,3)
print(odd)  #-> [1, 3, 9]
odd[2:2] = [5, 7]
print(odd)   # -> [1, 3, 5, 7, 9]


###   Delete List Elements
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]
print(my_list)  #-> ['p', 'r', 'b', 'l', 'e', 'm']
# delete multiple items
del my_list[1:5]
print(my_list)   # -> ['p', 'm']
# delete the entire list
del my_list
# Error: List not defined
#print(my_list)  # -> NameError: name 'my_list' is not defined


# remove(item) -> to remove the given item
# pop() -> to remove an item at the given index. The pop() method removes and returns the last item if the index is not provided.
#       This helps us implement lists as stacks (first in, last out data structure).
# clear() -> to empty the whole list.

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)