#!/usr/bin/python

import sys

__author__ = 's0925284'

current_file = None
count = 0
first = True

for line in sys.stdin:
    filename = line.strip()
    if filename == current_file:
        count += 1
    else:
        count += 1
        if not first:
            print "%s\t%s" % (current_file, count)
        current_file = filename
        count = 0
        first = False

if filename==current_file:
    count += 1
    print "%s\t%s" % (current_file, count)
