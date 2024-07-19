from pyspark.sql import SparkSession

# creating spark session and context
spark = SparkSession.builder.appName("word_counter").getOrCreate()
sc = spark.sparkContext

####################### Simple #######################

# reading file
text_file = sc.textFile("/app/sentences.txt")

# splitting words with space and counting each occurances
counts = text_file.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda x, y: x + y)
output = counts.collect()

####################### Spark DataFrame #######################

from pyspark.sql.functions import explode,split,col

# creating DataFrame
df = spark.read.text("/app/sentences.txt")

# splitting words and counting them, then sorting them based on count and storing in to new dataframe named as df_count
df_count=(
    df.withColumn('word', explode(split(col('value'), ' ')))
    .groupBy('word')
    .count()
    .sort('count', ascending=False)
)

# displaying DataFrame
df_count.show()

####################### Spark SQL #######################

df.createOrReplaceTempView('words')
word_count_df = spark.sql("""
    SELECT word, COUNT(*) AS count
    FROM (
        SELECT explode(split(value, ' ')) AS word
        FROM words
    )
    GROUP BY word
""")

results = word_count_df.collect()
for row in results:
    print(f"{row['word']}\t{row['count']}")