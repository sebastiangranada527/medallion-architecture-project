from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum, count, to_date

def aggregate_to_gold(input_parquet, daily_output, product_store_output):
    spark = SparkSession.builder.appName("Gold").getOrCreate()
    df = spark.read.parquet(input_parquet)
    
    df_daily = df.groupBy(to_date("sale_date").alias("sale_date")) \
                 .agg(spark_sum("total").alias("daily_revenue"), count("*").alias("num_transactions"))
    
    df_product_store = df.groupBy("sale_date", "product", "store_id") \
                         .agg(spark_sum("total").alias("revenue"), count("*").alias("transactions"))
    
    df_daily.write.mode("overwrite").parquet(daily_output)
    df_product_store.write.mode("overwrite").parquet(product_store_output)
    print("Gold completado")
    spark.stop()