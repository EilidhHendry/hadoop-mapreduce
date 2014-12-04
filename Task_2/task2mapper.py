#!/usr/bin/python

__author__ = 's0925284'

import sys

import math
terms = set()
for line in file('terms.txt'):
    terms.add(line.strip().lower())

for line in sys.stdin:
    line = line.strip()
    word, doc_freq, docs = line.split(":")
    word = word.strip()
    if word in terms:
        N = 17.0
        idf = math.log((N/(1+int(doc_freq))),10)
        print "%s\t%s\t%s" % (word, idf, docs)
