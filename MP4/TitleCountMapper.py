#!/usr/bin/env python3

import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

# TODO
with open(stopWordsPath) as f:
    # TODO
    # lines is a list where each lines is an item.
    lines = f.readlines()
    # stopWords is a list of clean crisp words
    stopWords = [line.strip() for line in lines]

# TODO 
with open(delimitersPath) as f:
    # TODO
    # delimiters is a list of single item  ,;.?!-:@[](){}_*/
    delimiters = f.readline()

for line in sys.stdin:
    # TODO

    #strip all spaces and \n
    #excludes delimiters and lowercases all characters, and then join them back together into a single line
    line = ''.join([ch.lower() if ch not in delimiters else ' ' for ch in line.strip()])
    #exclude stopWords and split the lines into words
    line = line.split()
    wordstop = [word for word in line if word not in stopWords]
    #print word 'tab' 1
    for word in wordstop:
        print('%s\t%s' % (word, "1"))
    # print('%s\t%s' % (  ,  )) pass this output to reducer