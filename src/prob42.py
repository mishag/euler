#!/usr/bin/python

import math

def is_triangle_number(a):
    radicand = 8*a + 1
    root = int(math.sqrt(radicand))
    if root*root != radicand:
        return False

    return (root - 1) % 2 == 0


if __name__ == "__main__":
    f = open('prob42.dat', 'r')
    count = 0
    for word in f:
        word = word.strip()
        word_val = sum([ord(letter) - ord('A') + 1 for letter in word])
        if is_triangle_number(word_val):
            count += 1

    print count
