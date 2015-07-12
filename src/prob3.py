#!/usr/bin/python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import itertools
import math

N = 600851475143


# Credit to Cooking with Python:
# David Eppstein, Tim Peters, Alex Martelli, Wim Stolker, Kazuo Moriwaka, 
# Hallvard Furuseth, Pierre Denis, Tobias Klausmann, David Lees, 
# Raymond Hettinger
def primes():
    D = {  }  # map each composite integer to its first-found prime factor
    for q in itertools.count(2):     # q gets 2, 3, 4, 5, ... ad infinitum
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, so q is prime, therefore, yield it
            yield q
            # mark q squared as not-prime (with q as first-found prime factor)
            D[q*q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D:
                x += p
            D[x] = p

if __name__ == "__main__":
    limit = math.floor(math.sqrt(N))
    max = 0
    for prime in primes():
        if prime > limit:
            print max
            break
        if 0 == N % prime:
            max = prime

    exit(0)
