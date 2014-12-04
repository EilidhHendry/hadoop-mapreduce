#!/usr/bin/python

import sys
import string
import os

for line in sys.stdin:
    line = line.strip()
    nopunc = line.translate(None, string.punctuation)
    tokens = nopunc.split()
    filepath = os.environ["map_input_file"]
    filename = os.path.split(filepath)[-1]
    for word in tokens:
        print "%s\t%s" % (word.lower(), filename)
