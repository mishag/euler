#!/usr/bin/python

import sys
import time

def reciprocal(n):
    r = 1
    while r:
        r *= 10
        if 0 == r / n:
            yield 0
            continue

        yield r / n
        r = r % n

def calc_interval(string):
    fragment = string[10:15]
    idx = string.find(fragment, 15)
    return idx - 10
    
if __name__ == "__main__":
    start = time.time()
    
    N = int(sys.argv[1])
    precision = int(sys.argv[2])

    max_interval = -100
    max_num = 0
    
    for n in range(1,N):
        digits = []
        # print "%d => " %n,
        for i, d in enumerate(reciprocal(n)):
            digits.append(d)
            if i >= precision - 1:
                break
            
        string = ''.join([str(d) for d in digits])
        interval = calc_interval(string)
        # print interval
        if interval > max_interval:
            max_interval = interval
            max_num = n

    print "%d ==> %d" %(max_num, max_interval)
    print time.time() - start
    exit(0)
