def divide_two_numbers(a, b):
    print("entered the function")
    val = 0
    try:
        print("Try")
        val = a/b
    except ZeroDivisionError as error:
        print("in except")
        print("There was an error - a was divided by 0 - new value was given to val")
        print(error)
        val = -1
    else:
        print("in else")
        val = int(val)
    finally:
        print("in finally")
        return val

if "__main__" == __name__:
    print("The result of dividing {} to {} is {}".format(10, 0, divide_two_numbers(a=10, b=0)))
    print("The result of dividing {} to {} is {}".format(10, 5, divide_two_numbers(a=10, b=5)))
    list = [0, 1, 2, 3]