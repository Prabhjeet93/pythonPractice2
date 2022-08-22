"""
    String Methods

        1.  String capitalize() :- It converts the first character of a string to an uppercase letter and all other alphabets to lowercase.
                                   It returns a string with the first letter capitalized and all other characters in lowercase.
                                   e.g -> python is Love -> Python is love
        2. String center() :- method returns a new centered string after padding it with the specified character.
                              Syntax -: str.center(width, [fillchar]) -> width - length of the string with padded characters, fillchar (optional) - padding character.
                              Note: If fillchar is not provided, whitespace is taken as the default argument.

                              It returns a string padded with specified fillchar.
                              The center() method doesn't modify the original string.

        3. String casefold() :- This method converts all characters of the string into lowercase letters and returns a new string.
        4. String count() :- This method returns the number of occurrences of a substring in the given string.
                             Syntax -> string.count(substring, start=..., end=...)
        5. String endswith():- This method returns True if a string ends with the specified suffix. If not, it returns False.
                              Syntax -> str.endswith(suffix[, start[, end]])
                              The endswith() method returns a boolean.
        6. String expandtabs():- The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
                                Syntax :- string.expandtabs(tabsize)

        7. String encode() :- This method returns an encoded version of the given string.
                            Syntax -: string.encode(encoding='UTF-8',errors='strict')
                            It returns an utf-8 encoded version of the string. In case of failure, it raises a UnicodeDecodeError exception.

        8. String find() :- This method returns the index of first occurrence of the substring (if found).
                            If not found, it returns -1.
                            Syntax -: str.find(sub[, start[, end]] )
             rfind() :- This method returns the index of first occurrence of the substring (if found) from last.
                        similar to find but search from last.

        9. String format():- This method formats the given string into a nicer output in Python.
        10. String index():- This  method returns the index of a substring inside the string (if found).
                            If the substring is not found, it raises an exception.(it raises a ValueError exception.)
                            syntax -: str.index(sub[, start[, end]] )
        11. String isalnum() -: This method returns True if all characters in the string are alphanumeric (either alphabets or numbers).
                                    If not, it returns False.
        12. String isalpha():- This method returns True if all characters in the string are alphabets. If not, it returns False.
        13. String isdecimal():- This method returns True if all characters in a string are decimal characters. If not, it returns False.
        14. String isdigit():- Ths method returns True if all characters in a string are digits. If not, it returns False.
        15. String isidentifier():- This method returns True if the string is a valid identifier in Python. If not, it returns False.
        16. String islower():- This method returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
        17. String isupper():- This method returns whether or not all characters in a string are uppercased or not.
        18. String isnumeric():- This method checks if all the characters in the string are numeric.
        19. String join() :- This string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.
                        Syntax - string.join(iterable)   -> iterable objects - List, Tuple, String, Dictionary and Set.
                        The join() method provides a flexible way to create strings from iterable objects.
                        It joins each element of an iterable (such as list, string, and tuple) by a string separator (the string on which the join() method is called) and returns the concatenated string.

                        If the iterable contains any non-string values, it raises a TypeError exception.







"""

## 1. capitalize()
sentence = "i love PYTHON"
# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()
print(capitalized_string)  # Output: I love python

# the sentence string is not modified.
print('Before capitalize():', sentence)  # Before capitalize(): i love PYTHON
print('After capitalize():', capitalized_string)  # After capitalize(): I love python

## 2. center()
sentence = "Python is awesome"

# returns the centered padded string of length 24
new_string = sentence.center(24, '*')
print(new_string)
# Output: ***Python is awesome****

#center() with Default Argument
text = "Python is awesome"
# returns padded string by adding whitespace up to length 24
new_text = text.center(24)
print("Centered String: ", new_text)   # Centered String:     Python is awesome


## 3. String casefold() :- This method converts all characters of the string into lowercase letters and returns a new string.
# The casefold() method is similar to the lower() method but it is more aggressive. This means the casefold() method converts more characters into lower case compared to lower() .

text = "PYTHON IS FUN"

