#!/usr/bin/python

__author__ = 's0925284'

import re
import sys

def get_web_page(line):
    request = re.findall(r'\"(.+)\"',line)[0]
    tokens = request.split()
    if len(tokens) == 1:
        accessed_file = tokens[0]
    else:
        accessed_file = tokens[1]
    return accessed_file

for line in sys.stdin:
    line = line.strip()
    print get_web_page(line)

