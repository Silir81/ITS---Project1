
def name_age(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
# -----------------------------------------------------------


def my_fun(*argv):
    for arg in argv:
        print(arg)
# -----------------------------------------------------------


def my_fun2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
# -----------------------------------------------------------


def my_fun3(*argv, **kwargs):
    for arg in argv:
        print(arg)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
# -----------------------------------------------------------


def even_odd(x):
    """Function to check if the number is even or odd
    :param x = integer - number to check
    """
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


def short_function(x):
    """

    :param x:
    :return:
    """
    return x ** 2

# -----------------------------------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # name_age(33, "dan")
    # name_age(33, "Dan")
    # my_fun("Hello", "Welcome", "to", "Jungle", "is", "a", "song", "by", "Gun\'s\'Roses")
    # my_fun2(start_hour= "08:00", manual_break=True)
    # my_fun3("Hello", "Welcome", "to", "Jungle", firPassenger="Gale", secPassenger="Sidney")
    # print(even_odd.__doc__)
    # short_function = lambda x: x ** 2

    print(short_function(3))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def test(x,y):

