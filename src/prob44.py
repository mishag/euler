#!/usr/bin/python

import math
import sys

def P(i):
    return i * (3*i - 1) / 2

def is_pentagonal(n):
    radicand = 1 + 24*n
    root = int(math.sqrt(1 + 24*n))
    if root*root != radicand:
        return False

    return (1 + root) % 6 == 0

if __name__ == "__main__":
    results = {}
    N = int(sys.argv[1])
    for i in range(1, N):
        Pi = P(i)
        for j in range(i+1, N):
            Pj = P(j)
            diff = abs(Pi - Pj)
            if is_pentagonal(Pi + Pj) and is_pentagonal(diff):
                results[(i, j)] = diff

    print results
