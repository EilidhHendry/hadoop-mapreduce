#!/usr/bin/python

import sys
from collections import defaultdict

current_word = None
first = True
locations = defaultdict(int)


for line in sys.stdin:
    line = line.strip()
    word, location = line.split("\t")
    if word == current_word:
        locations[location]+=1
    else:
        locations[location]+=1
        if not first:
            sorted_dict = sorted(locations.items())
            print current_word, " : ", len(locations), " : ", sorted_dict
        current_word = word
        locations = defaultdict(int)
        first = False

if word==current_word:
    locations[location]+=1
    sorted_dict = sorted(locations.items())
    print current_word, " : ", len(locations), " : ", sorted_dict

