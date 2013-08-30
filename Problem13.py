#!/usr/bin/python


import utils


@utils.timeit
def solve():
    return str(sum(int(x) for x in open("problem13.txt", "r")))[0:10]


if __name__ == "__main__":
    print("Result: {result}".format(result=solve()))
