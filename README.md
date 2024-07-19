# Apache Spark Word Counter
- Simple word counter application built using Apache Spark.
- Is this the right project to showcase what apache spark is capable of? No.
- Is this project follows the best practices in terms of solution the infra for spark and folder structure? Probably not. 
- This project shows how apache spark is useful for streaming and batch processing.


### Tools and Technologies
- Docker
- Docker Compose
- Python
- Shell

### Project Explaination
- I am running 1 Spark Master and 3 Spark Worker through docker compose.
- `src/` directory is attached as volume with docker compose. This directory is not monitored by compose actively. So when you make changes, you have to update the job inside the container.
- Shell script is used for the same reason, it will copy the update python file to container and then submit the job to spark. Then spark will run that job.
- Here, job is nothing but the simple word count application.

### Libraries for Local Development
- pyspark

### Setup Instructions
- Create virtual environment and activate it.
    ```
    python3 -m venv venv
    source venv/bn/activate
    ```
- Install pyspark for local development.
    ```
    pip install pyspark
    # if you have requirements.txt
    pip install -r requirements.txt
    ```

### Running the project
- Execute below command to create spark cluster.
    ```
    docker compose up
    ```
- Now, we will run shell script to submit spark job to spark cluster.
    ```
    sh submit_spark_job.sh > output.txt
    ```
- You can see word counts are available in `output.txt`.