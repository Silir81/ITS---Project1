import os.path


def check_file(file):
    """
    This function will check if you have a file in the specified location
    :param file: it should be the path to the file
    :return: It will return a confirmation print if is true, if not, you will get a print that tell you it's not a
    valid file there
    """
    #   Line 12, check if is a file in the path file
    file_checking = os.path.isfile(file)

    #   If is a file the first print confirm, if not the second text it's telling you that you don't have a file
    if file_checking is True:
        print("You have a valid file here !")
    else:
        print("You don't have the file here !")
    return


def read_only(for_file):
    """
    This function it's opening the file in read mode.
    :param for_file: it should be the path to the file that you want to read
    """

    #   First it's opening the file in "read" mode and tells you are in "read" mode, then, from line 30 close the file
    open_file = open(for_file, "r")
    print("You are in READING mode !")
    open_file.close()
    return


def read_and_write(which_file):
    """
    With this function, the file it's opened in read and write mode
    :param which_file: it should be the path to the file that you want to read or write in
    """

    #   First it's opening the file in "read" and "write" mode
    #   Then, it's telling you that, you are in "read" and "write" mode, then, from line 30 close the file
    open_file = open(which_file, "r+")
    print("You are in READING and WRITING mode !")
    open_file.close()
    return


def add_text_line(in_file):
    """
    With this function you can add a text line based on a user input
    :param in_file: Which is the file that you want to add the text line
    """

    #   Open the file in append and mode
    open_file = open(in_file, "a")

    #   Adding the paragraph from main, used "\n" to add the new line below of the actual text line
    #   Then, close the file
    open_file.writelines(my_string + "\n")
    open_file.close()

    #   Open it again, to add the user input in file
    open_file = open(in_file, "a")

    #   You can add the text that you want to have in file
    add_text = input("Add your line: ")

    #   The inputed text it's added in the file, used "\n" to start from begin with the text line, then, close the file
    add_line = open_file.writelines(add_text + "\n")
    open_file.close()

    #   To see the actual content of the file, the file needs to be opened again in "read" mode
    open_file = open(in_file, "r")

    #   Used .read() to read the text from file and then close the file
    print(open_file.read())
    open_file.close()
    return


def remove_file(file_to_remove):
    """
    Be careful with this function, it will delete the file form specified adress
    :param file_to_remove: The path to the file that you want to remove
    :type file_to_remove: String type
    :return: File from path deleted
    """

    ask_to_delete = input("Would you like to delete your file? ")

    if ask_to_delete == "yes":

        #   Remove the file if the user input it's "yes"
        os.remove(file_to_remove)

    else:
        print("Ok !")
    return


if __name__ == "__main__":

    my_string = ("The rain turned to snow. New skies dawned bright on the green pasture."
                 "My luck was about to turn for the better once I opened Word."
                 "My favorite TV show is big bang theory."
                 "Random text on line 4.")

    path_file = "Database/newFile.txt"

    file_name = "newFile.txt"

    print()
    check_file(path_file)
    print()
    read_only(path_file)
    print()
    read_and_write(path_file)
    print()
    add_text_line(path_file)
    print()
    remove_file(path_file)