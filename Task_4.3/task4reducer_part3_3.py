#!/usr/bin/python

__author__ = 's0925284'

import sys

for line in sys.stdin:
    line = line.strip()
    size, user, answers = line.split("\t")
    print user, " -> ", size, answers