def get_length(param_string):
    """
    Description: THis function will return the length of the param_string
    :param param_string: String to be measured
    :return: length of string
    """
    return len(param_string)


def get_no_of_words(param_string):
    """
    Description: This function will count the words from the parameter
    :param param_string: Words to be counted
    :return: Number of words
    """
    return len(param_string.split())


if __name__ == "__main__":
    String1 = "I am writing something that I will probably use later on"
    print("The length of String1 is: " + str(get_length(String1)))
    print("The number of words in the string is: " + str(get_no_of_words(String1)))

    # Imparte string-ul in cuvinte
    words = String1.split()

    # Sterge al 2-lea si al 3-lea cuvant (Index 1 si index 2)
    del words[1:3]

    # Join the remaining words back into a string
    result = ' '.join(words)

    # Afiseaza rezultatul
    print(result)