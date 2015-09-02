#!/usr/bin/python

import random
import sys

def does_ray_intersect_segment(ray_slope, point_x, point_y):
    a = point_x[0]
    b = point_x[1]

    c = point_y[0]
    d = point_y[1]
    
    alpha = ray_slope

    t = (d - alpha * c) / (d - b - alpha * (c - a))
    s = c - (c - a) * t

    return t >= 0 and t <= 1 and s >= 0


def does_triangle_contain_origin(A, B, C):
    ray_slope = random.random()
    num_intersections = 0
    if does_ray_intersect_segment(ray_slope, A, B):
        num_intersections += 1
        
    if does_ray_intersect_segment(ray_slope, A, C):
        num_intersections += 1
        
    if does_ray_intersect_segment(ray_slope, B, C):
        num_intersections += 1

    return num_intersections % 2 == 1

def run(filename):
    num_triangles_containing_origin = 0
    f = open(filename, 'r')
    for line in f:
        coordinates = [int(x) for x in line.strip().split(',')]
        if does_triangle_contain_origin((coordinates[0], coordinates[1]),
                                        (coordinates[2], coordinates[3]),
                                        (coordinates[4], coordinates[5])):
            num_triangles_containing_origin += 1

    print num_triangles_containing_origin


if __name__ == "__main__":
    # print does_triangle_contain_origin((-175, 41),
    #                                    (-421, -714),
    #                                    (574, -645))

    # print does_triangle_contain_origin((-340, 495),
    #                                    (-153, -910),
    #                                    (835, -947))

    filename = sys.argv[1]
    run(filename)
