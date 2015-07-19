#!/usr/bin/python

import primes
import sys

g_primes = set([])
circular_primes = set([])

def generate_cycles(n):    
    cycles = []
    num_str = str(n)
    for i in range(len(num_str)):
        num_str = num_str[1:] + num_str[0]
        m = int(num_str)
        cycles.append(m)

    return cycles

def build_prime_set(N):
    for p in primes.primes():
        
        if p >= N:
            break
        
        g_primes.add(p)

if __name__ == "__main__":
    N = int(sys.argv[1])

    build_prime_set(N)
    for i in range(N):
        cycles = generate_cycles(i)
        cycle_set = set(cycles)
        if cycle_set <= g_primes:
            circular_primes |= cycle_set

    print circular_primes
    print len(circular_primes)
    
