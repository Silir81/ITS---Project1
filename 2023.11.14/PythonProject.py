import os.path

if __name__ == '__main__':
    filepath = "Database/newtxt.txt"
    print(os.path.isfile(filepath))
    file = open(filepath, "r")
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    print(file.readlines())
    print(file.read())
    file.close()