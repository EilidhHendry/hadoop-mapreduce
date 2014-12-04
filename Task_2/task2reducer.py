#!/usr/bin/python

__author__ = 's0925284'

import sys
import ast

for line in sys.stdin:
    line = line.strip()
    word, idf, docs = line.split("\t")
    docs = docs.strip().strip("[]")
    docs_count = ast.literal_eval(docs)
    if len(docs_count)==2:
        doc = docs_count[0]
        count = docs_count[1]
        if doc=='d1.txt':
            print word, ", ", doc, " = ", count*float(idf)
    else:
        for doc, count in docs_count:
            if doc=='d1.txt':
                print word, ", ", doc, " = ", count*float(idf)