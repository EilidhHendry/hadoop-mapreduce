#!/usr/bin/python

__author__ = 'eilidhhendry'

import sys
import datetime

current_host = None
first = True
min_time = datetime.datetime(datetime.MAXYEAR, 1, 1)
max_time = datetime.datetime(datetime.MINYEAR, 1, 1)

for line in sys.stdin:
    line = line.strip()
    host, timestamp = line.split("\t")
    time = datetime.datetime.strptime(timestamp[:-6], "%d/%b/%Y:%H:%M:%S")
    if host == current_host:
        if time < min_time:
            min_time = time
        if time > max_time:
            max_time = time
    else:
        if time < min_time:
            min_time = time
        if time > max_time:
            max_time = time
        if not first:
            if max_time-min_time == datetime.timedelta(0):
                print current_host, max_time
            else:
                print current_host, max_time - min_time
        current_host = host
        max_time = time
        min_time = time
        first = False

if host == current_host:
    if time < min_time:
        min_time = time
    if time > max_time:
        max_time = time
    if max_time-min_time == datetime.timedelta(0):
        print current_host, max_time
    else:
        print current_host, max_time - min_time