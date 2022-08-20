"""
    What is Name in Python?
        Name (also called identifier) is simply a name given to objects.
        Everything in Python is an object. Name is a way to access the underlying object.

        For example, when we do the assignment a = 2, 2 is an object stored in memory and a is the name we associate it with.
        We can get the address (in RAM) of some object through the built-in function id().

        Memory diagram of a variable - Check namespace_scope.pdf file
                 Initially, an object 2 is created and the name a is associated with it,
                 when we do a = a+1, a new object 3 is created and now a is associated with this object.
                  Note that id(a) and id(3) have the same values.
                   Furthermore, when b = 2 is executed, the new name b gets associated with the previous object 2.
                    This is efficient as Python does not have to create a new duplicate object.
                    This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.

    Functions -:
                 Functions are objects too, so a name can refer to them as well.


    What is a Namespace in Python?
        a namespace is a collection of names.
        In Python, you can imagine a namespace as a mapping of every name you have defined to corresponding objects.
        Different namespaces can co-exist at a given time but are completely isolated.
        A namespace containing all the built-in names is created when we start the Python interpreter and exists as long as the interpreter runs.
        This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program. Each module creates its own global namespace.
        These different namespaces are isolated. Hence, the same name that may exist in different modules does not collide.
        Modules can have various functions and classes. A local namespace is created when a function is called, which has all the names defined in it. Similar is the case with class.

    Variable Scope :-
        A scope is the portion of a program from where a namespace can be accessed directly without any prefix.

            At any given moment, there are at least three nested scopes.
                  1.  Scope of the current function which has local names
                  2. Scope of the module which has global names
                  3. Outermost scope which has built-in names
        When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.
        If there is a function inside another function, a new scope is nested inside the local scope.


"""
# Note: You may get same values for the id. - as they are associated to the same object that is 2.
# It may change everytime we run the code.
a = 2
print('id(2) =', id(2))  #-> 1811170066704

print('id(a) =', id(a)) #-> 1811170066704

# Note: You may get different values for the id

#output - id(a) = 2204091285776
a = 2
print('id(a) =', id(a))

# Output - id(a) = 2204091285808
a = a+1
print('id(a) =', id(a))

# Output - id(3) = 2204091285808
print('id(3) =', id(3))

b = 2
#Output - id(b) = 2204091285776
print('id(b) =', id(b))
#Output - id(b) = 2204091285776
print('id(2) =', id(2))


# All these are valid and a will refer to three different types of objects in different instances.
a = 5
a = 'Hello World!'
a = [1,2,3]


##Functions-: Functions are objects too, so a name can refer to them as well.

def printHello():
    print("Hello")
a = printHello
a() #-> Hello

####Example of Scope and Namespace in Python
"""
Here, the variable a is in the global namespace. Variable b is in the local namespace of outer_function() and c is in the nested local namespace of inner_function().
When we are in inner_function(), c is local to us, b is nonlocal and a is global. 
We can read as well as assign new values to c but can only read b and a from inner_function().
If we try to assign as a value to b, a new variable b is created in the local namespace which is different than the nonlocal b. 
The same thing happens when we assign a value to a.
"""
def outer_function():
    b = 20
    def inner_func():
        print("starting scope")
        c = 30
        print(c)
print("starting scope")
a = 10
print(a)

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

## Output
# a = 30
# a = 20
# a = 10


""" All references and assignments are to the global a due to the use of keyword global. """

def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

# Output
# a = 30
# a = 30
# a = 30