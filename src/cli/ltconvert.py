#!/usr/bin/python

import lingtree
import sys

# open file specified on command-line
try:
    filename = sys.argv.pop(1)
    file = open(filename)
except:
    print 'please specify a valid input filename'
    sys.exit(2)

print lingtree.convert(''.join(file.readlines()))
