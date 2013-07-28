#!/usr/bin/python


import string
import time


def createAsciiDictionary():
	keys = [letter for letter in string.ascii_uppercase]
	value = [x for x in xrange(1, 27)]
	return dict(zip(keys, value))

d = createAsciiDictionary()

def solve():
	with open("names.txt") as names:
		listOfNames = sorted([name[1:-1] for name in names.read().split(',')])
		i = 0
		for name in listOfNames:
			listOfNames[i] = sum(d[c] for c in name) * (i+1)
			i += 1
		return sum(listOfNames)
		

if __name__ == '__main__':
	startTime = time.time()
	print "Result: {0}".format(solve())
	elapsedTime = time.time() - startTime
	print "Elapsed time: {0}".format(elapsedTime)