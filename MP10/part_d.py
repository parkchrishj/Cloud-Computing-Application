from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.linalg import Vectors

from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, FloatType, DoubleType
from pyspark.ml.feature import VectorAssembler

sc = SparkContext()
sqlContext = SQLContext(sc)


def predict(df_train, df_test):
    # TODO: Train random forest classifier

    # Hint: Column names in the given dataframes need to match the column names
    # expected by the random forest classifier `train` and `transform` functions.
    # Or you can alternatively specify which columns the `train` and `transform`
    # functions should use
    VecAssembler = VectorAssembler(inputCols = [f'{i}' for i in range(1,8)], outputCol ="features")
    new_df_train = VecAssembler.transform(df_train)
    # new_df_train.printSchema()
    rf = RandomForestClassifier(labelCol='label', featuresCol = 'features', numTrees = 200, maxDepth = 10)
    model = rf.fit(new_df_train)

    new_df_test = VecAssembler.transform(df_test)
    # new_df_test.printSchema()
    pred = model.transform(new_df_test)
    # pred.printSchema()
    # pred.show()#.select("prediction").show()
    # Result: Result should be a list with the trained model's predictions
    # for all the test data points
    ret = []
    for i in range(pred.count()):
        ret.append(int(pred.collect()[i][11]))
    return ret

def parse_line(line):
    label = line.strip().rsplit(",",1)[1]
    feats = line.rsplit(",",1)[0]
    ret = []
    ret.append(float(label))
    for feat in feats.split(","):
        ret.append(float(feat))
    return ret

def simple_parse_line(line):
    ret = []
    for feat in line.split(","):
        ret.append(float(feat))
    return ret

def main():
    raw_training_data = sc.textFile("dataset/training.data")

    # TODO: Convert text file into an RDD which can be converted to a DataFrame
    # Hint: For types and format look at what the format required by the
    # `train` method for the random forest classifier
    # Hint 2: Look at the imports above
    rdd_train = raw_training_data.map(parse_line)
    # print(rdd_train.take(3))
    # https://spark.apache.org/docs/1.5.0/ml-features.html#vectorassembler
    # TODO: Create dataframe from the RDD
    label_struct = StructType([StructField('label', FloatType(),True)])
    feat_struct = StructType([StructField(f'{i}',FloatType(),True) for i in range(1,9)])
    schema = StructType(label_struct.fields + feat_struct.fields)
    df_train = sqlContext.createDataFrame(rdd_train, schema)
    # df_train.show()
    # df_train.printSchema()

    raw_test_data = sc.textFile("dataset/test-features.data")

    # TODO: Convert text file lines into an RDD we can use later
    rdd_test = raw_test_data.map(simple_parse_line)
    # print(rdd_test.take(3))
    # TODO:Create dataframe from RDD
    schema = StructType([StructField(f'{i}',FloatType(),True) for i in range(1,9)])
    df_test = sqlContext.createDataFrame(rdd_test,schema)
    # df_test.show()
    # df_test.printSchema()

    predictions = predict(df_train, df_test)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right
    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()