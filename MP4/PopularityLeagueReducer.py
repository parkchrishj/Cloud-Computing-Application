#!/usr/bin/env python3
import sys
#TODO
league_dict = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    league, count = line.strip().split('\t')
    league = int(league)
    count = int(count)
    league_dict[league] = count

sorted_dict = sorted(league_dict.items(), key = lambda kv: kv[0], reverse = True)
#TODO
# print('%s\t%s' % (  ,  )) print as final output
for league, count in sorted_dict:
    rank = 0
    for leggo, compare in sorted_dict:
        if count > compare:
            rank = rank + 1
    print('%s\t%s' % (league, rank)) 