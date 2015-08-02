#!/usr/bin/python

from math import log

count = 0

if __name__ == "__main__":
    for k in range(2, 10):
        n = 1
        while log(k, 10) >= float(n - 1) / float(n):
            print "k = %d    n = %d" %(k, n)
            count += 1
            n += 1

    print count + 1   # +1 for 1
