"""
    JSON (JavaScript Object Notation) -
            is a popular data format used for representing structured data.
            It's common to transmit and receive data between a server and web application in JSON format.\
            JSON exists as a string.

            p = '{"name": "Bob", "languages": ["Python", "Java"]}'

            import json

        Writing JSON to a file -
                json.dump()  - to write json into a file.

        Read json
        1. Parse JSON in Python
            parse a JSON string using json.loads() method. The method returns a dictionary.
        2. Python Convert to JSON string
                convert a dictionary to JSON string using json.dumps() method

            Python	            JSON Equivalent
            dict	            object
            list,tuple	        array
            str	               string
            int,float,int   	number
                True	        true
                False	        false
                None	        null

        3. Python pretty print JSON
                    To analyze and debug JSON data, we may need to print it in a more readable format.
                    This can be done by passing additional parameters indent and sort_keys to json.dumps() and json.dump() method.



"""

## write json into a file


import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.txt','w') as file:
    json.dump(person_dict,file)

# {"name": "Bob", "languages": ["English", "French"], "married": true, "age": 32}


# Read above file
with open('person.txt','r') as f:
    data = json.load(f)

print(data)  # {'name': 'Bob', 'languages': ['English', 'French'], 'married': True, 'age': 32}


##################################33
# Parse JSON
# read json

# person is a JSON string,
person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])



###############################33
## Python Convert to JSON string
#  convert a dictionary to JSON string using json.dumps() method

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)



#############################
#  Python pretty print JSON

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))

# {
#     "languages": "English",
#     "name": "Bob",
#     "numbers": [
#         2,
#         1.6,
#         null
#     ]
# }


