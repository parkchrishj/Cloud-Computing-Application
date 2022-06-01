#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
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

collected_map = lines.flatMap(flat).\
  reduceByKey(lambda x,y: x+y).\
    takeOrdered(10, key=lambda x: -x[1])

output = open(sys.argv[2], "w")
sorted_dict = sorted(collected_map)

for child_count in sorted_dict:#.collect():
    output.write('%s\t%s\n' % (child_count[0],child_count[1]))

sc.stop()

# count_dict = {}
# collected_list = collected_map.collect()

# for child in collected_list:
#     count_dict[child] = count_dict.get(child,0) + 1

# sorted_array = sorted(count_dict.items())
# length = len(sorted_array)

# output = open(sys.argv[2], "w")

# #TODO
# #write results to output file. Foramt for each line: (key + \t + value +"\n")
# for child, count in sorted_array[length-10:]:
#     output.write('%s\t%s\n' % (child,count))

# sc.stop()

