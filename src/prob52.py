#!/usr/bin/python

def check(n):
    n2 = str(2*n)
    n3 = str(3*n)
    n4 = str(4*n)
    n5 = str(5*n)
    n6 = str(6*n)

    if (len(n2) != len(n3) or
        len(n3) != len(n4) or
        len(n4) != len(n5) or
        len(n5) != len(n6) or
        len(n6) != len(n2)):
        return False

    return (sorted(n2) == sorted(n3) and
            sorted(n3) == sorted(n4) and
            sorted(n4) == sorted(n5) and
            sorted(n5) == sorted(n6))
    

if __name__ == "__main__":
    n = 0
    while True:
        n += 1
        
        if n % 10000 == 0:
            print "Processed %d" %n
            
        if check(n):
            print n
            exit(0)
