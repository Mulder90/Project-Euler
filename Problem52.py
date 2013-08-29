#!/usr/bin/env python


import itertools
import utils
import math

def digits(n):
    return sorted(str(n))


@utils.timeit
def solve():
    for i in itertools.count(1):
        len_number_i = int(math.log10(i)) + 1
        if len_number_i == int(math.log10(i * 6)) + 1:
            values = [digits(i * j) for j in range(2, 7)]
            digit_i = digits(i)
            if all([digit_i == value for value in values]):
                return i
        else:
            i = int(str('1' + ('0' * len_number_i)))


if __name__ == '__main__':
    print("Result: {result}".format(result=solve()))
