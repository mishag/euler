#!/usr/bin/python

import sys

def reciprocal(n):
    r = 1
    while r:
        r *= 10
        if 0 == r / n:
            yield 0
            continue

        yield r / n
        r = r % n
    

if __name__ == "__main__":
    n = int(sys.argv[1])
    for i, d in enumerate(reciprocal(n)):
        print  d,
        if i > 1000:
            break

    exit(0)
