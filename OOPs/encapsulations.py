"""

    Encapsulation:-
        Using OOP in Python, we can restrict access to methods and variables.
        This prevents data from direct modification which is called encapsulation.
        In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
        But we can change these constants value by creating setter() method.

"""

class Gadget:

    def __init__(self):
        # private variables
        self.__maxprice='1500'
        self._memory='1024'

    def storage(self):
        print("This gadget has {} GB memory".format(self._memory))

    def sellingprice(self, type):
        print("The selling price of {} is ${}".format(type, self.__maxprice))

    def setterStorage(self, newmemory):
        self._memory=newmemory


laptop = Gadget()
laptop.storage()
laptop.sellingprice("Dell")  # The selling price of Dell is $1500

# trying to change the private variable or constant's value
laptop.__maxprice = 2000
laptop.sellingprice("HP")  # The selling price of HP is $1500

# changing constant's or private variable value with setter method.
laptop.setterStorage('2048')
laptop.storage()  # This gadget has 2048 GB memory
