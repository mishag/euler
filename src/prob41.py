#!/usr/bin/python

import primes

def is_pandigital(n):
    n_str = str(n)
    num_digits = len(n_str)
    digit_set = set([int(d) for d in n_str])
    return (len(digit_set) == num_digits and 
            min(digit_set) == 1 and 
            max(digit_set) == num_digits)

MAX_NUM = 7654321

if __name__ == "__main__":
    max_pandigital = 2
    count = 0
    for p in primes.primes():
        
        count += 1
        if count % 1000000 == 0:
            print "%d done" %count
            
        if is_pandigital(p):
            max_pandigital = p

        if p > MAX_NUM:
            break

    print max_pandigital
            
