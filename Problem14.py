#!/usr/bin/python


import time

def generateNext(n):
    if n%2==0:
        return n/2
    else:
        return 3*n + 1
    
def countSequence(n):
    count = 0
    while generateNext(n) != 1:
        n = generateNext(n)
        count += 1
    return count
    
def solve():
    length = 0
    result = 0
    for i in xrange(1, 1000000):
        tmp = countSequence(i)
        if tmp > length:
            length = tmp
            result = i
    return result

if __name__ == "__main__":
    startTime = time.time()
    print solve()
    elapsedTime = (time.time() - startTime)
    print "Found solution in {0}s".format(elapsedTime)
