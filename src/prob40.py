#!/usr/bin/python

def champernowne():
    n = 0
    while True:
        digits = [int(d) for d in str(n)]
        for d in digits:
            yield d

        n += 1

if __name__ == "__main__":
    for i,d in enumerate(champernowne()):
        if i in set([1, 10, 100, 1000, 10000, 100000, 1000000]):
            print d

        if i > 1000000:
            break

    exit(0)
