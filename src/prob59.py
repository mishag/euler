#!/usr/bin/python

import sys

def decode(line, key):
    s = ""
    N = len(line)
    for i in range(N):
        s += "%s" %chr(line[i] ^ key[i % 3])
        # s += "%s%s%s"  %(chr(key[0] ^ line[3*i]),
        #                  chr(key[1] ^ line[3*i + 1]),
        #                  chr(key[2] ^ line[3*i + 2]))
    return s

if __name__ == "__main__":
    #key = sys.argv[1]

    f = open('prob59.dat', 'r')
    nums = [int(x) for x in f.readline().strip().split(' ')]
    key = [ord('g'), ord('o'), ord('d')]
    text = decode(nums, key)
    print text
    print len(text)
    print sum([ord(c) for c in text])
