from __future__ import annotations

from typing import Optional

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def build_spark_session(app_name: str = "pyspark-example") -> Optional[SparkSession]:
    try:
        return (
            SparkSession.builder.master("local[*]")
            .appName(app_name)
            .config("spark.driver.memory", "1g")
            .getOrCreate()
        )
    except Exception as exc:  # pragma: no cover - environment dependent
        print(f"Spark session could not be created: {exc}")
        return None


def run_sample_etl() -> None:
    spark = build_spark_session()
    if spark is None:
        print("PySpark ETL example skipped because Spark could not be started in this environment.")
        return

    data = [
        (1, "Alice", 25),
        (2, "Bob", 30),
        (3, "Charlie", 35),
    ]

    df = spark.createDataFrame(data, ["id", "name", "age"])
    filtered_df = df.filter(col("age") >= 30)
    filtered_df.show()

    spark.stop()


if __name__ == "__main__":
    run_sample_etl()
