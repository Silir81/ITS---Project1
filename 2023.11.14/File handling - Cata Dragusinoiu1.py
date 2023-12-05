

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