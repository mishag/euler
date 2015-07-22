#!/usr/bin/python

import primes
import partitions

if __name__ == "__main__":
    n = 1
    prime_set = []
    for p in primes.primes():
        prime_set.append(p)
        while (n <= p):
            primes_tuple = tuple(prime_set)
            num_partitions = partitions.partitions_from_set(n, primes_tuple)
            print "%d ==> %d" %(n, num_partitions)
            if num_partitions >= 5000:
                exit(0)
            n += 1
