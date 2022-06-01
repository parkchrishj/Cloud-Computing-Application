#!/usr/bin/env python3
import sys


for line in sys.stdin:
  #TODO
  id, children_array = line.strip().split(':')
  children = children_array.split()

  for child in children:
    # if id != child:
      print('%s\t%s' % (child, "1"))
  # print('%s\t%s' % (  ,  )) pass this output to reducer