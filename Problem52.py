#!/usr/bin/env python


import time
import math


def digits(n):
    return sorted(str(n))


def solve():
    i = 1
    while True:
        if int(math.log10(i)) + 1 == int(math.log10(i * 6)) + 1:
            values = [digits(i * j) for j in range(2, 7)]
            if all([digits(i) == value for value in values]):
                return i
            else:
                i += 1
        else:
            i = int(str('1' + ('0' * (int(math.log10(i)) + 1))))


if __name__ == '__main__':
    start_time = time.time()
    print("Result: {0}".format(solve()))
    elapsed_time = time.time() - start_time
    print("Elapsed time: {0}".format(elapsed_time))
