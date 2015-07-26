#!/usr/bin/python

import primes
import sys

ps = []
sieve = set([])

if __name__ == "__main__":

    N = int(sys.argv[1])
    
    for p in primes.primes():
        
        if p == 2:
            continue

        sieve.add(p)
        
        ps.append(p)
        for i, q in enumerate(ps[::-1]):
            sieve.add(q + 2*(i+1)*(i+1))

        if p > N:
            break

    sieve = sorted(sieve)
    max_in_sieve = max(sieve)

    # print sieve

    for odd in range(3, max_in_sieve, 2):
        if odd not in sieve:
            print odd
            break

