#!/usr/bin/python

if __name__ == "__main__":
    result_set = set([])
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            result_set.add(a**b)

    print len(result_set)
