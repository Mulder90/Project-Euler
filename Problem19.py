#!/usr/bin/python


import time
import calendar


def solve():
    count = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            first_day = calendar.weekday(year, month, 1)
            if first_day == 6:
                count += 1
    return count


if __name__ == '__main__':
    start_time = time.time()
    print "Result: {0}".format(solve())
    elapsed_time = time.time() - start_time
    print "Time elapsed: {0}".format(elapsed_time)
