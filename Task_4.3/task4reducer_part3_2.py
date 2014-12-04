#!/usr/bin/python

__author__ = 's0925284'

import sys

current_user = None
answers = []
first = True
user_id = None
post_id = None

for line in sys.stdin:
    line = line.strip()
    user_id, post_id = line.split("\t")
    answers.append(post_id)
    if user_id != current_user:
        if not first:
            print "%s\t%s\t%s" % (len(answers), current_user, answers)
        answers = []
        current_user = user_id
        first = False

if user_id == current_user:
    answers.append(post_id)
    print "%s\t%s\t%s" % (len(answers), current_user, answers)