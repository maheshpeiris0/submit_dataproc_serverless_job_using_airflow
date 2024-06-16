from pyspark.sql import SparkSession
from pyspark.sql.types import *  # Import datatypes for schema definition if needed
def load_data_gcs_to_gbq():
    spark = SparkSession.builder \
    .appName("GCS_to_GBQ") \
    .config("spark.jars", "gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.13-0.36.3.jar") \
    .getOrCreate()

    # GCS Configuration
    gcs_bucket = "bucket_name" # bucket name 
    gcs_file = "Google_Price.csv" # name of the file to be load or path of the file if in sub folder
    gcs_path = f"gs://{gcs_bucket}/{gcs_file}"

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(gcs_path)
    project_id = "project"  # project name
    bq_dataset = "bigquert_dataset" # dataset name
    bq_table = "google_shareprice"

    # 2. Write to BigQuery
    df.write.format("bigquery") \
        .option("table", f"{project_id}:{bq_dataset}.{bq_table}") \
        .option("temporaryGcsBucket", gcs_bucket)  \
        .mode("overwrite") \
        .save()

    spark.stop()
    
if __name__ == "__main__":
    load_data_gcs_to_gbq()
    
