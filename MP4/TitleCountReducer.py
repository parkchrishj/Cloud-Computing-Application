#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
wordDictionary = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    # gets rid of the tab
    #word is the word, and count is 1
    word, count = line.strip().split('\t', 1)
    #dictionary {'word' : 1} if word doesn't exist, put 0, or if it exists add 1 by 1
    wordDictionary[word] = int(wordDictionary.get(word, 0)) + 1

# TODO
# print('%s\t%s' % (  ,  )) print as final output
for word in wordDictionary:
    print('%s\t%s' % (word, wordDictionary.get(word)))