#!/usr/bin/python


import time


def solve():
    somma = 0
    with open("problem13.txt") as text:
        for line in text:
            somma += int(line) 
    return str(somma)[:10]
    
def solveBetter():
    return str(sum(int(x) for x in open("problem13.txt", "r")))[0:10]
    
if __name__ == "__main__":
	startTime = time.time()
	print solveBetter()
	elapsedTime = time.time() - startTime
	print "Elapsed time: {0}".format(elapsedTime)