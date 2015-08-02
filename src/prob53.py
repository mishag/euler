#!/usr/bin/python

import sys

results = {}

def generate(num_rows):
    over_million = 0
    
    results[(0,0)] = 1
    results[(1, 0)] = 1
    results[(1, 1)] = 1

    for row in range(2, num_rows):
        for col in range(0, row + 1):
            if col == 0 or col == row:
                results[(row, col)] = 1
            else:
                res = (results[(row - 1, col)] + 
                       results[(row - 1, col - 1)])
                results[(row, col)] = res
                if res > 1000000:
                    over_million += 1

    return over_million

def print_pascal(num_rows):
    for row in range(num_rows):
        for col in range(0, row + 1):
            print results[(row, col)],
        print "\n"

if __name__ == "__main__":
    num_rows = int(sys.argv[1])
    print generate(num_rows)  #4075
    #print_pascal(num_rows)
