from pyspark.sql import SparkSession

def main():
    # Create a SparkSession
    spark = SparkSession.builder \
        .appName("HelloWorldPySpark") \
        .getOrCreate()

    # Sample data
    data = [("Alice", 28), ("Bob", 24), ("Cathy", 22)]

    # Convert the data to a DataFrame
    df = spark.createDataFrame(data, ["Name", "Age"])

    # Show the DataFrame
    df.show()

    # Stop the SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
