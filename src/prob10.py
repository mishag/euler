#!/usr/bin/python

import primes
import itertools

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

if __name__ == "__main__":
    print sum([x for x in itertools.takewhile(lambda x: x < 2000000, 
                                              primes.primes())])
