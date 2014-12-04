#!/usr/bin/python

__author__ = 's0925284'

import sys

for line in sys.stdin:
    line = line.strip()
    reply = line.split()[-2]
    if reply=="404":
        host = line.split("- -")[0]
        print host



