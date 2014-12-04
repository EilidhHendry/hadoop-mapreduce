#!/usr/bin/python

__author__ = 'eilidhhendry'

import sys

for line in sys.stdin:
    line = line.strip()
    count, question_id = line.split("\t")
    print question_id, count
