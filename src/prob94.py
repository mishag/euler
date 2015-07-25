#!/usr/bin/python

import sys
import math

def is_integral_area1(x):
    
    rad  = (3*x + 1) * (x - 1)

    last_digit = rad % 10    
    if last_digit == 3 or last_digit == 7:
        return False
    
    root = int(math.sqrt(rad))
    
    if root*root != rad:
        return False

    return ((x + 1) * root) % 4 == 0

def is_integral_area2(x):
    
    rad  = (3*x - 1) * (x + 1)
    
    last_digit = rad % 10
    if last_digit == 3 or last_digit == 7:
        return False
    
    root = int(math.sqrt(rad))
    
    if root*root != rad:
        return False

    return ((x - 1) * root) % 4 == 0

    
# 312530318954683775
# 156265304204412982
if __name__ == "__main__":
    MAX_PERIMETER = int(sys.argv[1])

    max_side = MAX_PERIMETER/3 + 10
    print "max side: %d" %max_side
    
    perimeter_sum = 0
    count = 0
    
    for x in xrange(3, max_side, 2):  # x must be odd
        
        count += 1
        if count % 10000000 == 0:
            print "Processed %d" %count

        if is_integral_area1(x):
            print "(%d, %d, %d)" %(x, x, x-1)
            if (3*x-1 < MAX_PERIMETER):
                perimeter_sum += 3*x - 1

        if is_integral_area2(x):
            print "(%d, %d, %d)" %(x, x, x+1)
            if (3*x + 1 < MAX_PERIMETER):
                perimeter_sum += 3*x + 1
            
    print perimeter_sum

        
        

    
