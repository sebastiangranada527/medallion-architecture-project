from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, when, to_date

def transform_to_silver(input_parquet, output_parquet):
    spark = SparkSession.builder.appName("Silver").getOrCreate()
    df = spark.read.parquet(input_parquet)
    
    df_silver = df.withColumn("store_id", regexp_replace(col("store_id"), r"[^0-9]", "")) \
                  .withColumn("store_id", when(col("store_id") != "", col("store_id")).otherwise("UNKNOWN")) \
                  .na.fill({"price": 0.0, "total": 0.0, "status": "Unknown", "quantity": 0.0}) \
                  .filter((col("total") >= 0) & (col("quantity") >= 0)) \
                  .withColumn("sale_date", to_date(col("sale_date")))
    
    df_silver.write.mode("overwrite").partitionBy("sale_date").parquet(output_parquet)
    print(f"Silver completado: {output_parquet}")
    spark.stop()