# converts text to lowercase
print(text.casefold())  #-> python is fun

text = 'groß'

# convert text to lowercase using casefold()
print('Using casefold():', text.casefold())  # Using casefold(): gross

# convert text to lowercase using lower()
print('Using lower():', text.lower())  # Using lower(): groß


### 4. count() :- This method returns the number of occurrences of a substring in the given string.
message = 'python is popular programming language'

# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('p'))   # Output: Number of occurrence of p: 4
# define string
string = "Python is awesome, isn't it?"
substring = "i"
# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)
# print count
print("The count is:", count) # The count is: 1


# define string
string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
# print count
print("The count is:", count)  # The count is 2


###  5. endswith()
text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)
result = text.endswith('to learn.')
# returns True
print(result)
result = text.endswith('Python is easy to learn.')
# returns True
print(result)

text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)
# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched
result = text.endswith('is', 7, 26)
# Returns False
print(result)
result = text.endswith('easy', 7, 26)
# returns True
print(result)

##  endswith() With Tuple Suffix
text = "programming is easy"
result = text.endswith(('programming', 'python'))
# prints False
print(result)
result = text.endswith(('python', 'easy', 'java'))
#prints True
print(result)
# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)
# prints True
print(result)


## 7.  String encode() :- This method returns an encoded version of the given string.

title = 'Python Programming'
# change encoding to utf-8
print(title.encode())   # Output: b'Python Programming'

# unicode string
string = 'pythön!'
# print string
print('The string is:', string)  # The string is: pythön!
# default encoding to utf-8
string_utf = string.encode()
# print result
print('The encoded version is:', string_utf)   # The encoded version is: b'pyth\xc3\xb6n!'

# unicode string
string = 'pythön!'
# print string
print('The string is:', string)
# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))  # The encoded version (with ignore) is: b'pythn!'
# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))   # The encoded version (with replace) is: b'pyth?n!

### 8. String find()

message = 'Python is a fun programming language'
# check the index of 'fun'
print(message.find('fun')) # Output: 12

print(message.rfind('e'))  # Output: 35

quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))   # -1
# Substring is searched in ' small things with great love'
print(quote.find('small things', 2))   # 3
# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))  # -1
# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))   # 9



# 9. format()

# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))   # Hello Adam, your balance is 230.2346.
# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))  # Hello Adam, your balance is 230.2346.
# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))  # Hello Adam, your balance is 230.2346.
# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))   # Hello Adam, your balance is 230.2346.


### index()

sentence = 'Python programming is fun.'
result = sentence.index('is fun')
print("Substring 'is fun':", result)  # Substring 'is fun': 19
#result = sentence.index('Java')
#print("Substring 'Java':", result)   # ValueError: substring not found


# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10)) #15
# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))   # 17
# Substring is searched in 'programming'
#print(sentence.index('fun', 7, 18))    # ValueError: substring not found

### isalnum()

# contains either numeric or alphabet
string1 = "M234onica"
print(string1.isalnum()) # True
# contains whitespace
string2 = "M3onica Gell22er"
print(string2.isalnum()) # False
# contains non-alphanumeric character
string3 = "@Monica!"
print(string3.isalnum()) # False

# #### isalpha()

name = "Monica"
print(name.isalpha())  # True
# contains whitespace
name = "Monica Geller"
print(name.isalpha())   # False
# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())   # False


### isdecimal()

s = "28212"
print(s.isdecimal())  # True
# contains alphabets
s = "32ladk3"
print(s.isdecimal())   # False
# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())  #False


## isidentifier()
str = 'Python'
print(str.isidentifier())  # True
str = 'Py thon'
print(str.isidentifier())   # False
str = '22Python'
print(str.isidentifier())   # False
str = ''
print(str.isidentifier())    # False

### join()

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))  # Output: Python is a fun programming language

###  String join() :- This string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))   # Output: Python is a fun programming language

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))  ## 1, 2, 3, 4

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))   ## 1, 2, 3, 4

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))    # s1.join(s2): 1abc2abc3

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))   # s2.join(s1): a123b123c


