"""

    Operator Overloading:-
            Python operators work for built-in classes. But the same operator behaves differently with different types.
            For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
            This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading

            Objects can't be added with + operator. it throws an error.
            we can achieve this task in Python through operator overloading

"""

# demo of operator overloading with + on objects. we will get error.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(2, 3)
# print(p1+p2)  # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2, 3)
print(p1)  # (2, 3)

# Overloading the + Operator, we will add __add__() function.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)  # (3,5)
# when we called p1+p2 , actually called p1.__add__(p2) and then it is equivalent to Point.__add__(p1,p2)

# overloading the less than operator
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1,-1)

# use less than
print(p1<p2)  # True
print(p2<p3)  # False
print(p1<p3)  # False

"""
			Operator	        Expression	        Internally
			Addition	        p1 + p2	        p1.__add__(p2)
			Subtraction	        p1 - p2	        p1.__sub__(p2)
			Multiplication	     p1 * p2	        p1.__mul__(p2)
			Power	             p1 ** p2	        p1.__pow__(p2)
			Division	         p1 / p2	        p1.__truediv__(p2)
			Floor Division	     p1 // p2	        p1.__floordiv__(p2)
			Remainder (modulo)	  p1 % p2	        p1.__mod__(p2)
			Bitwise Left Shift	  p1 << p2	        p1.__lshift__(p2)
			Bitwise Right Shift	  p1 >> p2	        p1.__rshift__(p2)
			Bitwise AND	          p1 & p2	        p1.__and__(p2)
			Bitwise OR	         p1 | p2	        p1.__or__(p2)
			Bitwise XOR	          p1 ^ p2	        p1.__xor__(p2)
			Bitwise NOT	~          p1	           p1.__invert__()
			
			
			Operator        	    Expression	        Internally
			Less than	              p1 < p2	        p1.__lt__(p2)
			Less than or equal to	     p1 <= p2	        p1.__le__(p2)
			Equal to	                 p1 == p2	        p1.__eq__(p2)
			Not equal to	            p1 != p2	        p1.__ne__(p2)
			Greater than	            p1 > p2	        p1.__gt__(p2)
			Greater than or equal to	 p1 >= p2	        p1.__ge__(p2)
"""