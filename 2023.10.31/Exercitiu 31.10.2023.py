def using_loops(param_list: list):
    for a in list1:
        if str(type(a)) == "<class 'int'>":
            print(a)
        else:
            for b in a:
                if str(type(b)) == "<class 'int'>":
                    print(b)
                else:
                    for c in b:
                        print(c)
    # pass


def using_iterators(param_list: list):
    lista_mea = iter(list1)
    # if str(type()) == "<class 'int'>":
    print(next(lista_mea)) #index 0
    print(next(lista_mea))
    print(next(lista_mea))
    print(next(lista_mea))
    print(next(lista_mea))
    print(next(lista_mea))
    print(next(lista_mea))
    print(next(lista_mea))
    print(next(lista_mea))
    # print(next(lista_mea)) # index9
    var1 = next(lista_mea)

    for a in var1:
        print(a)
        for b in a:
            print(b)




def using_generators(param_list: list):
    for a in param_list:
        yield a
    # pass


if name == "main":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, [1, 2, 3], [[1, 2], [3, 4]]]

    # 1. Write a function that will iterate and print each element of the list, using:
    # - loops
    # - iterators
    # - generators
    using_loops(list1)
    using_iterators(list1)
    using_generators(list1)
    var2 = using_generators(list1)

    print(next(var2))
    print(next(var2))
    print(next(var2))
    print(next(var2))
    print(next(var2))
    print(next(var2))
    print(next(var2))
    print(next(var2))
    print(next(var2))
    for a in var2:
        print(a)
        for b in a:
            print(b)

    #2. Write another list using the "list

    # list2 = [element for element in list1 if isinstance(element, int) or isinstance(element, list)]
    # if str(type(el)) == "<class 'int'>" <=> is instance(el, int)
    list2 = [el for el in list1 if isinstance(el, int)]
    list3 = [el for el in list1 if isinstance(el, list)]
    list4 = [el for el in list3]
    print(list2)
    print(list3)
    print(list4)