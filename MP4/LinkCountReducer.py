#!/usr/bin/env python3
import sys

#TODO
temp_dict = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    child, count = line.strip().split('\t')
    child = int(child)
    temp_dict[child] = temp_dict.get(child,0) + int(count)

# TODO
for child, count in temp_dict.items():
    print('%s\t%s' % (child, count))
# print('%s\t%s' % (  ,  )) print as final output