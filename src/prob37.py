#!/usr/bin/python

import primes

ps = set([])

def is_truncatable(p):
    if p < 10:
        return False
    
    q    = p
    temp = p
    num_digits = 0
    
    while (p):
        num_digits += 1
        if p not in ps:
            return False
        
        p /= 10

    for i in range(num_digits-1, 0, -1):
        q= q % 10**i
        if q not in ps:
            return False

    print "prime %d is truncatable" %temp
    return True
        

if __name__ == "__main__":

    num_primes = 0
    s = 0
    for p in primes.primes():
        ps.add(p)
        if is_truncatable(p):
            s += p
            num_primes += 1
            
        if num_primes == 11:
            break

    print "Num primes = %d" %num_primes
    print "sum = %d" %s
    
