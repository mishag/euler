#!/usr/bin/python

""" 10001st prime """

import primes

if __name__ == "__main__":
    for i, p in enumerate(primes.primes()):
        if i == 10000:
            print p
            break
