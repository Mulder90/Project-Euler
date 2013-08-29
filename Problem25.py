#!/usr/bin/python

import utils


@utils.timeit
def fibonacci():
    a, b = 0, 1
    count = 0
    while True:
        if(len(str(a))) == 1000:
            return (a, count)
        count += 1
        a, b = b, a + b


if __name__ == "__main__":
    print("Result: {result}".format(result=fibonacci()))
