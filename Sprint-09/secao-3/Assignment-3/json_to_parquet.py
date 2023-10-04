import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from pyspark.sql.functions import lit, explode, col

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# As variáveis 
source_file_actor = 's3://etl-desafio/Raw/TMDB/JSON/2023/09/14/Resultados_Atores.json'
source_file_genre = 's3://etl-desafio/Raw/TMDB/JSON/2023/09/14/Resultados_Genero.json'
output_file_actor = 'Resultados_Atores.parquet'
output_file_genre = 'Resultados_Genero.parquet'
output_path_actor = f's3://etl-desafio/Trusted/Parquet/2023/09/25/{output_file_actor}'
output_path_genre = f's3://etl-desafio/Trusted/Parquet/2023/09/25/{output_file_genre}'

# Colocando os json's com o formato multilinha 
df_actors = spark.read.option('multiline', True).json(source_file_actor)
df_genre = spark.read.option('multiline', True).json(source_file_genre)

# Dropando colunas desnecessárias
df_actors_drop = df_actors.drop('page', 'total_pages', 'total_results')
# Dando um explode na coluna results
df_results_actors = df_actors_drop.select(explode(col("results")).alias("result"))

# O data frame com os dados da coluna result
df_actors_split = df_results_actors.select(
    col("result.adult").alias("adult"),
    col("result.gender").alias("gender"),
    col("result.id").alias("id"),
    col("result.known_for_department").alias("known_for_department"),
    col("result.name").alias("name"),
    col("result.popularity").alias("popularity"),
    col("result.profile_path").alias("profile_path"),
    explode(col("result.known_for")).alias("known_for")
)

# O data frame com os dados da coluna result mais os dados da coluna known_for explodida 
df_actors_split = df_actors_split.select(
    "adult",
    "gender",
    "id",
    "known_for_department",
    "name",
    "popularity",
    "profile_path",
    col("known_for.title").alias("Movie_title"),
    col("known_for.release_date").alias("Movie_release_date"),
    col("known_for.vote_average").alias("Movie_vote_average"),
    col("known_for.vote_count").alias("Movie_vote_count"),
    col("known_for.genre_ids").alias("genre_ids"),
    col("known_for.media_type").alias("media_type"),
    col("known_for.id").alias("Movie_id"),
    col("known_for.original_language").alias("original_language")
)

df_actors_split = df_actors_split.drop('profile_path', 'total_pages', 'total_results')

# Dropando colunas desnecessárias
df_genre_drop = df_genre.drop('page', 'total_pages', 'total_results')
# Dando um explode na coluna results
df_results_genre = df_genre_drop.select(explode(col("results")).alias("result"))

# O data frame com os dados da coluna result
df_genre_split = df_results_genre.select(
    col("result.first_air_date").alias("first_air_date"),
    col("result.genre_ids").alias("genre_ids"),
    col("result.id").alias("id"),
    col("result.name").alias("name"),
    col("result.origin_country").alias("origin_country"),
    col("result.original_language").alias("original_language"),
    col("result.original_name").alias("original_name"),
    col("result.popularity").alias("popularity"),
    col("result.vote_average").alias("vote_average"),
    col("result.vote_count").alias("vote_count")
)

# Escrevendo os parquet's
df_actors_split.write.parquet(output_path_actor, mode='overwrite')
df_genre_split.write.parquet(output_path_genre, mode='overwrite')


job.commit()