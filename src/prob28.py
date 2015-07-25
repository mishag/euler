#!/usr/bin/python

import sys

def generate(n):
    nums = [1]
    current = 1
    for d in xrange(2, n, 2):
        for j in range(4):
            current += d
            nums.append(current)

    return nums

if __name__ == "__main__":
    n = int(sys.argv[1])
    nums = generate(n)
    print sum(nums)
