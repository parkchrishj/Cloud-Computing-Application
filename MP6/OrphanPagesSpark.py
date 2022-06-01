#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1)

def flat(z):
  ret = []
  parent = z.split(": ")[0]
  ret.append((parent, 0))
  children = z.split(": ")[1]
  for child in children.split():
    ret.append((child,1))
  return ret

collected_map = lines.flatMap(flat).\
  reduceByKey(lambda x,y: x+y).\
    filter(lambda x: int(x[1])==0).\
      sortByKey()

output = open(sys.argv[2], "w")

for orphan in collected_map.collect():
  output.write('%s\n' % (orphan[0]))

sc.stop()
