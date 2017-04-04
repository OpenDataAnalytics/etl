import pyspark

# Create sql context
sqc = pyspark.sql.SQLContext(sc)

# Read hard-code data for now
mdata = sqc.read.parquet("hdfs://localhost:9000/mydata/out3.parq")
mrdd = mdata.rdd

# Print out number of rows in the data
mrdd.count()