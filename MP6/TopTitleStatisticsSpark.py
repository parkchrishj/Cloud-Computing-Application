#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import math

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1],1)

#TODO                                     1     2
# spark-submit TopTitleStatisticsSpark.py partA partB
collected_list = lines.collect()
countList = []
for line in collected_list:
    word, count = line.strip().split('\t')
    countList.append(int(count))

mean = math.floor(sum(countList) / len(countList))
countSum = sum(countList)
total = len(countList)
variance = math.floor(sum([(count-mean)**2 for count in countList]) / total)

outputFile = open(sys.argv[2],"w")

#TODO write your output here
#write results to output file. Format
outputFile.write('Mean\t%s\n' % mean)
outputFile.write('Sum\t%s\n' % countSum)
outputFile.write('Min\t%s\n' % min(countList))
outputFile.write('Max\t%s\n' % max(countList))
outputFile.write('Var\t%s\n' % variance)


sc.stop()

