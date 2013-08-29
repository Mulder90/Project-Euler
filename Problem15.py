#!/usr/bin/python


import math
import utils

@utils.timeit
def lattice(n):
    return binomial_coefficient(n + n, n)


def binomial_coefficient(a, b):
    return math.factorial(a) // (math.factorial(a - b) * math.factorial(b))


if __name__ == '__main__':
   print("Result: {result}".format(result=lattice(20)))
