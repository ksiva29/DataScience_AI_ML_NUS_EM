from src.pyspark_example import build_spark_session


def test_build_spark_session() -> None:
    spark = build_spark_session(app_name="test-pyspark-example")
    if spark is not None:
        spark.stop()
