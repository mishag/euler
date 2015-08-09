#!/usr/bin/python

import fractions
import sys

sys.setrecursionlimit(10000)

convergents = {}

def f(N):
    if N == 1:
        return fractions.Fraction(1, 2)

    res = fractions.Fraction(1, 2 + f(N - 1))
    convergents[N] = 1 + res
    return res

def sqrt2(N):
    return 1 + f(N)

if __name__ == "__main__":
    N = int(sys.argv[1])
    approx = sqrt2(N)
    print approx
    print float(approx)

    count = 0
    for key,frac in convergents.iteritems():
        print "%d\t%d\t%s" %(len(str(frac.numerator)), len(str(frac.denominator)), frac)
        if len(str(frac.numerator)) > len(str(frac.denominator)):
            count += 1
            
    print count
