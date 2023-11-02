def print_a_var():
    if x == 15:
        print(x)


def modify_a_var():
    global x
    x = 20
    print(x)


if __name__ == "__main__":
    x = 15
    print(x)
    print_a_var()
    print(x)
    modify_a_var()
    print(x)
