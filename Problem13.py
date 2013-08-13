#!/usr/bin/python


import time


def solve():
    return str(sum(int(x) for x in open("problem13.txt", "r")))[0:10]


if __name__ == "__main__":
    start_time = time.time()
    print(solve())
    elapsed_time = time.time() - start_time
    print("Elapsed time: {0}".format(elapsed_time))
