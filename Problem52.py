#!/usr/bin/env python


import itertools
import time
import math


def digits(n):
    return sorted(str(n))


def solve():
    for i in itertools.count(1):
        len_number = int(math.log10(i)) + 1
        if len_number == int(math.log10(i * 6)) + 1:
            values = [digits(i * j) for j in range(2, 7)]
            if all([digits(i) == value for value in values]):
                return i
        else:
            i = int(str('1' + ('0' * len_number)))


if __name__ == '__main__':
    start_time = time.time()
    print("Result: {result}".format(result=solve()))
    elapsed_time = time.time() - start_time
    print("Elapsed time: {time}".format(time=elapsed_time))
