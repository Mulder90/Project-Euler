#!/usr/bin/python


import string
import utils


def create_ascii_dictionary():
    keys = [letter for letter in string.ascii_uppercase]
    values = [x for x in range(1, 27)]
    return dict(zip(keys, values))


d = create_ascii_dictionary()


@utils.timeit
def solve():
    with open("names.txt") as names:
        list_of_names = sorted([name[1:-1]
                               for name in names.read().split(',')])
        i = 0
        for name in list_of_names:
            list_of_names[i] = sum(d[c] for c in name) * (i + 1)
            i += 1
        return sum(list_of_names)


if __name__ == '__main__':
    print("Result: {result}".format(result=solve()))
