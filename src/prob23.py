#!/usr/bin/python

N = 28124

def proper_divisors(n):
    divisors = []
    for i in xrange(1, n/2 + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors

def is_abundant(n):
    return sum(proper_divisors(n)) > n

def construct_abundant_nums(n):
    print "Constructing abundant nums < %d" %n
    abundant_nums = set([])
    for i in range(N):
        if is_abundant(i):
            abundant_nums.add(i)

    print "Done constructing abundant nums."
    return abundant_nums

def construct_abundant_sums(abundant_nums):
    print "Constructing abundant sums..."
    sums = set([])
    for m in abundant_nums:
        for n in abundant_nums:
            sums.add(m+n)

    return sums
    print "Done constructing sums"

if __name__ == "__main__":
    abundant_nums = construct_abundant_nums(N)
    abundant_sums = construct_abundant_sums(abundant_nums)
    result = 0
    for i in range(N):
        if i not in  abundant_sums:
            result += i

    print result
    exit(0)
            
