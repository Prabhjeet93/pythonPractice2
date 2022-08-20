"""

    What is if...else statement in Python?
        Decision making is required when we want to execute a code only if a certain condition is satisfied.
        The if…elif…else statement is used in Python for decision making.

        Syntax :-
            if test expression:
                Body of if
            elif test expression:
                Body of elif
            else:
                Body of else

"""

num = 0.5
if num > 0:
    print("Positive number") #-> this will execute
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# nested if else if

#num = float(input("Enter a number: "))
num = 3.2
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number") #-> this will execute
else:
    print("Negative number")

