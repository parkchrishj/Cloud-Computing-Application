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
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####
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
df2 = df.select("word", "count1").distinct().limit(100); #it really is 100 rows
df2.createOrReplaceTempView('gbooks2')
# df3 = df2
# df3.createOrReplaceTempView('gbooks3')
sqlContext.setConf("spark.sql.autoBroadcastJoinThreshold", "-1")
# sqlContext.sql("SELECT * FROM gbooks2 a INNER JOIN gbooks2 b WHERE a.count1=b.count1").count()
print(sqlContext.sql("SELECT * FROM gbooks2 A, gbooks2 B WHERE A.count1=B.count1").count())

# sqlContext.sql("SELECT * FROM gbooks2 INNER JOIN gbooks3 ON gbooks2.count1=gbooks3.count1").count()
# sqlContext.sql("SELECT * FROM gbooks2 A, gbooks3 B WHERE A.count1 = B.count1").count()
# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API
# output: 210

