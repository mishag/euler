#!/usr/bin/python

"""
Find abc where (a, b, c) is a pythagorean triplet with a + b + c = 1000
"""

def generate_candidates():
    for c in range(333, 500):
        for a in range(1, c):
            b = 1000 - a - c
            if a*a + b*b == c*c:
                print "a=%d b=%d c=%d abc=%d" %(a, b, c, a*b*c)

if __name__ == "__main__":
    generate_candidates()
