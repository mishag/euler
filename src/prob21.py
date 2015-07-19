#!/usr/bin/python

import sys

def get_proper_divisors(n):
    divisors = []
    for m in range(n/2):
        if n % (m+1) == 0 and n != m+1:
            divisors.append(m+1)

    return divisors


if __name__ == "__main__":
    N = int(sys.argv[1])

    amicables = set([])
    divisor_sums = {}
    for n in range(1,N,1):
        n_pair = sum(get_proper_divisors(n+1))
        divisor_sums[n+1] = n_pair
        divisor_sums[n_pair] = sum(get_proper_divisors(n_pair))

        if (divisor_sums[n+1] == n_pair and
            divisor_sums[n_pair] == n+1 and
            n_pair != n+1):
            amicables.add(n+1)
            amicables.add(n_pair)

    print amicables
    print sum(amicables)
    
