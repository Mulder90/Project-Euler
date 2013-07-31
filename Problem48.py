#!/usr/bin/python


import time


def solve(n):
    return str(sum(x ** x for x in xrange(1, n + 1)))[-10:]


if __name__ == '__main__':
    start_time = time.time()
    print "Result: {0}".format(solve(1000))
    elapsed_time = time.time() - start_time
    print "Elapsed time: {0}".format(elapsed_time)
