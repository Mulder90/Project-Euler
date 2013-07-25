#!/usr/bin/python


import math


def lattice(n):
	return binomialCoefficient(n + n, n)

def binomialCoefficient(a, b):
	return math.factorial(a)/(math.factorial(a - b)*math.factorial(b))


if __name__ == '__main__':
    print lattice(20)