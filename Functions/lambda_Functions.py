"""
    What are lambda functions in Python?
        An anonymous function is a function that is defined without a name.
        While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
        Hence, anonymous functions are also called lambda functions.
        Lambda functions can be used wherever function objects are required.

        syntax -
            lambda arguments: expression
                it can have any number of arguments but only one expression.
        example -
            double = lambda x: x * 2
            print(double(5)) -> 10

    We generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
    Lambda functions are used along with built-in functions like filter(), map() etc.

    1. filter():
        The filter() function in Python takes in a function and a list as arguments.
        The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.

    2. map():
        The map() function in Python takes in a function and a list.
        The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

"""

# define lambda function.
# Rules:
#    1. use lambda keyword
#    2. Assign function to some variable and to store the output.
#    3. how to call -> call with variable name and pass paramenters in it.
#  This function has no name. It returns a function object which is assigned to the identifier
#  it is same as :
# def double(x):
#   return x * 2
double = lambda x: x * 2
print(double(5)) #-> 10


# Filter method in lambda function

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x : (x%2 ==0), my_list))

print(new_list)   #-> [4, 6, 8, 12]

# map() with lambda function

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)  #-> [2, 10, 8, 12, 16, 22, 6, 24]




