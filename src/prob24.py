#!/usr/bin/python

import sys
import time

if __name__ == "__main__":
    N = int(sys.argv[1])
    
    start = time.time()
    count = 0
    digits = set(range(0, 10))
    for d1 in sorted(digits):
        for d2 in sorted(digits - set([d1])):
            for d3 in sorted(digits - set([d1, d2])):
                for d4 in sorted(digits - set([d1, d2, d3])):
                    for d5 in sorted(digits - set([d1, d2, d3, d4])):
                        for d6 in sorted(digits - set([d1, d2, d3, d4, d5])):
                            for d7 in sorted(digits - set([d1, d2, d3, d4, d5, d6])):
                                for d8 in sorted(digits - set([d1, d2, d3, d4, d5, d6, d7])):
                                    for d9 in sorted(digits - set([d1, d2, d3, d4, d5, d6, d7, d8])):
                                        for d10 in sorted(digits - set([d1, d2, d3, d4, d5, d6, d7, d8, d9])):
                                            count += 1
                                            if count == N:
                                                print ''.join([str(d) for d in [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]])
                                                end = time.time()
                                                print end - start
                                                exit(0)


