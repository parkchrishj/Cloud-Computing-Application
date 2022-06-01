#!/usr/bin/env python3
import sys


for line in sys.stdin:
    # TODO
    line = line.strip()
    word, count = line.split('\t')
    print('%s\t%s' % (word, count))
    # print('%s\t%s' % (  ,  )) pass this output to reducer
