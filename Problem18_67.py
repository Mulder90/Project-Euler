#!/usr/bin/python


import utils


"""To solve problem 18 you must change 'trinagle.txt' with 'problem18.txt'"""


@utils.timeit
def solve():
    with open("triangle.txt") as triangle:
        numbers = [[int(c) for c in line.split(" ")] for line in triangle]
        for i in range(len(numbers) - 2, -1, -1):
            for j in range(0, i + 1):
                numbers[i][j] += max(numbers[i + 1][j], numbers[i + 1][j + 1])
        return numbers[0][0]


if __name__ == '__main__':
    print("Result: {result}".format(result=solve()))
