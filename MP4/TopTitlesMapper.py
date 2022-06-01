#!/usr/bin/env python3
import sys


# TODO
titles = {}


for line in sys.stdin:
       #TODO
       title, count = line.strip().split('\t')
       titles[title] = titles.get(title,0) + int(count)

sorted_dict = sorted(titles.items(), key=lambda kv: kv[1])# reverse = True)
#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
length = len(sorted_dict)
for title, count in sorted_dict[length-10:]:
       print('%s\t%s' % (title, count))
