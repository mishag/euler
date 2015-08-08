#!/usr/bin/python

import sys

if __name__ == "__main__":
    max_digit_sum = 0
    max_a = 0
    max_b = 0
    
    N = int(sys.argv[1])
    for a in range(1, N):
        for b in range(1, N):
            digit_sum = sum([ord(d) - ord('0') for d in str(a**b)])
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
                max_a = a
                max_b = b

    print "a=%d b=%d max_digit_sum=%d" %(max_a, max_b, max_digit_sum)
