#!/usr/bin/env python3
import sys


for line in sys.stdin:
  # TODO
  line = line.strip()
  id, children = line.split(':')
  child = children.split()
  #parents are 0
  if child:
    print('%s\t%s' % (id, 0))
    for link in child:
      if link != id:
        print('%s\t%s' % (link, 1))
  #every child are 1, cuz they got 1 to link to it.
  # print('%s\t%s' % (  ,  )) pass this output to reducer