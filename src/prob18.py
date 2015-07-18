#!/usr/bin/python

"""
find the max sum path from top to bottom in prob18.txt
"""

import sys

g_max_sum_at = {}

def construct_from_file(file_name):
    try:
        input = open(file_name, 'r')
    except:
        print "Failed to open file %s" %file_name
        return None

    triangle = []
    for line in input:
        line = [int(x) for x in line.strip().split()]
        triangle.append(line)

    return triangle

def generate_max_paths(triangle):
    last_row_index = len(triangle) - 1
    
    for i in range(last_row_index, -1, -1):
        for j, val in enumerate(triangle[i]):
            if i == last_row_index:
                g_max_sum_at[(i, j)] = val
            else:
                g_max_sum_at[(i, j)] = val + max(g_max_sum_at[(i+1, j)],
                                                 g_max_sum_at[(i+1, j+1)]) 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Expecting file name argument."
        exit(-1)

    triangle = construct_from_file(sys.argv[1])
    generate_max_paths(triangle)
    print g_max_sum_at[(0, 0)]
