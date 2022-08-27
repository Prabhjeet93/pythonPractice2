"""
    Object Oriented Programming
        Python is a multi-paradigm programming language. It supports different programming approaches.
        One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).
        An object has two characteristics:
            1. attributes
            2. behavior

        lets take an example:

        We have an object name Animal.
        This animal object has attributes like - name, color
        and behaviour as swim, run

    Class:-
        A class is a blueprint for the object.

        We can think of class as a sketch of a animal with labels. It contains all the details about the name, colors, size etc.
        Based on these descriptions, we can study about the animal. Here, a animal is an object.
        syntax-
        class Animal:
            pass
    Instances -
        An instance is a specific object created from a particular class.

    Object:-
        When class is defines that time only description of the class is defined no memory or storage allocation or anything else.
        An object(instance) is an instantiation  of a class.
        syntax-
            dog = Animal()
            dog -> is an object of class Animal.

        How to access class attributes -
            <obj>.__class__.<attribute_name>    ->   dog.__class__.legs
            Class attributes are the same for all instances of a class.

        How to access instance attributes -
            <obj>.<instance_attriute>  ---> dog.name
            instance attributes are different for every instance of a class

        __init__() -
            It is the initializer method that is first run as soon as the object is created.

    Methods:-
        Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
        syntax - def sing(self):





"""

# Demo of Class object and methods.
class Animal:

    # class attributes
    legs = 4

    # instance attributes
    def __init__(self, name,color, age):
        self.name = name
        self.color = color
        self.age = age
        print("Hello New Object")

    def run(self,platforms):
        return self.name,'runs faster on {}'.format(platforms)

    def swim(self):
        return self.name, " is swiiming"



# instaniate the Animal class.
# dog = Animal() # TypeError: Animal.__init__() missing 2 required positional arguments: 'color' and 'age'
dog = Animal('oscar','red',5)  # Hello New Object
cat = Animal('bruno','black',3)  # Hello New Object

# access the class attributes
print('oscar is a {} legs animal'.format(dog.__class__.legs))  # oscar is a 4 legs animal
print('bruno is a {} legs animal'.format(cat.__class__.legs))  # bruno is a 4 legs animal

# access the instance attributes
print("{} is {} years old and has color {}".format(dog.name, dog.age, dog.color))  # oscar is 5 years old and has color red
print("{} is {} years old and has color {}".format(cat.name, cat.age, cat.color))  # bruno is 3 years old and has color black

# call instance methods
print(dog.run('ground'))  # ('oscar', 'runs faster on ground')
print(cat.run('tree'))  # ('bruno', 'runs faster on tree')
print(dog.swim())  # ('oscar', ' is swiiming')
print(cat.swim())  # ('bruno', ' is swiiming')








