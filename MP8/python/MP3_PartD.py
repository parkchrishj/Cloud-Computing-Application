from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API


####
# 4. MapReduce (10 points): List the three most frequent 'word' with their count of appearances
####

# Spark SQL

# There are 18 items with count = 425, so could be different 
# +---------+--------+
# |     word|count(1)|
# +---------+--------+
# |  all_DET|     425|
# | are_VERB|     425|
# |about_ADP|     425|
# +---------+--------+

textfile = sc.textFile('gbooks')

def parse(lines):
    word = lines.strip().split("\t",1)[0]
    counts = lines.split("\t",1)[1]
    ret = []
    ret.append(word)
    for count in counts.split():
        ret.append(int(count))
    return ret

filterwordlist = ["ATTRIBUTE", ]
parsedRDD = textfile.map(parse)#.\
    # filter(lambda x: x in filterwordlist)
#print(parsedRDD.take(10))

fields = [
    StructField('word', StringType(), True),
    StructField('count1', IntegerType(), True),
    StructField('count2', IntegerType(), True),
    StructField('count3', IntegerType(), True),
    ]
schema = StructType(fields)

df = sqlContext.createDataFrame(parsedRDD, schema)
df.createOrReplaceTempView("DBname")

#part D

sqlContext.sql("SELECT word, COUNT(*) FROM DBname GROUP BY word ORDER BY 2 DESC").show(3)

