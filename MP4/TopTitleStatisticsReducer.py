#!/usr/bin/env python3
import sys
import math


#TODO
countList = []
for line in sys.stdin:
    # TODO
    word, count = line.strip().split('\t')
    countList.append(int(count))
#TODO
mean = math.floor(sum(countList) / len(countList))
countSum = sum(countList)
total = len(countList)
variance = math.floor(sum([(count-mean)**2 for count in countList]) / total)
# print('%s\t%s' % (  ,  )) print as final output
print('%s\t%s' % ("Mean", mean))
print('%s\t%s' % ("Sum", countSum))
print('%s\t%s' % ("Min", min(countList)))
print('%s\t%s' % ("Max", max(countList)))
print('%s\t%s' % ("Var", variance))
