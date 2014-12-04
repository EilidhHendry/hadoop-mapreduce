#!/usr/bin/python

__author__ = 's0925284'

import sys

current_host = None
count = 0
first = True

for line in sys.stdin:
    host = line.strip()
    if host == current_host:
        count += 1
    else:
        count += 1
        if not first:
            print "%s\t%s" % (current_host, count)
        current_host = host
        count = 0
        first = False

if host==current_host:
    count += 1
    print "%s\t%s" % (current_host, count)