"""

    Inheritance:-
        Inheritance is a way of creating a new class for using details of an existing class without modifying it.
        The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

        Syntax:-
        Parent class -> class Bird:
        child class -> class Humming(Bird): ->  this is how child class inherite the parent class.

    Python Multiple Inheritance
        A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.

        In multiple inheritance, the features of all the base classes are inherited into the derived class.
        The syntax for multiple inheritance is similar to single inheritance.

        Example:-
            class Base1:
                pass

            class Base2:
                pass

            class MultiDerived(Base1, Base2):
                pass

    Python Multilevel Inheritance:-
            We can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.
            In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class.

            Example:-
            class Base:
                pass

            class Derived1(Base):
                pass -> features of Base class

            class Derived2(Derived1):
                pass  -> Features of Derived1 Class and Base class.

    MRO - Method Resolution Order in Python
            In the multiple inheritance scenario, any specified attribute is searched first in the current class.
            If not found, the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.
            So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object].
            This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).
            MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents.
            In case of multiple parents, the order is the same as tuples of base classes.
            MRO of a class can be viewed as the __mro__ attribute or the mro() method.
            The former returns a tuple while the latter returns a list.
            e.g. - MultiDerived.__mro__
                    (<class '__main__.MultiDerived'>,
                    <class '__main__.Base1'>,
                    <class '__main__.Base2'>,
                    <class 'object'>)
"""

###### Inheritance

# parent or base class
class Bird:

    def __init__(self):
        print("Inside bird Class")

    def fly(self):
        print("Inside bird's fly method")

    def sing(self):
        print("Inside bird's sing method")

# child or derived class
class Humming(Bird):

    def __init__(self):
        print("Inside Humming class")
        # call super() function - calling parent class __init__method
        super().__init__()

    def fly(self):
        print("Inside Humming class fly method")

    def sing(self, type):
        print("Inside humming class sing method", type)

    def food(self):
        print("Inside humming class food method")

bd = Bird()   # Inside bird Class
bd.sing()    # Inside bird's sing method
hm = Humming()  # Inside Humming class # Inside bird Clas
hm.fly()  # Inside Humming class fly method
hm.sing("jazz")  # Inside humming class sing method jazz -> This is called override method
hm.food()  # Inside humming class food method
# bd.food()   # AttributeError: 'Bird' object has no attribute 'food'. IF we try to access child class attributes.


# Demonstration of MRO

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class '__main__.X'>,
#  <class '__main__.Y'>, <class '__main__.Z'>,
#  <class 'object'>]