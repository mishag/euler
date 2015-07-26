#!/usr/bin/python

# 997651 ==> 543

import time
import sys
import primes

plist = []

def get_max_sequential_sum_len(p, seq):
    # print seq
    end = len(seq) - 1
    start = end
    curr_sum = seq[end]
    max_seq_len = end - start + 1
    
    while True:        
        if curr_sum < p:
            start -= 1
            if start < 0: 
                break
            curr_sum += seq[start]

        if curr_sum > p:
            curr_sum -= seq[end]
            end -= 1
            if end < 0:
                break
            
        if curr_sum == p:
            #print "Got seq summing to p: %s -> %d" %(seq[start:end+1], sum(seq[start:end+1]))
            
            if end - start + 1 > max_seq_len:
                max_seq_len = end - start + 1
                
            curr_sum -= seq[end]
            end -= 1
            start -= 1
            if start < 0:
                break
            curr_sum += seq[start]

    return max_seq_len

if __name__ == "__main__":
    start = time.time()
    
    N = int(sys.argv[1])
    
    for p in primes.primes():
        if p >= N:
            break
        plist.append(p)

    max_seq_length = 0
    max_prime = 0
    for i,p in enumerate(plist[::-1]):
        seq_length = get_max_sequential_sum_len(p, plist[:len(plist)-i])
        print "%d ==> %d" %(p, seq_length)        
        if seq_length > max_seq_length:
            max_prime = p
            max_seq_length = seq_length

            
    print "%d ==> %d" %(max_prime, max_seq_length)
    print time.time() - start
