filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("1001 de nopti"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))


def my_example_of_a_short_function(my_name):
    do_exclaim = lambda s: s + '!'
    # print("do_exclaim():", do_exclaim("I am tired"))
    print(do_exclaim(my_name))

if __name__ == "__main__":
    my_example_of_a_short_function("Dan")