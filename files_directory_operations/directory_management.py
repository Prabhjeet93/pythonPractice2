"""
    Python Directory:
            A directory or folder is a collection of files and subdirectories.
            Python has the os module that provides us with many useful methods to work with directories (and files as well).

        1. Get Current Directory
                We can get the present working directory using the getcwd() method of the os module.
                This method returns the current working directory in the form of a string.
                We can also use the getcwdb() method to get it as bytes object.

        2. Changing Directory: chdir()
                    os.chdir('C:\\Python33')

        3. List Directories and Files: listdir()
                    print(os.listdir())
                    print(os.listdir('C:\\))

        4. Making a New Directory : mkdir()
                    os.mkdir('test')

        5. Renaming a Directory or a File :- rename()
                    os.rename('test','new_one')

        6. Removing Directory or File:
                   os.remove() -  A file can be removed (deleted) using the remove() method.
                   os.rmdir() - the rmdir() method removes an empty directory.
                   shutil.rmtree() - method removes an non-empty directory.




"""

import os
print(os.getcwd())   # C:\pythonPractice2\files_directory_operations
print(os.getcwdb())  # b'C:\pythonPractice2\files_directory_operations'

#Changing Directory: chdir()
os.chdir('C:\\data')
print(os.getcwd())  #C:\data

# List Directories and Files: listdir()
# if path not provided then current directory's data
print(os.listdir())   # [Doc, lib, 'output.csv', 'output1.csv', 'output4.csv']

# if path is provided.
print(os.listdir('C:\\'))

# Making a New Directory:-   mkdir()
os.mkdir('test2')
print(os.listdir())  # ['output.csv', 'output1.csv', 'output4.csv', 'test', 'test1']

# Renaming a Directory or a File :- rename()
#os.rename('test','new_one')
print(os.listdir())  # ['new_one', 'output.csv', 'output1.csv', 'output4.csv', 'test1', 'test2']


# Removing Directory or File:

# 1. removing empty directory
os.rmdir('test')

# 2. creating a file in the directory to make it non empty and then deleting it.
os.chdir('C:\\data\\test1')
print(os.getcwd())
print(os.listdir())
with open('read.txt','w') as f:
    f.write("Created new file")
print(os.listdir())  # ['read.txt']
os.chdir('C:\\data')
# os.rmdir('test1')  # OSError: [WinError 145] The directory is not empty: 'test1' -> getting error for non empty directory
print(os.listdir())   # ['new_one', 'output.csv', 'output1.csv', 'output4.csv', 'test1', 'test2']

import shutil
shutil.rmtree('test1')
print(os.listdir())   # ['new_one', 'output.csv', 'output1.csv', 'output4.csv', 'test2'] -> test1 removed which is an non empty directory.


### 3. Creating a file in current directory and then deleting it with remove()
with open('read1.txt','w') as f:
    f.write("Created new file")

print(os.listdir())  # ['new_one', 'output.csv', 'output1.csv', 'output4.csv', 'read1.txt', 'test2']
os.remove('read1.txt')
print(os.listdir())  # ['new_one', 'output.csv', 'output1.csv', 'output4.csv', 'test2']


