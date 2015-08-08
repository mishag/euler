#!/usr/bin/python

import itertools
import math

def make_series(f):
    for n in itertools.count(0):
        yield f(n)

def mult(a, b):
    alist = []
    blist = []
    current_power = 0
    for pair in itertools.izip(a, b):
        alist.append(pair[0])
        blist.append(pair[1])
        yield sum([alist[i] * blist[current_power - i] for i in xrange(current_power + 1)])
        current_power += 1

# constant term must equal to 1
def reciprocal(a):
    blist = [1]  # reciprocal
    alist = [next(a)]
    current_power = 1
    yield 1
    for x in a:
        alist.append(x)
        b = sum([-1 * alist[current_power - i] * blist[i] for i in xrange(current_power)])
        blist.append(b)
        yield b
        current_power += 1

def euler_function(n):
    root = int(math.sqrt(1 + 24*n))
    if root * root != 1 + 24 * n:
        return 0

    if (1 + root) % 6 == 0:
        power = (1 + root) / 6
        return 1 if power % 2 == 0 else -1

    if (1 - root) % 6 == 0:
        power = (1 - root) / 6
        return 1 if power % 2 == 0 else -1

    return 0
        
if __name__ == "__main__":
    f = make_series(lambda n: n+1)
    g = make_series(lambda n: 1)
    e = make_series(euler_function)
    
    # for i, prod in enumerate(mult(f, g)):
    #     if i > 10:
    #         break
    #     print prod

    # for i, inv in enumerate(reciprocal(f)):
    #     if i > 10:
    #         break
    #     print inv

    # for i, a in enumerate(e):
    #     if i > 10:
    #         break
    #     print a

    # Euler problem 78
    # 55374
    for i, inv in enumerate(reciprocal(e)):
        if i % 10000 == 0:
            print "Processed %d" %i
            break

        if inv % 1000000 == 0:
            print "%d ===> %d" %(i, inv)
