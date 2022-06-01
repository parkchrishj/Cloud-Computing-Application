#!/usr/bin/env python3
import sys


# TODO
temp_dict = {}

for line in sys.stdin:
       #TODO
       child, count = line.strip().split('\t')
       child = int(child)
       temp_dict[child] = temp_dict.get(child,0) + int(count)

#TODO
sorted_array = sorted(temp_dict.items(), key = lambda kv: (kv[1]))#, reverse = True)

length = len(sorted_array)
for child, count in sorted_array[length-10:]:
       print('%s\t%s' % (child, count))
# print('%s\t%s' % (  ,  )) pass this output to reducer