from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
import pyspark.sql.functions as F

from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, FloatType
from pyspark.ml.feature import VectorAssembler

############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()
sqlContext = SQLContext(sc)


def get_clusters(df, num_clusters, max_iterations, initialization_mode,
                 seed):
    # TODO:
    # Use the given data and the cluster parameters to train a K-Means model
    # Find the cluster id corresponding to data point (a car)
    # Return a list of lists of the titles which belong to the same cluster
    # For example, if the output is [["Mercedes", "Audi"], ["Honda", "Hyundai"]]
    # Then "Mercedes" and "Audi" should have the same cluster id, and "Honda" and
    # "Hyundai" should have the same cluster id
    vecAssembler = VectorAssembler(inputCols = [f'{i}' for i in range(1,12)], outputCol ="features")
    new_df = vecAssembler.transform(df)
    kmeans = KMeans(k=num_clusters, initMode=initialization_mode, maxIter=max_iterations, seed=seed)
    # model = kmeans.fit(df)
    # transformed = model.transform(df).select("features")
    model = kmeans.fit(new_df.select('features'))
    transformed = model.transform(new_df)
    # transformed.show()
    #https://stackoverflow.com/questions/47585723/kmeans-clustering-in-pyspark/47593712
    #https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.KMeans.html#pyspark.ml.clustering.KMeans
    
    # group0 = transformed.filter(prediction==0)
    # group1 = transformed.filter(prediction==1)
    ret = []
    for i in range(4):
        ret_temp = []
        group = transformed.filter(transformed.prediction==i)
        for i in range(group.count()):
            ret_temp.append(group.collect()[i][0])
        ret.append(ret_temp)    
    return ret


def parse_line(line):
    # TODO: Parse data from line into an RDD
    # Hint: Look at the data format and columns required by the KMeans fit and
    # transform functions
    car = line.strip().split(",",1)[0]
    feats = line.split(",",1)[1]
    ret = []
    ret.append(car)
    for feat in feats.split(","):
        ret.append(float(feat))
    return ret


if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")

    rdd = f.map(parse_line)
    # print(rdd.take(10))
    # TODO: Convert RDD into a dataframe
    car_struct = StructType([StructField('car', StringType(),True)])
    feat_struct = StructType([StructField(f'{i}',FloatType(),True) for i in range(1,12)])
    schema = StructType(car_struct.fields + feat_struct.fields)
    df = sqlContext.createDataFrame(rdd, schema)
    # df.printSchema()
    # df.createOrReplaceTempView("DBname")
    # sqlContext.sql("SELECT * FROM DBname").show()

    clusters = get_clusters(df, NUM_CLUSTERS, MAX_ITERATIONS,
                            INITIALIZATION_MODE, SEED)
    for cluster in clusters:
        print(','.join(cluster))