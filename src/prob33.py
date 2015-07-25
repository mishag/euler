#!/usr/bin/python

import fractions


def is_cancelling_fraction(num, denom):
    if ((num >= denom)                      or
        (num > 99 or denom > 99)            or
        (num % 10 == 0 or denom % 10 == 0) or
        (num < 10)):
        
        return False

    # neither numerator nor denominator may contain digit 0

    num_digits   = [num / 10, num % 10]
    denom_digits = [denom / 10, denom % 10]

    val = float(num) / float(denom)

    if ( (float(num_digits[0]) / float(denom_digits[0]) == val) and
         (num_digits[1] == denom_digits[1]) ):
        return True

    if ( (float(num_digits[0]) / float(denom_digits[1]) == val) and
         (num_digits[1] == denom_digits[0]) ):
        return True

    if ( (float(num_digits[1]) / float(denom_digits[0]) == val) and
         (num_digits[0] == denom_digits[1]) ):
        return True

    if ( (float(num_digits[1]) / float(denom_digits[1]) == val) and
         (num_digits[0] == denom_digits[0]) ):
        return True

    return False
    
    
if __name__ == "__main__":
    prod_num = 1
    prod_denom = 1
    for num in range(11, 100):
        for denom in range(11, 100):
            if is_cancelling_fraction(num, denom):                
                print "(%d, %d)" %(num, denom)
                prod_num *= num
                prod_denom *= denom

    print fractions.Fraction(prod_num, prod_denom)
