#!/usr/bin/python

import sys

"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2      (n is even)
n -> 3n + 1   (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

sys.setrecursionlimit(10000)

g_lengths = {
    0 : 0,
    1 : 1    
}

def c(n):
    return n/2 if 0 == n % 2 else 3*n + 1

def sequence_length(n):
    
    if n in g_lengths:
        return g_lengths[n]

    g_lengths[n] = 1 + sequence_length(c(n))
    return g_lengths[n]

if __name__ == "__main__":
    N = int(sys.argv[1])

    max_len   = 0
    max_index = -1
    
    for i in range(N):
        len = sequence_length(i)
        if len > max_len:
            max_len   = len
            max_index = i

    print "%d ==> %d" %(max_index, max_len)
        
