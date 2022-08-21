"""
    What is [list]?
        A list can have any number of items and they may be of different types (integer, float, string, etc.).
        List is an ordered sequence of items.
        All the items in a list do not need to be of the same type.
        Lists are mutable, meaning, the value of elements of a list can be altered.

        e.g -> list1 = [1, 'hello', 2.3, [1,2]]

        Methods used in List :-

            Methods	    Descriptions
            len()        return the length or count of the items in the list
            list1[position] - To access the element at  position.
            append()	adds an element to the end of the list. The method doesn't return any value (returns None).
            extend()	adds all elements of a list to another list. The extend() method modifies the original list. It doesn't return any value.
            insert()	inserts an item at the defined index. The insert() method doesn't return anything; returns None. It only updates the current list.
            remove()	removes an item(first matching) from the list. The remove() doesn't return any value (returns None).
            pop()	    returns and removes an element at the given index. The pop() method returns the item present at the given index. This item is also removed from the list.
            clear() 	removes all items from the list. The clear() method only empties the given list. It doesn't return any value.
            del obj_name    del keyword is used to delete objects. Here, obj_name can be variables, user-defined objects, lists, items within lists, dictionaries etc.
            index() 	returns the index of the first matched item.
            count() 	returns the count of the number of items passed as an argument
            sort()	    sort items in a list in ascending order. But sort() changes the list directly and doesn't return any value
            sorted()    sort items in a list in ascending order. But ssorted() doesn't change the list and returns the sorted list.
            reverse()	reverse the order of items in the list. The reverse() method doesn't return any value. It updates the existing list.
            copy() 	    returns a shallow copy of the list. if we modify any one list it will not modify other list or vice versa.
            =          create a copy of the list. old_list=new_list. if we modify any one list it will  modify other list too or vice versa.

        Negative indexing
                             'p', 'r', 'o', 'b', 'e'
             index            0,  1,    2,   3,   4
            Negative Index   -5, -4,  -3,   -2,  -1
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

"""

# create a list with mix datatypes and list inside a list
list1 = [1, 'hello', 2.3, [7,8,9]]

## Len() of the list
print(len(list1)) #-> 4

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


## append() - will add item in the last of the list. We can add one item to a list using the append() method
# extend() -> use to append another list to the main list. add several items using the extend() method.
# appending using + and slicing operators.
# Appending and Extending lists in Python
odd = [1, 3, 5]
tt=[15,17]
odd.append(7)
print(odd) #-> [1, 3, 5, 7]
odd.extend([9, 11, 13])
print(odd)  #  -> [1, 3, 5, 7, 9, 11, 13]
tt.append(odd)  # it added list to a list.
print(tt)  #-> [15, 17, [1, 3, 5, 7, 9, 11, 13]]

# the + operator
a = [1, 2]
b = [3, 4]
a += b    # a = a + b
# Output: [1, 2, 3, 4]
print('a =', a)

## the slicing syntax
a = [1, 2]
b = [3, 4]
a[len(a):] = b
# Output: [1, 2, 3, 4]
print('a =', a)


# Concatenating(+) -> to combine the list and repeating(*) lists

odd = [1, 3, 5]
print(odd + [9, 7, 5])  #-> [1, 3, 5, 9, 7, 5]
print(["re"] * 3)   # -> ['re', 're', 're']


### Insert() -> insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.
# syntax -> list.insert(index, item)
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
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# deleting all elements
del my_list[:]
print(my_list)   # Output: []

# Delete variable, list, and dictionary
my_var = 5
my_tuple = ('Sam', 25)
my_dict = {'name': 'Sam', 'age': 25}
del my_var
del my_tuple
del my_dict
# Error: my_var is not defined
print(my_var)
# Error: my_tuple is not defined
print(my_tuple)
# Error: my_dict is not defined
print(my_dict)

# Delete an user-defined object

class MyClass:
    a = 10
    def func(self):
        print('Hello')
# Output:
print(MyClass)
# deleting MyClass
del MyClass
# Error: MyClass is not defined
print(MyClass)

# del With Tuples and Strings
#  Note: You can't delete items of tuples and strings in Python. It's because tuples and strings are immutables; objects that can't be changed after their creation.
my_tuple = (1, 2, 3)
# Error: 'tuple' object doesn't support item deletion
del my_tuple[1]

#However, you can delete an entire tuple or string.
my_tuple = (1, 2, 3)
# deleting tuple
del my_tuple



# remove(item) -> to remove the given item. The remove() method removes the first matching element (which is passed as an argument) from the list.
# pop() -> to remove an item at the given index. The pop() method removes and returns the last item if the index is not provided.
#       This helps us implement lists as stacks (first in, last out data structure).
#       The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
#       The pop() method returns the item present at the given index. This item is also removed from the list.
# clear() -> to empty the whole list.
# delete items in a list by assigning an empty list to a slice of elements.

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
#delete items in a list by assigning an empty list to a slice of elements.
my_list = ['p','r','o','b','l','e','m']
print(my_list)
my_list[2:4]=[]  #it will delete items from 2 to 3(4-1) index
print(my_list)  #-> ['p', 'r', 'l', 'e', 'm']
my_list[3:5]=[]  # it will delete items from 3 to 4(5-1) index
print(my_list)  #-> ['p', 'r', 'l']


# append()-> add item at the end of the list
# index() -> find the position of the given item in the list
# count() -> find the count of the given item in the list

