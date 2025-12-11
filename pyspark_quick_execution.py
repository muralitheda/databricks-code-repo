from pyspark.sql.session import SparkSession
spark = SparkSession.builder.appName("SparkQuickExecutionProgram").getOrCreate()

print(f"Spark Session: {spark}")
print(f"Spark version: {spark.version}")
print(f"Spark master: {spark.conf.get('spark.master')}")
print(f"Spark app name: {spark.conf.get('spark.app.name')}")