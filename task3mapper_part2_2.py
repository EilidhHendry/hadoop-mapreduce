#!/usr/bin/python

__author__ = 's0925284'

import sys

for line in sys.stdin:
    line = line.strip()
    host, count = line.split("\t")
    print count, host