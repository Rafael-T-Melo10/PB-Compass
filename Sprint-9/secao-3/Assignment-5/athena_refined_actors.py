import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Uma função para colocar somente uma repartição de parquet para cada tabela
def create_dynamic_frame(glueContext, database, table_name):
    return glueContext.create_dynamic_frame.from_catalog(database=database, table_name=table_name).repartition(1)

# Uma função para escrever o dataframe
def write_dynamic_frame(glueContext, dynamic_frame, output_path):
    glueContext.write_dynamic_frame.from_options(
        frame=dynamic_frame, connection_type='s3',
        connection_options={'path': output_path}, format='parquet'
    )

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

glueContext = GlueContext(SparkContext.getOrCreate())
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job.init(args['JOB_NAME'], args)

# O path do s3
output_path = 's3://etl-desafio/Refined/Parquet/2023/09/28/'

# As variáveis com o nome das tabelas
source_tables = ['movies_parquet', 'series_parquet']
actors_views = ['dim_ator_actors', 'dim_departamento_actors', 'dim_filmes_actors', 'dim_genero_actors', 'dim_midia_actors', 'tabela_fato_actors']
genre_views = ['dim_data_genre', 'dim_genero_genre', 'dim_idioma_genre', 'dim_pais_genre', 'fatos_genre']

# O looping para criar os parquet's dos csv's
for table in source_tables:
    datasource = create_dynamic_frame(glueContext, 'tmdb_database', table)
    write_dynamic_frame(glueContext, datasource, output_path + 'CSV/')

# O looping para criar os parques do parquet actors
for view in actors_views:
    datasource = create_dynamic_frame(glueContext, 'tmdb_database', view)
    write_dynamic_frame(glueContext, datasource, output_path + 'actors')

# O looping para criar os parques do parquet genre
for view in genre_views:
    datasource = create_dynamic_frame(glueContext, 'tmdb_database', view)
    write_dynamic_frame(glueContext, datasource, output_path + 'genre')

job.commit()
