#!/usr/bin/env python
#                                                         1              2
#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO

def flat(z):
  ret = []
  parent = z.split(": ")[0]
  ret.append((parent, 0))
  children = z.split(": ")[1]
  for child in children.split():
    ret.append((child,1))
  return ret

leagueIds = sc.textFile(sys.argv[2], 1)

#TODO
league_list = leagueIds.collect()

collected_map = lines.flatMap(flat).\
  reduceByKey(lambda x,y: x+y).\
    filter(lambda x: x[0] in league_list).\
      sortByKey()

output = open(sys.argv[3], "w")
sorted_list = collected_map.collect()
#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")
for league_count in sorted_list:
    rank = 0
    for league_count2 in sorted_list:
        if league_count[1] > league_count2[1]:
            rank = rank +1
    output.write('%s\t%s\n' % (league_count[0],rank))

sc.stop()

