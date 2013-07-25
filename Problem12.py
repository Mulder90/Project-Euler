#!/usr/bin/python


import time

        
def numberOfDivisor(n):
    return len(sum([[x, (n/x)] for x in xrange(1, (int((n**0.5) + 1))) if not (n%x)], []))

def solver(n):
    x = 2
    while numberOfDivisor(genTriangle(x)) < n:
        x += 1
    return genTriangle(x)

def genTriangle(n):
    return ((n*(n+1))/2)

        
if __name__ == "__main__":
	startTime = time.time()
	print solver(500)
	elapsedTime = time.time() - startTime
	print "Elapsed time: {0}".format(elapsedTime)


