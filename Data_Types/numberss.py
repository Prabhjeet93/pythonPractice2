"""
    Number Data Type in Python:-
        int(5), float(5.0), and complex(x + yj) classes in Python.

        type() function to know which class a variable or a value belongs to.
        isinstance() function to check if it belongs to a particular class.

    Type Conversion:
        print(1 + 2.0) -> 3.0 -> implicit
        print(float(5)) -> 5.0 -> explicit

    Python Decimal:
        print( (1.1 + 2.2) == 3.3)   -> False

        *********************** Important Note ***************************
        What is going on?
            It turns out that floating-point numbers are implemented in computer hardware as binary fractions as the computer only understands binary (0 and 1). Due to this reason, most of the decimal fractions we know, cannot be accurately stored in our computer.
            Let's take an example. We cannot represent the fraction 1/3 as a decimal number. This will give 0.33333333... which is infinitely long, and we can only approximate it.
            It turns out that the decimal fraction 0.1 will result in an infinitely long binary fraction of 0.000110011001100110011... and our computer only stores a finite number of it.
            This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer hardware and not an error in Python.

            isuue -> print(1.1 + 2.2)   -> 3.3000000000000003
                To overcome this issue, we can use Decimal module.

        Why not implement Decimal every time, instead of float?
            The main reason is efficiency. Floating point operations are carried out much faster than Decimal operations.

        When to use Decimal instead of float?
            We generally use Decimal in the following cases.
            When we are making financial applications that need exact decimal representation.
            When we want to control the level of precision required.
            When we want to implement the notion of significant decimal places.

    Python Fractions:
        Python provides operations involving fractional numbers through its fractions module.
        A fraction has a numerator and a denominator, both of which are integers.
        This module has support for rational number arithmetic.

            Example:
                print(fractions.Fraction(1.5))  #-> 3/2
                print(fractions.Fraction(5))   #-> 5
                print(fractions.Fraction(1,3))  # -> 1/3

        While creating Fraction from float, we might get some unusual results.
        This is due to the imperfect binary floating point number representation as discussed in the previous section.

        Fortunately, Fraction allows us to instantiate with string as well. This is the preferred option when using decimal numbers.
            # As float
            # Output: 2476979795053773/2251799813685248
            print(fractions.Fraction(1.1))

            # As string
            # Output: 11/10
            print(fractions.Fraction('1.1'))


    Math function :
    math.pi, cos,exp(10), log10(1000), math.sinh(1), math.factorial(6)

    random function
    random.randrange(10, 20) -> any random number between the range
    random.random() -> any random number
    random.shulle(), random.choice()

"""

a = 5
print(type(a))   #->  <class 'int'>
print(type(5.0))  #-> <class 'float'>
c = 5 + 3j
print(c + 3)  # (8+3j)
print(isinstance(c, complex)) #-> True

# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10)

# Output: 13
print(0o15)


####   Type conversion

print(1 + 2.0)    # -> 3.0 -> implicit
print(float(5))   # -> 5.0 -> explicit

print(int(2.3))
print(int(-2.8))
print(float(5))
print(complex('3+5j'))
print(complex(3)) # -> (3+0j)


##########3   Decimal
print( (1.1 + 2.2) == 3.3)  #-> False

print(1.1 + 2.2)   # -> 3.3000000000000003 -> for this issue we use decimal module.

import decimal
print(0.1)   #-> 0.1
print(decimal.Decimal(0.1))   #-> 0.1000000000000000055511151231257827021181583404541015625

from decimal import Decimal as D
print(D('1.1') + D('2.2'))  #-> 3.3
print(D('1.2') * D('2.50'))  #-> 3.000


#### Fractions
import fractions

print(fractions.Fraction(1.5))  #-> 3/2
print(fractions.Fraction(5))   #-> 5
print(fractions.Fraction(1,3))  # -> 1/3

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))

from fractions import Fraction as F

print(F(1, 3) + F(1, 3))
print(1 / F(5, 6))
print(F(-3, 10) > 0)
print(F(-3, 10) < 0)

# 2/3
# 6/5
# False
# True


### math()
import math

print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))

# 3.141592653589793
# -1.0
# 22026.465794806718
# 3.0
# 1.1752011936438014
# 720


## random()

import random

print(random.randrange(10, 20))  # -> 19

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))   #-> c
# Shuffle x
random.shuffle(x)  #->  ['e', 'c', 'd', 'a', 'b']
# Print the shuffled x
print(x)
# Print random element
print(random.random())    #-> 0.4909693331323016



