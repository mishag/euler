#!/usr/bin/python

import sys

def is_palindrome(string):    
    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1

    return True

def is_palindrome_10(n):
    return is_palindrome(str(n))

def is_palindrome_2(n):
    return is_palindrome(bin(n)[2:])
    
if __name__ == "__main__":
    N = int(sys.argv[1])

    S = 0
    for i in range(1,N):
        if is_palindrome_2(i) and is_palindrome_10(i):
            print "%d\t%s" %(i, bin(i))
            S += i

    print S
