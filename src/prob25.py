#!/usr/bin/python

"""
first fibonacci number with number of digits >= 1000
"""

import math
import itertools
import prob2


if __name__ == "__main__":
    for i, f in enumerate(prob2.fib()):
        if len(list(str(f))) >= 1000:
            print i+1

            break

    exit(0)
