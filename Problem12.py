#!/usr/bin/python


import time


def number_of_divisor(n):
    return len(sum([[x, (n // x)] for x in range(1, (int((n ** 0.5) + 1))) if not (n % x)], []))


def solver(n):
    x = 2
    while number_of_divisor(gen_triangle(x)) < n:
        x += 1
    return gen_triangle(x)


def gen_triangle(n):
    return ((n * (n + 1)) // 2)


if __name__ == "__main__":
    start_time = time.time()
    print(solver(500))
    elapsed_time = time.time() - start_time
    print("Elapsed time: {time}".format(time=elapsed_time))
