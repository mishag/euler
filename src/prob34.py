#!/usr/bin/python

import math

MAX_NUMBER = 10000000

def sum_of_factorials_of_digits(n):
    return sum([math.factorial(int(d)) for d in str(n)])

if __name__ == "__main__":
    res = []
    for n in xrange(1, MAX_NUMBER, 1):
        if sum_of_factorials_of_digits(n) == n:
            res.append(n)
            print n

    print "%s ==> %d" %(res, sum(res))
