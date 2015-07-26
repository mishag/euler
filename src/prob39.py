#!/usr/bin/python

import sys

def get_pythagorian_triples(p):
    triples = set([])
    for a in range(3,p):
        for b in range(a,p):
            c = p - (a + b)
            if c <= b:
                break
            if a*a + b*b == c*c:
                triples.add(tuple(sorted([a, b, c])))

    return triples

def print_results(results):
    for key, value in results.iteritems():
        
        if len(value) == 0:
            continue
        
        print "%d ==> %s" %(key, value)

if __name__ == "__main__":
    P = int(sys.argv[1])

    results = {}
    for p in range(12,P):
        results[p] = get_pythagorian_triples(p)

    print_results(results)
