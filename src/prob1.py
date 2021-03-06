#!/usr/bin/python

"""
If we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

if __name__ == "__main__":
    print sum([x for x in xrange(1000) if 0 == x % 3 or 0 == x % 5])
