#!/usr/bin/env python
#                                                     1             2               3               4
'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
	#TODO
    lines = f.readlines()
    stopWords = [line.strip() for line in lines]

with open(delimitersPath) as f:
    #TODO
    delimiters = f.readline()

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[3],1)

#TODO
collected_list = lines.collect()
wordDictionary = {}
for line in collected_list:
    #strip all spaces and \n
    #excludes delimiters and lowercases all characters, and then join them back together into a single line
    line = ''.join([ch.lower() if ch not in delimiters else ' ' for ch in line.strip()])
    #exclude stopWords and split the lines into list of words
    line = line.split()
    wordstop = [word for word in line if word not in stopWords]
    for word in wordstop:
        wordDictionary[word] = int(wordDictionary.get(word, 0)) + 1
    
outputFile = open(sys.argv[4],"w")

#TODO
#write results to output file. Foramt for each line: (line +"\n")
sorted_dict = sorted(wordDictionary.items(), key=lambda kv: kv[1], reverse = True)
alphabet = {}
for title, count in sorted_dict[:10]:
    alphabet[title] = count
alphabet_sorted = sorted(alphabet.items())
for title, count in alphabet_sorted[:10]:
    outputFile.write('%s\t%s\n' % (title, count))

sc.stop()
