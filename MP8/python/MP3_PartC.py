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
# 3. Filtering (10 points) Count the number of appearances of word 'ATTRIBUTE'
####

# Spark SQL

# +--------+                                                                      
# |count(1)|
# +--------+
# |     201|
# +--------+

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

#part C

# sqlContext.sql("SELECT Count(*) FROM DBname").show()
# sqlContext.sql("SELECT COUNT(word) FROM DBname WHERE word CONTAINS 'ATTRIBUTE'").show()
sqlContext.sql("SELECT COUNT(*) FROM DBname WHERE word = 'ATTRIBUTE'").show()
# sqlContext.sql("SELECT COUNT(*) FROM DBname WHERE word LIKE '%ATTRIBUTE%')").show()
# https://stackoverflow.com/questions/7510646/like-vs-contains-on-sql-server/7510685
