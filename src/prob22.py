#!/usr/bin/python

if __name__ == "__main__":
    input = open("prob22.txt", "r")

    total = 0
    
    for i, line in enumerate(input):
        name = line.strip()
        name_total = sum([ord(c) - ord('A') + 1 for c in list(name)])
        total += (i+1) * name_total
        
    print total
