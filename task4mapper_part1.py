#!/usr/bin/python

__author__ = 'eilidhhendry'

import sys
import re

for line in sys.stdin:
    line = line.strip()
    post_type = re.findall(r'PostTypeId="(.*?)"', line)
    if post_type == '1':
        post_id = re.findall(r' Id="(.*?)"', line)
        view_count = re.findall(r'ViewCount="(.*?)"', line)
        print "%s\t%s" % (view_count, post_id)
