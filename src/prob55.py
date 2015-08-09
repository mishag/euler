#!/usr/bin/python

import sys

def is_palindrome(n):
    nstr = str(n)
    i = 0
    j = len(nstr) - 1
    while i < j:
        if nstr[i] != nstr[j]:
            return False
        i += 1
        j -= 1

    return True

def reverse(n):
    return int(str(n)[::-1])

def is_lychrel(n):
    temp = n
    for i in range(50):
        n = n + reverse(n)
        if is_palindrome(n):
            print "%d ==> %d iterations" %(temp, i + 1)
            return False

    print "%d is Lychrel!" %temp
    return True

if __name__ == "__main__":
    N = int(sys.argv[1])
    count = 0
    for n in range(N):
        if is_lychrel(n):
            count += 1

    print count
