#!/usr/bin/python

import primes

prime_perms = {}

def is_arithmetic(seq):
    return seq[1] - seq[0] == seq[2] - seq[1]

def check_triples(prime_list):
    n = len(prime_list)

    for i in range(n):
        for j in range(i+1, n, 1):
            for k in range(j+1, n, 1):
                triple = [prime_list[i], prime_list[j], prime_list[k]]
                if is_arithmetic(triple):
                    print triple

if __name__ == "__main__":
    for p in primes.primes():
        if p < 1000:
            continue
        if p > 9999:
            break

        digit_tuple = tuple(sorted([int(d) for d in str(p)]))
        primes = prime_perms.get(digit_tuple, [])
        primes.append(p)
        prime_perms[digit_tuple] = sorted(primes)

    for key, prime_list in prime_perms.iteritems():
        if len(prime_list) < 3:
            continue

        if len(prime_list) > 3:
            check_triples(prime_list)
        
        
        
