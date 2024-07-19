#!/bin/bash
JOB_PATH="main.py"
SPARK_MASTER="spark-master"
CONTAINER_JOB_PATH="/app/${JOB_PATH}"

# Copy the Python script to Spark master container
docker cp src/${JOB_PATH} ${SPARK_MASTER}:${CONTAINER_JOB_PATH}
docker exec ${SPARK_MASTER} chmod +r ${CONTAINER_JOB_PATH}

# Submit the PySpark job using spark-submit
docker exec ${SPARK_MASTER} /opt/bitnami/spark/bin/spark-submit --master spark://spark-master:7077 ${CONTAINER_JOB_PATH}