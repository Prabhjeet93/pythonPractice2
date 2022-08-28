"""
    CSV  - Comma Separated Values

        Methods -
        1. open() - This is for all types of file, to open the file.

        2. csv module - to deal with csv files

        3. csv.writer() -  This function returns a writer object that converts the user's data into a delimited string.
        4. writerow() - write into CSV files line by line
        5. writerows() - write into CSV files whole 2-D list

    Python csv.DictWriter() Class-
            The objects of csv.DictWriter() class can be used to write to a CSV file from a Python dictionary.
            syntax    - csv.DictWriter(file, fieldnames)
                       fieldnames -  a list object which should contain the column headers specifying the order in which data should be written in the CSV file

    Python csv.DictReader() Class
            The objects of a csv.DictReader() class can be used to read a CSV file as a dictionary.
            syntax - csv.DictReader(file, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)


    Using the Pandas library to Handle CSV files

            Pandas is a popular data science library in Python for data manipulation and analysis.
            If we are working with huge chunks of data, it's better to use pandas to handle CSV files for ease and efficiency.

            import pandas as pd

    CSV Files with Custom Delimiters - Delimeters can be |, "", \t, -:

            syntax - writer = csv.writer(file, delimiter='|')
                    reader = csv.reader(file, delimiter = '|')

    Dialects in CSV module -
            using two or more deimeter formats int he csv file.

"""

import csv

# writing the csv file line by line
with open('movies1.csv','w', newline='') as f:
    wr=csv.writer(f)
    wr.writerow(["SN", "Movie", "Protagonist"])
    wr.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    wr.writerow([2, "Harry Potter", "Harry Potter"])

f.close()

# read file
with open('movies1.csv', 'r') as file:
    rd = csv.reader(file)
    # reader = csv.reader(file, delimiter='\t')  # -> CSV file was using tab as a delimiter. To read such files, we can pass optional parameters to the csv.reader() function
    for row in rd:
        print(row)
file.close()
# ['SN', 'Movie', 'Protagonist']
# ['1', 'Lord of the Rings', 'Frodo Baggins']
# ['2', 'Harry Potter', 'Harry Potter']


# Writing multiple rows with writerows()
data = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]  # 2- D list

with open('movies2.csv','w') as fl:
    wr = csv.writer(fl)
    wr.writerows(data)
fl.close()

with open('movies2.csv', 'r') as file:
    rd = csv.reader(file)
    for row in rd:
        print(row)

# ['SN', 'Movie', 'Protagonist']
# []
# ['1', 'Lord of the Rings', 'Frodo Baggins']
# []
# ['2', 'Harry Potter', 'Harry Potter']
# []


###  : Writing to a CSV File with Tab Delimiter
with open('movies3.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '\t')
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])


# read file with tab delimeter
with open('movies3.csv', 'r') as fl:
    #rd = csv.reader(file)
    rd = csv.reader(fl, delimiter='\t')  # -> CSV file was using tab as a delimiter. To read such files, we can pass optional parameters to the csv.reader() function
    for row in rd:
        print(row)

# ['SN', 'Movie', 'Protagonist']
# []
# ['1', 'Lord of the Rings', 'Frodo Baggins']
# []
# ['2', 'Harry Potter', 'Harry Potter']
# []


###################################################
# csv file read and write as a dictionary

# write csv file
with open('people1.csv', 'w', newline='') as flo:
    column = ['player_name','fide_rating']
    wr = csv.DictWriter(flo,fieldnames=column)
    wr.writeheader()
    wr.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    wr.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    wr.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})

with open('people1.csv','r') as file:
    rd = csv.DictReader(file)
    print(rd)  # <csv.DictReader object at 0x545tr960>
    for row in rd:
        print(dict(row))
        print(row)

# {'player_name': 'Magnus Carlsen', 'fide_rating': '2870'}
# {'player_name': 'Fabiano Caruana', 'fide_rating': '2822'}
# {'player_name': 'Ding Liren', 'fide_rating': '2801'}


# ###########################################################################################3
## Using the Pandas library to Handle CSV files

import pandas as pd
# creating a data frame
df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])

# writing data frame to a CSV file
df.to_csv('person.csv')

# read csv file
rd = pd.read_csv("person.csv")
#print(rd)
#    Unnamed: 0  Name  Age
# 0           0  Jack   24
# 1           1  Rose   22

for row in rd:
    print(row)
# Unnamed: 0
# Name
# Age

####################################33
## CSV Files with Custom Delimiters - Delimeters can be |, "", \t,
data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)

# SN|Name|Contribution
# 1|Linus Torvalds|Linux Kernel
# 2|Tim Berners-Lee|World Wide Web
# 3|Guido van Rossum|Python Programming


with open('innovators.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '|')
    for row in reader:
        print(row)

# ['SN', 'Name', 'Contribution']
# ['1', 'Linus Torvalds', 'Linux Kernel']
# ['2', 'Tim Berners-Lee', 'World Wide Web']
# ['3', 'Guido van Rossum', 'Python Programming']


############################################33
## Dialects in CSV module

# write using dialects
row_list = [
    ["ID", "Name", "Email"],
    ["A878", "Alfonso K. Hamby", "alfonsokhamby@rhyta.com"],
    ["F854", "Susanne Briard", "susannebriard@armyspy.com"],
    ["E833", "Katja Mauer", "kmauer@jadoop.com"]
]
csv.register_dialect('myDialect',
                     delimiter='|',
                     quoting=csv.QUOTE_ALL)
with open('office.csv', 'w', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)

# "ID"|"Name"|"Email"
# "A878"|"Alfonso K. Hamby"|"alfonsokhamby@rhyta.com"
# "F854"|"Susanne Briard"|"susannebriard@armyspy.com"
# "E833"|"Katja Mauer"|"kmauer@jadoop.com"


### read using dialects
csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('office.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)

