#!/usr/bin/python

__author__ = 'eilidhhendry'

import sys
import re

for line in sys.stdin:
    line = line.strip()
    post_type = re.findall(r'PostTypeId="(.*?)"', line)[0]
    if post_type == '2':
        owner_ids = re.findall(r'OwnerUserId="(.*?)"', line)
        if owner_ids:
            owner_id = owner_ids[0]
        post_id = re.findall(r' Id="(.*?)"', line)[0]
        print "%s\t%s" % (owner_id, post_id)
