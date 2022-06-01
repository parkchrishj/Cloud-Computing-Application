#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO
league_dict = {}
league_list = []

with open(leaguePath) as f:
	#TODO
       leagues = f.readlines()
       for league in leagues:
              league = int(league)
              league_list.append(league)
       # leagues = []
       # for line in f:
       #        leagues.append(line.split()[0])
       # for league in leagues:
       #        league_dict[league] = 0

for line in sys.stdin:
       #TODO
       child, count = line.strip().split('\t')
       child = int(child)
       count = int(count)
       # league_list_items = league_list.items()
       # sort_dict = sorted(league_list_items)
       for league in league_list:
              if child == league:
                     league_dict[league] = int(count)
       # print('%s\t%s' % (  ,  )) pass this output to reducer
for league, count in league_dict.items():
       print('%s\t%s' % (league, count))