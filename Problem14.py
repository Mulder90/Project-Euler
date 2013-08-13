#!/usr/bin/python


import time
import operator

# memoization
cache = {}


def generate_next(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def count_sequence(n):
    count = 0
    start = n
    while generate_next(n) != 1:
        if n in cache:
            count += cache[n]
            break
        n = generate_next(n)
        count += 1
    cache[start] = count
    return count


def solve():
    max_index, max_value = max(enumerate((count_sequence(
        i) for i in range(1, 1000001)), start=1), key=operator.itemgetter(1))
    return max_index


if __name__ == "__main__":
    start_time = time.time()
    print("Result: {0}".format(solve()))
    elapsed_time = (time.time() - start_time)
    print("Found solution in {0}s".format(elapsed_time))
