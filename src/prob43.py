#!/usr/bin/python

import time

def make_number(digits):
    return int(''.join([str(d) for d in digits]))

if __name__ == "__main__":
    start = time.time()
    
    S = 0
    digits = set(range(0, 10))
    for d1 in digits - set([0]):
        for d2 in digits - set([d1]):
            for d3 in digits - set([d1, d2]):
                for d4 in digits - set([d1, d2, d3, 1, 3, 5, 7, 9]):
                    for d5 in digits - set([d1, d2, d3, d4]):
                        for d6 in set([0, 5]) - set([d1, d2, d3, d4, d5]):
                            for d7 in digits - set([d1, d2, d3, d4, d5, d6]):
                                for d8 in digits - set([d1, d2, d3, d4, d5, d6, d7]):
                                    for d9 in digits - set([d1, d2, d3, d4, d5, d6, d7, d8]):
                                        for d10 in digits - set([d1, d2, d3, d4, d5, d6, d7, d8, d9]):
                                            if ( (make_number([d3, d4, d5]) % 3 == 0) and
                                                 (make_number([d5, d6, d7]) % 7 == 0) and
                                                 (make_number([d6, d7, d8]) % 11 == 0) and
                                                 (make_number([d7, d8, d9]) % 13 == 0) and
                                                 (make_number([d8, d9, d10]) % 17 == 0) ):
                                                n = make_number([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10])
                                                print n
                                                S += n
    end = time.time()
    print S
    print end - start

    
                                           
