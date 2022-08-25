"""

    Files -
        In Python, a file operation takes place in the following order:

            1. Open a file
            2. Read or write (perform operation)
            3. Close the file

            1. open() -> This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.
                    We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.
                    The default is reading in text mode. In this mode, we get strings when reading from the file.
                    On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

                      Mode	Description
                        r	Opens a file for reading. (default)
                        w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
                        x	Opens a file for exclusive creation. If the file already exists, the operation fails.
                        a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
                        t	Opens in text mode. (default)
                        b	Opens in binary mode.
                        +	Opens a file for updating (reading and writing)

                    the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux. So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

            2. Closing Files - close()
                        Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.
                        Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.
                        This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.
                            A safer way is to use a try...finally block.

                with statment - This ensures that the file is closed when the block inside the with statement is exited.
                                We don't need to explicitly call the close() method. It is done internally.
                        with open("test.txt", encoding = 'utf-8') as f:
                            f.write("my first file\n")


            3. Writing to Files: write()
                        In order to write into a file in Python, we need to open it in write w,
                        append a or exclusive creation x mode.
                        We need to be careful with the w mode, as it will overwrite into the file if it already exists.
                            Due to this, all the previous data are erased.
                        Writing a string or sequence of bytes (for binary files) is done using the write() method.
                            This method returns the number of characters written to the file.

        read() - Reading Files in Python:
                    To read a file in Python, we must open the file in reading r mode.
                    There are various methods available for this purpose. We can use the read(size) method to read in the size number of data.
                    If the size parameter is not specified, it reads and returns up to the end of the file.

                We can read a file line-by-line using a for loop. This is both efficient and fast.

        seek() - We can change our current file cursor (position) using the seek() method
        tell() - This method returns our current position (in number of bytes).
        readline() -  method to read individual lines of a file. This method reads a file till the newline, including the newline character.

            Method	        Description
            close() 	    Closes an opened file. It has no effect if the file is already closed.
            detach()	    Separates the underlying binary buffer from the TextIOBase and returns it.
            fileno()	    Returns an integer number (file descriptor) of the file.
            flush() 	    Flushes the write buffer of the file stream.
            isatty()	    Returns True if the file stream is interactive.
            read(n)	         Reads at most n characters from the file. Reads till end of file if it is negative or None.
            readable()	    Returns True if the file stream can be read from.
            readline(n=-1)	Reads and returns one line from the file. Reads in at most n bytes if specified.
            readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
            seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end).
            seekable()	        Returns True if the file stream supports random access.
            tell()	             Returns an integer that represents the current position of the file's object.
            truncate(size=None)	Resizes the file stream to size bytes. If size is not specified, resizes to current location.
            writable()  	    Returns True if the file stream can be written to.
            write(s)	        Writes the string s to the file and returns the number of characters written.
            writelines(lines)	Writes a list of lines to the file.

"""
#
# # Open a file
# f = open("test.txt")    # open file in current directory
# #f = open("C:/Python38/README.txt")  # specifying full path
#
# # open file with modes
# f = open("test.txt")      # equivalent to 'r' or 'rt'
# f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode
#
# # the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.
# # Hence, when working with files in text mode, it is highly recommended to specify the encoding type.
# f = open("test.txt", mode='r', encoding='utf-8')
#
#
# # Closing Files
# f = open("test.txt", encoding = 'utf-8')
# # perform file operations
# f.close()
#
# # This method is not entirely safe.
# # If an exception occurs when we are performing some operation with the file, the code exits without closing the file.
# # A safer way is to use a try...finally block.
# try:
#    f = open("test.txt", encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()
#
# # with statement
# with open("test.txt", encoding = 'utf-8') as f:
#     pass
# # perform file operations

# write in to file - it will create new file if not exist and thn write into it.
with open("test2.txt", 'w', encoding='utf-8') as f:
    f.write("my first file to \n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

# reading the files in python
f = open("test.txt",'r',encoding = 'utf-8')
#print(f.read(4))    # read the first 4 data   -> my f
#print(f.read(4))    # read the next 4 data   -> irst
print(f.read())     # read in the rest till end of file    'my first file\nThis file\ncontains three lines\n'
# my first file
# This file
#
# contains three lines

print(f.read())  # further reading returns empty sting  ''

# seek() and tell()
print(f.tell())    # get the current file position  -> 50
print(f.seek(0))   # bring file cursor to initial position  -> 0

for line in f:
    print(line, end = '')

# my first file
# This file
#
# contains three lines

p=open('test2.txt', encoding='utf-8')
print(p.readline())  # my first file to
print(p.readline())  # This file
print(p.readline())  # ''

print(p.readlines())