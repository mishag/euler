#!/usr/bin/python

"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindromes = set([])

def generate_palindromes():
    for a in range(1,10):
        for b in range(0, 10):
            for c in range(0, 10):
                palindromes.add(a * 100001 + b * 10010 + c * 1100)

if __name__ == "__main__":
    generate_palindromes()
    max = 0
    first = 0
    second = 0
    for x in range(999, 0, -1):
        for y in range(x, 0, -1):
            prod = x*y
            if prod in palindromes and prod > max:
                max = prod
                first = x
                second = y
                
    print "%d = %d * %d" %(max, first, second)
