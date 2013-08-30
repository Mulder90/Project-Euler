#!/usr/bin/python


import utils
import calendar


@utils.timeit
def solve():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            first_day = calendar.weekday(year, month, 1)
            if first_day == 6:
                count += 1
    return count


if __name__ == '__main__':
    print("Result: {result}".format(result=solve()))
