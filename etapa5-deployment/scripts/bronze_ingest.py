from pyspark.sql import SparkSession

def ingest_to_bronze(input_csv, output_parquet):
    spark = SparkSession.builder.appName("Bronze").getOrCreate()
    df = spark.read.csv(input_csv, header=True, inferSchema=True)
    df.write.mode("overwrite").parquet(output_parquet)
    print(f"Bronze completado: {output_parquet}")
    spark.stop()