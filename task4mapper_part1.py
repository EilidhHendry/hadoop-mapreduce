#!/usr/bin/python

__author__ = 'eilidhhendry'

import sys
import re

for line in sys.stdin:
    line = line.strip()
    post_type = re.findall(r'PostTypeId="(.*?)"', line)[0]
    if post_type == '1':
        post_id = re.findall(r' Id="(.*?)"', line)[0]
        view_count = re.findall(r'ViewCount="(.*?)"', line)[0]
        print "%s\t%s" % (view_count, post_id)
