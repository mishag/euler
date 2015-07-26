#!/usr/bin/python

import sys
import primes
import math

factors = {}

def num_distinct_prime_factors(n):
    upto = n/2
    num_factors = 0
    current_factors = set([])
    temp = n
    for p in primes.primes():
        if p > upto:
            break
        
        if n % p != 0:
            continue

        current_factors.add(p)
        if n in factors:
            current_factors = current_factors.union(factors[n])
            return len(current_factors), current_factors

        num_factors += 1

        n /= p

    if len(current_factors) == 0:
        current_factors.add(n)   # n is prime
        
    factors[temp] = current_factors
    return len(current_factors), current_factors

    
if __name__ == "__main__":
    M = int(sys.argv[1])

    results = set([])
    n = 0
    while True:
        n += 1
        
        if n % 1000 == 0:
            print "Completed %d" %n
            
        num_factors, current_factors = num_distinct_prime_factors(n)
        #print "%d ==> %d  %s" %(n, num_factors, current_factors)
        if num_factors == 4:
            results.add(n)

            if n-1 in results and n-2 in results and n-3 in results:
                print "%d, %d, %d, %d" %(n-3,n-2,n-1,n)
                exit(0)