my_list3=[3, 8, 1, 6, 8, 8, 4]
my_list3.append('a')   #-> # Add 'a' to the end
print(my_list3)   #-> #-> [3, 8, 1, 6, 8, 8, 4, 'a']
print(my_list3.index(8))   #-> 1 , # Index of first occurrence of 8
print(my_list3.count(8))   # -> 3, # Count of 8 in the list

# index method with full expression -> list.index(element, start, end)
# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# index of 'i' in alphabets
index = alphabets.index('e')   # 1
print('The index of e:', index)
# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)
# 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # Error!
# print('The index of i:', index)


## List Comprehension :
# List comprehension is an elegant and concise way to create a new list from an existing list in Python.
#
# A list comprehension consists of an expression followed by for statement inside square brackets.
pow2 = [2 ** x for x in range(10)]
print(pow2)   #-> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# A list comprehension can optionally contain more for or if statements. An optional if statement can filter out items for the new list.

pow2 = [2**x for x in range(10) if x>5]
print(pow2)   # [64, 128, 256, 512]

odd = [x for x in range(20) if x%2==1]
print(odd)  # -> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



####  List Membership Test
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print('p' in my_list)   # True
print('P' in my_list)   # False
print('l' not in my_list)  # False


##### Iterating Through a List
# Using a for loop we can iterate through each item in a list.
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
# I like apple
# I like banana
# I like mango


##### ************** Interview question *********************
#####  copy() -> The copy() method returns a new list. It doesn't modify the original list.
# if we will modify the old list , it will not modify the original list.
# but by using = , if are copying the list by this operator, and modify old list, it will modify new list as well.

# mixed list using copy method.
my_list = ['cat', 0, 6.7]
# copying a list
new_list = my_list.copy()
new_list.append('a')
print('Copied List:', new_list)   # Copied List: ['cat', 0, 6.7, 'a']
print('old List:', my_list)   # old List: ['cat', 0, 6.7]

old_list = [1, 2, 3]
# copy list using =
new_list = old_list
# add an element to list
new_list.append('a')
print('New List:', new_list)   # New List: [1, 2, 3, 'a']
print('Old List:', old_list)  # Old List: [1, 2, 3, 'a']

## using slicing operator
# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]
# copying a list using slicing
new_list = list[:]
# Adding an element to the new list
new_list.append('dog')
# Printing new and old list
print('Old List:', list)
print('New List:', new_list)

#  slicing syntax for the copying list
# shallow copy using the slicing syntax
# mixed list
list = ['cat', 0, 6.7]
# copying a list using slicing
new_list = list[:]
# Adding an element to the new list
new_list.append('dog')
# Printing new and old list
print('Old List:', list)  #-> Old List: ['cat', 0, 6.7]
print('New List:', new_list)  #-> New List: ['cat', 0, 6.7, 'dog']


## Reverse a list using reverse () -> The reverse() method doesn't return any value. It updates the existing list.

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
# reverse the order of list elements
prime_numbers.reverse()
print('Reversed List:', prime_numbers)
# Output: Reversed List: [7, 5, 3, 2]

####   Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
# Reversing a list
# Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]
# updated list
print('Updated List:', reversed_list)

# Original List: ['Windows', 'macOS', 'Linux']
# Updated List: ['Linux', 'macOS', 'Windows']

# Accessing Elements in Reversed Order using reversed() function
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)

# Linux
# macOS
# Windows


### sort () -> sorts the items of a list in ascending or descending order. sort() changes the list directly and doesn't return any value.
## Syntax -> list.sort(key=..., reverse=...)
### sorted() ->  sorted() doesn't change the list and returns the sorted list.
####  Syntax -> sorted(list, key=..., reverse=...)


## sort in ascending order
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort()
# print vowels
print('Sorted list:', vowels)  #-> Sorted list: ['a', 'e', 'i', 'o', 'u']
## sort in descending order
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print("reverse sorted list:", vowels)  #-> reverse sorted list: ['u', 'o', 'i', 'e', 'a']
print(len(vowels)) #-> 5

## Implement own method of sorting
# take second element for sort
def takeSecond(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
random.sort(key=takeSecond)
# print list
print('Sorted list:', random)  #-> Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

# Another example -
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')
def get_age(employee):
    return employee.get('age')
def get_salary(employee):
    return employee.get('salary')
# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')
# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')
# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

# [{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]
#
# [{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]
#
# [{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]


## sorted() - > The sorted() function sorts the elements of a given iterable in a specific order (ascending or descending) and returns it as a list.
# sorted(iterable, key=None, reverse=False). The sorted() function returns a sorted list.

# sort in ascending order
# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list)) #-> ['a', 'e', 'i', 'o', 'u']
# string
py_string = 'Python'
print(sorted(py_string))  # -> ['P', 'h', 'n', 'o', 't', 'y']
# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))   #-> ['a', 'e', 'i', 'o', 'u']


## Sort in ascnding order
# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))  # ['u', 'o', 'i', 'e', 'a']
# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))  # ['u', 'o', 'i', 'e', 'a']
# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))  # ['u', 'o', 'i', 'e', 'a']

## key Parameter in Python sorted() function

# take the second element for sort
def take_second(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
sorted_list = sorted(random, key=take_second)
# print list
print('Sorted list:', sorted_list)  # Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]


# Another example
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]
def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)
sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)   #  [('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]

# above code using lambda
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)   # [('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]


