"""
    What is while loop in Python?
        The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
        we use this loop when we dont know the number of iterations.
        Syntax:-
            while test_expression:
                Body of while
        Python interprets any non-zero value as True. None and 0 are interpreted as False.
        While loop with else :
            The else part is executed if the condition in the while loop evaluates to False.
        The while loop can be terminated with a break statement.
        In such cases, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.
"""

n=10
sum=0
i=1
while i<=n:
    sum = sum+i
    i=i+1
print("the sum is",sum)   # -> the sum is :  55

## While loop with else :
# The else part is executed if the condition in the while loop evaluates to False.

counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter+1
else:
    print("Inside else")

# Inside loop
# Inside loop
# Inside loop
# Inside else


