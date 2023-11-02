#Request: create a list, of 100 elements, where each element is a random number between 1 and 200
import random

list_of_randoms = []
for i in list(range(100)):
    # print(i)
    tempNumber = random.randint(1, 200)
    list_of_randoms.append(tempNumber)
    if (tempNumber % 2 == 0):
        print("I am an even number {}".format(tempNumber))
    else:
        pass
    # do nothing
#
# # Request: print only even numbers
# list_of_even_numbers = []
# for element in list_of_randoms:
#     if (element % 2 == 0):    # the rest of the division  by 2 operation will be compared with 0
#         list_of_even_numbers.append(element)
#     else:
#         pass
# print(list_of_even_numbers)

# Request: print only numbers that can be divided by 10
list_of_numbers_that_can_be_perfectly_divided_by_10 = []
for element in list_of_randoms:
    if (element % 10 == 0):     # the rest of the division  by 10 operation will be compared with 0
        list_of_numbers_that_can_be_perfectly_divided_by_10.append(element)
    else:
        pass
print(len(list_of_numbers_that_can_be_perfectly_divided_by_10))
