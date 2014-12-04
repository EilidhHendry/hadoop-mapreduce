#!/usr/bin/python

import sys
from collections import defaultdict

current_word = None
word = None
location = None
locations = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    word, location = line.split("\t")
    if word == current_word:
        locations[location] += 1
    else:
        if current_word:
            if locations:
                sorted_dict = sorted(locations.items())
                print current_word, " : ", len(locations), " : ", sorted_dict
            else:
                print current_word, " : ", 1, "  : ", (location,1)
        current_word = word
        locations = defaultdict(int)

# catch the last word
if word == current_word:
    locations[location] += 1
    sorted_dict = sorted(locations.items())
    print current_word, " : ", len(locations), " : ", sorted_dict

