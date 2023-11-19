import os.path

if __name__ == '__main__':
    filepath = "Database/newtxt.txt"
    file = open(filepath, "r")
    print("'Read' function\n", file.read())  # reads the entire file and returns its contents as a string.
    print("'ReadLine' Function \n", file.readline(-1))  # reads a single line from the file and returns it as a string
    print("ReadLine Function")
    print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    print("ReadLine \n", file.readline())  # reads a single line from the file and returns it as a string.
    print("'ReadLines' Function \n", file.readlines())  # reads all the lines of the file and returns them as a list
                                                             # of strings.
    print(file.readlines())
    print(file.read())
    file.close()
