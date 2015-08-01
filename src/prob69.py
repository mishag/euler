#!/usr/bin/python

import primes
import sys

results     = {}
plist       = []
pset        = set([])

def print_max_ratio():
    max_key = 0
    max_value = 0
    max_ratio = 0
    for key, value in results.iteritems():
        ratio = float(key) / float(value)
        if ratio > max_ratio:
            max_ratio = ratio
            max_value = value
            max_key = key
            
    print "n=%d phi(n)=%d ratio=%f" %(max_key, max_value, max_ratio)

def generate_prime_powers(M):
    for p in plist:
        power = 2
        while p**power <= M:
            results[p**power] = (p**(power - 1)) * (p - 1)
            power += 1

def generate_primes(M):
    for p in primes.primes():
        
        if p > M:
            return
        
        plist.append(p)
        pset.add(p)
        results[p] = p - 1

# computes phi(p * mult) where p is prime
# if cannot compute from values in results map, return None
def compute(p, mult, M):
    
    if p * mult > M:
        return None
    
    other_mult = mult
    q = p

    while other_mult % p == 0:
        other_mult /= p
        q *= p
                
    if other_mult in results and q in results:
        return results[other_mult] * results[q]

    return None


        
def generate_all(M):
    for p in plist:
        mult = 2
        while p * mult <= M:
            val = compute(p, mult, M)
            if val:
                results[p * mult] = val
            mult += 1
                

if __name__ == "__main__":
    M = int(sys.argv[1])
    generate_primes(M)
    generate_prime_powers(M)
    generate_all(M)

    print "Computed: %d" %len(results)
    print_max_ratio()
