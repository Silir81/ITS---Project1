import os.path

if __name__ == '__main__':
    filepath = "Database/newtxt.txt"
    # print(os.path.isfile(filepath))
    file = open(filepath, "r")
    # file.seek(0)
    # print("'Read' function\n", file.read())  # reads the entire file and returns its contents as a string.
    # file.seek(0)
    # print("'ReadLine' Function \n", file.readline(-1))  # reads a single line from the file and returns it as a string
    print("ReadLine Function")
    for x in file:
        print(x)
    # print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    # print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    # print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    # print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    # print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    # print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    # file.seek(0)
    # print("'ReadLines' Function \n", file.readlines())  # reads all the lines of the file and returns them as a list
    # # of strings.
    print(file.readlines())
    # print(file.read())
    file.close()

# os.path.isfile(filepath): This checks whether the file at the given filepath exists.
# It returns True if the file exists and False otherwise. It prints the result.

# file = open(filepath, "r"): Opens the file in read mode.

# file.read(): Reads the entire content of the file as a string and prints it.

# file.readline(3): Reads the first 3 characters of the current line in the file and prints them as a string.
# It doesn't read the entire line, just the specified number of characters.

# file.readlines(): Reads all the lines of the file and returns them as a list of strings.
# This will read from the current file position (which will be at the end of the file if file.read() was called before).
#
# Note: Each time file.read(), file.readline(), or file.readlines() is called,
    # it moves the file cursor to the end of the read content.
# So, if you call file.read() first, subsequent calls to file.readline() or file.readlines()
    # may not read the content you expect because the cursor will be at the end of the file.
# You may want to either re-open the file or use file.seek(0) to reset the file pointer to the beginning.
