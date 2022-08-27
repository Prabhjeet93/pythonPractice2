"""

        Objects and Classes
            An object is simply a collection of data (variables) and methods (functions) that act on those data.
            Similarly, a class is a blueprint for that object.

            We can think of a class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows, etc.
            Based on these descriptions we build the house. House is the object.

            As many houses can be made from a house's blueprint, we can create many objects from a class.
            An object is also called an instance of a class and the process of creating this object is called instantiation.

            class definitions begin with a class keyword.
            class Animal:

            The first string inside the class is called docstring and has a brief description of the class.
            Although not mandatory, this is highly recommended.

        Creating an Object in Python -:
            john = Person()

        How to call attributes and methods of a class
            john.greet()
            it is equivalemt to -> Person.greet(john)

        Constructors in Python -:
                Class functions that begin with double underscore __ are called special functions as they have special meaning.
                Of one particular interest is the __init__() function. This special function gets called whenever a new object of that class is instantiated.
                This type of function is also called constructors in Object Oriented Programming (OOP). We normally use it to initialize all the variables.


        Deleting Attributes and Objects -
            using del keyword.
            When we do c1 = ComplexNumber(1,3), a new instance object is created in memory and the name c1 binds with it.
            On the command del c1, this binding is removed and the name c1 is deleted from the corresponding namespace.
            The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.
            This automatic destruction of unreferenced objects in Python is also called garbage collection.

"""


class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass

# As soon as we define a class, a new class object is created with the same name.
# This class object allows us to access the different attributes as well as to instantiate new objects of that class.
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

# Output: 10
print(Person.age)  # 10
# Output: <function Person.greet>
print(Person.greet)  # <function Person.greet at >
# Output: "This is a person class"
print(Person.__doc__)  # This is a person class


# Creating an Object in Python
john = Person()

# Output: <bound method Person.greet of <__main__.Person object>>
print(john.greet)

# Calling object's greet() method
# Output: Hello
john.greet()

# constructor in python - __init__()
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# print(num1.attr)


#### deleting objects and attributes
num1 = ComplexNumber(2,3)
num1.get_data()  # 2+3j
del num1
num1.get_data()  # NameError: name 'num1' is not defined.