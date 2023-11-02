
def convert_string_number_to_integer(number_as_string):
    string_to_analyze = number_as_string
    hundreds_no = ""
    hundreds_rest = ""
    tens_no = ""
    tens_rest = ""
    digits = ""
    number_to_return = 0
    if "sut" in string_to_analyze:
        hundreds_no = str(number_as_string.split("sut")[0]).strip()
        hundreds_rest = str(number_as_string.split("sut")[1])[1:].strip()
        string_to_analyze = hundreds_rest
    else:
        print("No Hundreds")
    if "spr" in string_to_analyze:
        tens_no = "unu"
        digits = str(string_to_analyze.split("spr")[0]).strip()
    elif "zec" in string_to_analyze:
        if "zece" == string_to_analyze:
            tens_no = "unu"
        else:
            tens_no = string_to_analyze.split("zec")[0].strip()
            tens_rest = str(string_to_analyze.split("zec")[1])[1:].strip()
            string_to_analyze = tens_rest
            if "si" in string_to_analyze:
                digits = string_to_analyze.split("si")[1].strip()
            else:
                print("No digits")
    else:
        print("No Tens")
        if string_to_analyze != "":
            digits = string_to_analyze
        else:
            print("No digits")

    print("hundreds: " + hundreds_no)
    temp = 100 * convert_string_number_to_integer_only_digits(hundreds_no)
    print("tens: " + tens_no)
    temp = temp + 10 * convert_string_number_to_integer_only_digits(tens_no)
    print("digits: " + digits)
    temp = temp + convert_string_number_to_integer_only_digits(digits)
    print(temp)


def convert_string_number_to_integer_only_digits(number_as_string):
    basic_number_db = {
        "zero": 0, 'o': 1, 'unu': 1, "un": 1,
        'doi': 2, 'doua': 2,
        'trei': 3,
        'patru': 4, 'pai': 4,
        'cinci': 5,
        'sase': 6, 'sai': 6,
        'sapte': 7,
        'opt': 8,
        'noua': 9,
        'zece': 10
    }
    # identify digits
    if number_as_string in list(basic_number_db.keys()):
        return basic_number_db[number_as_string]
    else:
        print("Character not recognized")
        return 0


if __name__ == "__main__":
    user_input = input("Please enter your number as string, in Romanian ")
    convert_string_number_to_integer(user_input)
