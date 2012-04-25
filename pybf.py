#!/usr/bin/python

import itertools
import string

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

n = raw_input("insert integer repeat number:")
m = int(n)

f = itertools.product(alphabet, repeat=m)
for elem in f:
    print elem
