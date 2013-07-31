#!/usr/bin/python


import time


def generate_next(n):
    if n%2==0:
        return n/2
    else:
        return 3*n + 1


def count_sequence(n):
    count = 0
    while generate_next(n) != 1:
        n = generate_next(n)
        count += 1
    return count

    
def solve():
    length = 0
    result = 0
    for i in xrange(1, 1000000):
        tmp = count_sequence(i)
        if tmp > length:
        	length, result = tmp, i
    return result


if __name__ == "__main__":
    start_time = time.time()
    print solve()
    elapsed_time = (time.time() - start_time)
    print "Found solution in {0}s".format(elapsed_time)
