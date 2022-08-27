"""

    Polymorphism:-
        One name multiple forms
        Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

        Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
        However we could use the same method to color any shape. This concept is called Polymorphism.

        e.g
        1+1 = 2 -> integer addition
        'hello'+' world' =hello world -> strings conatenation.
        + operator doing different task when data types are changed.

        another example is len() -> it gves length of the string, list and keys in dictionary.

    Polymorphism and Inheritance:-
            the child classes in Python also inherit methods and attributes from the parent class.
            We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.
            Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

    Note: Method Overloading, a way to create multiple methods with the same name but different arguments, is not possible in Python.

"""

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)  # Parrot can fly
flying_test(peggy)   # Penguin can't fly



####################

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

# Meow
# I am a cat. My name is Kitty. I am 2.5 years old.
# Meow
# Bark
# I am a dog. My name is Fluffy. I am 4 years old.
# Bark




###############################################3

###  Method Overriding
from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)   # Circle
print(b.fact())  # I am a two-dimensional shape.
print(a.fact())  # Squares have each angle equal to 90 degrees.
print(b.area())  # 153.93804002589985
