"""
    String Methods

        1.  String capitalize() :- It converts the first character of a string to an uppercase letter and all other alphabets to lowercase.
                                   It returns a string with the first letter capitalized and all other characters in lowercase.
                                   e.g -> python is Love -> Python is love
        2. String center() :- method returns a new centered string after padding it with the specified character.
                              Syntax -: str.center(width, [fillchar]) -> width - length of the string with padded characters, fillchar (optional) - padding character.
                              Note: If fillchar is not provided, whitespace is taken as the default argument.

                              It returns a string padded with specified fillchar.


"""

sentence = "i love PYTHON"
# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()
print(capitalized_string)  # Output: I love python

# the sentence string is not modified.
print('Before capitalize():', sentence)  # Before capitalize(): i love PYTHON
print('After capitalize():', capitalized_string)  # After capitalize(): I love python