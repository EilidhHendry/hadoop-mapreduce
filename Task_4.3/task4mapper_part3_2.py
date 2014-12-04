#!/usr/bin/python

__author__ = 's0925284'

import sys
import re

queue = []

with open('accepted_answers.txt') as accepted_answers_file:
    for line in accepted_answers_file:
        line = line.strip()
        queue.append(line)

for line in sys.stdin:
    line = line.strip()
    post_type = re.findall(r'PostTypeId="(.*?)"', line)[0]
    if post_type == '2':
        post_id = re.findall(r' Id="(.*?)"', line)[0]
        if post_id in queue:
            user_ids = re.findall(r'OwnerUserId="(.*?)"', line)
            if user_ids:
                user_id = user_ids[0]
            print "%s\t%s" % (user_id, post_id)
