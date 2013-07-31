#!/usr/bin/python


import string
import time
import itertools


def create_ascii_dictionary():
	keys = [letter for letter in string.ascii_uppercase]
	values = [x for x in xrange(1, 27)]
	return dict(itertools.izip(keys, values))


d = create_ascii_dictionary()


def solve():
	with open("names.txt") as names:
		list_of_names = sorted([name[1:-1] for name in names.read().split(',')])
		i = 0
		for name in list_of_names:
			list_of_names[i] = sum(d[c] for c in name) * (i+1)
			i += 1
		return sum(list_of_names)
		

if __name__ == '__main__':
	start_time = time.time()
	print "Result: {0}".format(solve())
	elapsed_time = time.time() - start_time
	print "Elapsed time: {0}".format(elapsed_time)