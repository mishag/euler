#!/usr/bin/python

import sys

from fractions import Fraction

sys.setrecursionlimit(50000)

results = {}

def make_fracs(n):
    return [Fraction(1, d*d) for d in range(2, n + 1)]

def count_sums(res, fracs):
    if (res, tuple(fracs)) in results:
        return results[(res, tuple(fracs))]

    if res < 0 or sum(fracs) < res:
        return 0
    
    if res == 0 or sum(fracs) == res:
        return 1

    if len(fracs) == 0:
        return 0

    res = (count_sums(res - fracs[0], fracs[1:]) +
           count_sums(res, fracs[1:]))

    results[(res, tuple(fracs))] = res
    return res
    

if __name__ == "__main__":
    N = int(sys.argv[1])
    print count_sums(Fraction(1, 2), make_fracs(N))
