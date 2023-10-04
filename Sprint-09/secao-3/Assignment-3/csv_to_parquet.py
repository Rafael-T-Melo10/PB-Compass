import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# As varáveis
output_file_serie = 'movies.parquet'
output_file_movies = 'series.parquet'
source_file_serie = 's3://etl-desafio/Raw/Local/CSV/Series/2023/08/31/series.csv'
source_file_movies = 's3://etl-desafio/Raw/Local/CSV/Movies/2023/08/31/movies.csv'
output_path_serie = f's3://etl-desafio/Trusted/Parquet/2023/09/25/{output_file_serie}'
output_path_movies = f's3://etl-desafio/Trusted/Parquet/2023/09/25/{output_file_movies}'

# Carregando os csv's em dataframes
df_movies = spark.read.load(source_file_serie, format='csv', sep='|', inferSchema='True', header='True')
df_series = spark.read.load(source_file_movies, format='csv', sep='|', inferSchema='True', header='True')

# Escrevendo os parquets
df_movies.write.parquet(output_path_movies, mode='overwrite')
df_series.write.parquet(output_path_serie, mode='overwrite')

job.commit()