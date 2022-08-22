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
