#!/usr/bin/python

__author__ = 'eilidhhendry'

import sys

current_user = None
posts = []
first = True

for line in sys.stdin:
    line = line.strip()
    owner_id, post_id = line.split("\t")
    if owner_id == current_user:
        posts.append(post_id)
    else:
        posts.append(post_id)
        if not first:
            print "%s\t%s\t%s" % (len(posts), current_user, posts)
        posts = []
        first = False
        current_user = owner_id

if owner_id == current_user:
    posts.append(post_id)
    print "%s\t%s\t%s" % (len(posts), current_user, posts)


