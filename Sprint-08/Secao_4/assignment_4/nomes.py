from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, udf, rand, when
from pyspark.sql.types import StringType
import random

spark = SparkSession.builder.appName('Exercicio 1').getOrCreate()

# As variáveis 
nome_arquivo_txt = 'nomes_aleatorios.txt'
escolaridade = ['Fundamental', 'Medio ', 'Superior']
pais = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 'Guiana' 'Francesa' ]

# As gerações
baby_boomers = (1944, 1964)
generation_x = (1965, 1979)
millennials = (1980, 1994)
generation_z = (1995, 2015)

# Criando um dataframe com os dados do csv
df_nomes = spark.read.csv(nome_arquivo_txt)
df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')
df_nomes.show(10)
df_nomes.printSchema()

# A função que coloca a escolaridade de forma aleatória
def add_random_escolaridade():
  return random.choice(escolaridade)
add_random_escolaridade_udf = udf(add_random_escolaridade, StringType())

# A função que coloca o país de forma aleatória
def add_random_pais():
  return random.choice(pais)
add_random_pais_udf = udf(add_random_pais, StringType())

# Adicionando a escolaridade, país e ano no dataframe
df_nomes = df_nomes.withColumn('Escolaridade', add_random_escolaridade_udf())
df_nomes = df_nomes.withColumn('Pais', add_random_pais_udf())
df_nomes = df_nomes.withColumn('AnoNascimento', (rand() * (2010 - 1945) + 1945).cast('int'))

# Criando um novo dataframe somente com os valores de ano de nascimento acima de 2000
df_select = df_nomes.filter(df_nomes['AnoNascimento'] >= 2001)
df_select.show(10)
df_select.printSchema()

# Fazendo a filtragem de pessoas nascidas a partir de 2000 com SQL
df_nomes.createOrReplaceTempView ('pessoas')
spark.sql('SELECT * FROM pessoas WHERE AnoNascimento >= 2001').show(10)

# Filtrando a geração millennial
df_nomes.filter((df_nomes['AnoNascimento'] >= 1980) & (df_nomes['AnoNascimento'] <= 1994)).show(10)

# Filtrando a geração millennial com SQL
spark.sql('SELECT * FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994').show(10)

# Criando um dataframe com uma coluna filtrando a geração de cada pessoa
df_geracao = df_nomes.withColumn(
    'Geracao',
    when(
        (col('AnoNascimento') >= baby_boomers[0]) & (col('AnoNascimento') <= baby_boomers[1]),
        'Baby Boomers'
    )
    .when(
        (col('AnoNascimento') >= generation_x[0]) & (col('AnoNascimento') <= generation_x[1]),
        'Generation X'
    )
    .when(
        (col('AnoNascimento') >= millennials[0]) & (col('AnoNascimento') <= millennials[1]),
        'Millennials'
    )
    .when(
        (col('AnoNascimento') >= generation_z[0]) & (col('AnoNascimento') <= generation_z[1]),
        'Generation Z'
    )
    .otherwise('Outra')
)

# Criando a coluna pessoas_com_geracao para colocar em que geração ela nasceu
df_geracao.createOrReplaceTempView('pessoas_com_geracao')
query = '''
    SELECT Pais, Geracao, COUNT(*) AS Quantidade
    FROM pessoas_com_geracao
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao
'''

df_resultado = spark.sql(query)
df_resultado.show()