#!/usr/bin/python

import sys
import primes

pset = set([])

def f(a, b, n):
    return n*n + a*n + b

def generate_primes(max_prime):
    for p in primes.primes():
        if p > max_prime:
            break
        pset.add(p)
        
def find_seq_len(a, b):
    n = 0
    while True:
        if f(a, b, n) not in pset:
            return n
        n += 1
        
if __name__ == "__main__":
    M = int(sys.argv[1])
    max_seq_len = 0
    max_a = 0
    max_b = 0
    generate_primes(100*100 + 100*M + M)
    for a in range(-M + 1, M):
        for b in primes.primes():
            if b >= M:
                break
            
            seq_len = find_seq_len(a, b)
            if seq_len > max_seq_len:
                max_seq_len = seq_len
                max_a = a
                max_b = b

    print "(%d, %d, %d) ==> %d" %(max_a, max_b, max_a * max_b, max_seq_len)
    
