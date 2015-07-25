#!/usr/bin/python


while True:
    T = t(n)
    P = p(n)
    H = h(n)
    if T in ps and T in hs:
        print "%d ==> %d" %(n, T)
    ts.add(T)
    ps.add(P)
    hs.add(H)
    n += 1
