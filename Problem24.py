#!/usr/bin/python


import utils


factoradic = {}


def gen_factoradic(n, k):
    for index in range(1, n + 1):
        pos = index
        factoradic_i = []
        for i in range(1, k + 1):
            factoradic_i.append(index % i)
            index //= i
        factoradic[pos] = factoradic_i[::-1]


@utils.timeit
def solve():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    gen_factoradic(1000000, len(digits))
    fact_rappresentation = factoradic[1000000 - 1]
    return "".join(str(digits.pop(i)) for i in fact_rappresentation)


if __name__ == "__main__":
    print("Result: {result}".format(result=solve()))
