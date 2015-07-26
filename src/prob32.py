#!/usr/bin/python

DIGITS = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
NUM_DIGITS = 9

results = set([])

def find_pandigital_products(digits):
    for i in range(1, NUM_DIGITS):
        for j in range(i + 1, NUM_DIGITS):
            mult1 = int(''.join([str(d) for d in digits[0:i]]))
            mult2 = int(''.join([str(d) for d in digits[i:j]]))
            prod =  mult1 * mult2 
            if ( prod == int(''.join([str(d) for d in digits[j:]]))):
                results.add(prod)
                print "%d * %d = %d" %(mult1, mult2, prod)
            

if __name__ == "__main__":
    for d1 in sorted(DIGITS):
        for d2 in sorted(DIGITS - set([d1])):
            for d3 in sorted(DIGITS - set([d1, d2])):
                for d4 in sorted(DIGITS - set([d1, d2, d3])):
                    for d5 in sorted(DIGITS - set([d1, d2, d3, d4])):
                        for d6 in sorted(DIGITS - set([d1, d2, d3, d4, d5])):
                            for d7 in sorted(DIGITS - set([d1, d2, d3, d4, d5, d6])):
                                for d8 in sorted(DIGITS - set([d1, d2, d3, d4, d5, d6, d7])):
                                    for d9 in sorted(DIGITS - set([d1, d2, d3, d4, d5, d6, d7, d8])):
                                        find_pandigital_products([d1, d2, d3, d4, d5, d6, d7, d8, d9])

    print sum(results)
