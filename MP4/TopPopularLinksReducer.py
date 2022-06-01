#!/usr/bin/env python3
import sys

titles = {}

# input comes from STDIN
for line in sys.stdin:
    # TODO
    # print('%s\t%s' % (  ,  )) print as final output
    child, count = line.strip().split('\t')
    titles[child] = int(count)

sorted_dict = sorted(titles.items(), key=lambda kv: kv[1])#, reverse = True)
    # print('%s\t%s' % (  ,  )) print as final output
    # first part of D is the output of unsorted output
length = len(sorted_dict)
for child, count in sorted_dict[length-10:]:
    print('%s\t%s' % (child, count))
