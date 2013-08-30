#!/usr/bin/python

import utils


@utils.timeit
def factorial(n):
    result = 1
    while n != 1:
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    print("Result: {result}".format(result=sum(int(x)
          for x in str(factorial(100)))))
