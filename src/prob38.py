#!/usr/bin/python

import sys

TUPLES = [(1, 2),
          (1, 2, 3),
          (1, 2, 3, 4),
          (1, 2, 3, 4, 5)]

def is_pandigital(string):
    if '0' in string:
        return False
    set_size = len(set(string))
    return set_size == 9 and set_size == len(string)

def concatenated_product(n, tple):
    nums = ''.join([str(n * a) for a in tple])
    return nums

if __name__ == "__main__":
    results = set([])
    N = int(sys.argv[1])
    max_product = 0
    max_tuple = tuple()
    max_num   = 0

    for n in xrange(10000):
        for t in TUPLES:
            concat_product = concatenated_product(n, t)
            if is_pandigital(concat_product):
                results.add(concat_product)
                concat_product_int = int(concat_product)
                if  concat_product_int > max_product:
                    max_product = concat_product_int
                    max_tuple = t
                    max_num = n

    print results
    print "max_product: %d\nmax_tuple: %s\nmax_num:%d" %(max_product,
                                                         max_tuple,
                                                         max_num)
