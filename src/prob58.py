#!/usr/bin/python

""" 
dakdjf 
1
3  5  7  9
13 17 21 25
31 37 43 49
"""

import itertools
import primes
import math

prime_generator = primes.primes()
prime_set       = set([])


def diag_seq():
    curr = 1
    yield curr
    for i in itertools.count(1):
        for j in range(4):
            curr += 2*i
            yield curr

def update_primes_upto(prime_gen, n):
    p = prime_gen.next()
    prime_set.add(p)
    while p <= n:
        p = prime_gen.next()
        prime_set.add(p)

    return p

if __name__ == "__main__":
    num_elems = 0
    num_primes = 0
    largest_prime = update_primes_upto(prime_generator, 100)
    

    for x in diag_seq():
        
        if x > largest_prime:
            largest_prime = update_primes_upto(prime_generator, x + 100)
            
        num_elems += 1
        if x in prime_set:
            num_primes += 1

        if 10 * num_primes < num_elems:
            print "num_primes ==> %d\nnum_elems ==> %d\nx ==> %d\ndim=%f" %(num_primes,
                                                                            num_elems,
                                                                            x,
                                                                            math.sqrt(x))
            break;

        if num_elems % 1000 == 0:
            print "num_primes ==> %d\nnum_elems ==> %d\nratio ==> %f\nx ==> %d\ndim=%f\n" %(num_primes,
                                                                                            num_elems,
                                                                                            float(num_primes)/float(num_elems),
                                                                                            x,
                                                                                            math.sqrt(x))
            

