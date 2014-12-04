#!/usr/bin/python

__author__ = 's0925284'

import sys
import ast

for line in sys.stdin:
    line = line.strip()
    word, idf, docs = line.split("\t")
    docs = docs.strip().strip("[]")
    docs_count = ast.literal_eval(docs)
    print docs_count
    for doc, count in docs_count:
        if doc=='d1.txt':
            print word, ", ", doc, " = ", count*float(idf)