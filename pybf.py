#!/usr/bin/python

import itertools
import string
import sys

def main():
#    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    alphabet = string.lowercase[:26]

#    n = raw_input("insert the character size:")
#    m = int(n)
    o = sys.argv[1]
    p = int(o)

    f = itertools.product(alphabet, repeat=p)
    for elem in f:
        print elem

if __name__== '__main__':
    main()
