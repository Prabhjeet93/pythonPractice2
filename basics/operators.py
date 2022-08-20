"""
Operatord and operand:-
        Operators are special symbols in Python that carry out arithmetic or logical computation.
        The value that the operator operates on is called the operand.
        2+3   2,3 are operand,  + is operator

    1. Arithmetic operators:-
        + -> addtion, - -> subtraction, / -> division, % -> Modulus (remainder), * -> multiply
        // -> Floor division - division that results into whole number adjusted to the left in the number line
        ** -> exponent -> x**y -> x to the power of y

    2. Comparison operators :-
         Comparison operators are used to compare values. It returns either True or False according to the condition.
         >, <, ==,!=, >=, <=

    3.  Logical operator -:
                        and, or, not

    4. Bitwise operators -:
                Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
                For example, 2 is 10 in binary and 7 is 111.
                Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
                Operator	Meaning     	    Example
                    &	Bitwise AND	            x & y = 0 (0000 0000) -> of both are 1 thn 1 otherwise 0
                    |	Bitwise OR	            x | y = 14 (0000 1110) -> if both 0 then 0 otherwise 1
                    ~	Bitwise NOT	            ~x = -11 (1111 0101)  -> of 1 make it 0 and if 0 make it 1
                    ^	Bitwise XOR	            x ^ y = 14 (0000 1110) ->
                    >>	Bitwise right shift     x >> 2 = 2 (0000 0010) -> shifts all digit to right side by 2.
                    <<	Bitwise left shift	    x << 2 = 40 (0010 1000)  -> shifts all digit to left side by 2

    5. Assignment operators :-
        a=2, means assigning value 5 to the variable a in left.
        compound operators - > a+=2 it means a=a+2
        Operator	Example	    Equivalent to
            =	    x = 5	    x = 5
            +=	    x += 5	    x = x + 5
            -=	    x -= 5	    x = x - 5
            *=	    x *= 5	    x = x * 5
            /=	    x /= 5	    x = x / 5
            %=	    x %= 5	    x = x % 5
            //=	    x //= 5	    x = x // 5
            **=	    x **= 5	    x = x ** 5
            &=	    x &= 5	    x = x & 5
            |=	    x |= 5	    x = x | 5
            ^=	    x ^= 5	    x = x ^ 5
            >>=	    x >>= 5	    x = x >> 5
            <<=	    x <<= 5	    x = x << 5

    6. Special operators :- identity operator or the membership operator
        i). identity operators -> 'is',  'is not'
            Operator	    Meaning	                                                                    Example
            is	          True if the operands are identical (refer to the same object)	            x is True
            is not	      True if the operands are not identical (do not refer to the same object)	x is not True

        ii). Membership operators -> in, not in
            Operator	    Meaning                                             	Example
                in	        True if value/variable is found in the sequence     	5 in x
                not in	    True if value/variable is not found in the sequence	    5 not in x



"""

### 1. Arithmetic operators

x = 35
y = 3

# Output: x + y = 38
print('x + y =',x+y)

# Output: x - y = 32
print('x - y =',x-y)

# Output: x * y = 105
print('x * y =',x*y)

# Output: x / y = 11.6666666666
print('x / y =',x/y)

# Output: x // y = 11
print('x // y =',x//y)

# Output: x ** y = 42875
print('x ** y =',x**y)


## 2. Comparision operator

x = 5
y = 7

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)


## 3. Logical operator
x = True
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)


## Special operators
### a. Identity operators -> is, is not
x1 = 7
y1 = 7
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)
# x1 and y1 are integers of the same values, so they are equal as well as identical. Same is the case with x2 and y2 (strings).
# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)   # -> x3 and y3 are lists. They are equal but not identical. It is because the interpreter locates them separately in memory although they are equal.

## ii. Membership operators -> in, not in

x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x) # -> python is case sensitive

# Output: True
print(1 in y) #-> it checks only keys not values

# Output: False
print('a' in y) #-> it checks in only keys not values