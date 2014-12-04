#!/usr/bin/python

__author__ = 's0925284'

import sys
import re

for line in sys.stdin:
    line = line.strip()
    post_type = re.findall(r'PostTypeId="(.*?)"', line)[0]
    if post_type == '1':
        accepted_answer = re.findall(r'AcceptedAnswerId="(.*?)"', line)
        if accepted_answer:
            print accepted_answer[0]