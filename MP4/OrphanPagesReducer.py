#!/usr/bin/env python3
import sys


#TODO
temp_dict = {}
#temp_dict parents start off 0 and +1 if in child & child start off 1 and +1 if in child again
for line in sys.stdin:
  # TODO
  parent, link_count = line.strip().split('\t')
  parent = int(parent)
  temp_dict[parent] = temp_dict.get(parent, 0) + int(link_count)
#TODO
#make the dictionary into a list for sorting

dict_items = temp_dict.items()
sorted_array = sorted(dict_items)
# print(sorted_array)
# print(xx) print as final output
#go through the dict in ascended order to print out the links that have 0 count
for link, count in sorted_array:
  if temp_dict.get(link) == 0:
    print(link)