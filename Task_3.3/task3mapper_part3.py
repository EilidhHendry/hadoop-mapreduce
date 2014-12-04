#!/usr/bin/python

__author__ = 'eilidhhendry'

import sys
import re

for line in sys.stdin:
    line = line.strip()
    host = line.split("- -")[0]
    timestamp = re.findall(r'\[(.+)\]',line)[0]
    print "%s\t%s" % (host, timestamp)