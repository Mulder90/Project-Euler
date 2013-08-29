#!/usr/bin/python


import utils


@utils.timeit
def solve(n):
    return str(sum(x ** x for x in range(1, n + 1)))[-10:]


if __name__ == '__main__':
    print("Result: {result}".format(result=solve(1000)))
