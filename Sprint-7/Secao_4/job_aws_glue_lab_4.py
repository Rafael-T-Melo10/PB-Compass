import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, count, max, row_number, desc, asc
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
from pyspark.sql.types import IntegerType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options("s3", {"paths": [ source_file ] }, "csv", {"withHeader": True, "separator":","} )
df_sp = df.toDF()
total_df = df_sp.withColumn('total', col('total').cast(IntegerType()))
df_sp = total_df.withColumn('ano', col('ano').cast('int'))

# Filtrar registros apenas para sexo feminino
df_feminino = df_sp.filter(col("sexo") == "F").orderBy(desc('total')).limit(1)
df_feminino.show()

# Filtrar registros apenas para sexo masculino
df_masculino = df_sp.filter(col("sexo") == "M").orderBy(desc('total')).limit(1)
df_masculino.show()

# Print do schema
df.printSchema()

# Imprimindo a contagem de linahs
line_count = df_sp.count()
print("Número de linhas no DataFrame:", line_count)

# Contagem de nomes agrupados por 'ano' e 'sexo'
count_by_year_sex = df_sp.groupBy("ano").pivot("sexo").count().orderBy(desc('ano'))

# Imprimir os resultados
count_by_year_sex.show()

count_by_year_sex_ = total_df.groupBy("ano").sum("total").orderBy("ano").limit(10)
count_by_year_sex_.show()

# Colocando os nomes em maiúsculo
nomes_upper = df.withColumn("nome", upper(col("nome")))
nomes_upper_sp = nomes_upper.toDF()
# Printando os nomes em maiúsculo separando em pastas
nomes_upper_sp.write.partitionBy('sexo','ano').json(target_path, mode="append")

job.commit()