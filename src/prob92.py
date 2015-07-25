#!/usr/bin/python

import sys

results = {}

def square_digit_sum(n):
    return sum([int(d)**2 for d in str(n)])


def get_terminus(n):
    
    if n in results:
        return results[n]

    temp = n

    while n != 89 and n != 1:
        n = square_digit_sum(n)

    results[temp] = n
    return n

if __name__ == "__main__":
    N = int(sys.argv[1])

    num_89s = 0

    for i in xrange(N, 0, -1):
        if get_terminus(i) == 89:
            num_89s += 1

    print num_89s
