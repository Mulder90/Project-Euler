#!/usr/bin/python


import math


def lattice(n):
	return binomial_coefficient(n + n, n)


def binomial_coefficient(a, b):
	return math.factorial(a)/(math.factorial(a - b)*math.factorial(b))


if __name__ == '__main__':
    print lattice(20)