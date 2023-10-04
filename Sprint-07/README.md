# Descrição

 Durante esta sprint, tive a valiosa oportunidade de expandir meus conhecimentos ao aprender sobre Hadoop e Spark utilizando Python, com destaque para o uso do PySpark. Além disso, pude aprimorar ainda mais minhas habilidades em AWS, Python e Docker, aplicando-as de forma prática e eficaz.

 - Na seção 1 nos recebemos as orientações sobre os exercícios  
 - Na seção 2 nos tivemos que ler um pdf de resumo sobre hadoop e spark e outro sobre as bibliotecas numpy e pandas e ETL/ELT
 - Na seção 3 nos tivemos que fazer uma tarefa com 4 exercícios sobre pandas e numpy
 - Na seção 4 nos fizemos um lab do glue
 - Na seção 5 nos fizemos um desafio de ETL usando docker e python

<details>
<summary>Seção 3</summary>

# Python com Pandas e Numpy

## Parte 1: Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes

~~~python
import pandas as pd

data_frame = pd.read_csv('actors.csv')
# print(data_frame.head())

maior_filme = data_frame['Number of Movies'].idxmax()
filmes_max = data_frame.loc[maior_filme, 'Number of Movies']
ator_max = data_frame.loc[maior_filme, 'Actor']
print(f'O ator com o maior número de filmes é {ator_max}, com {filmes_max} filmes')
~~~

A saida dele foi: O ator com o maior número de filmes é Robert DeNiro, com 79 filmes

## Parte 2: Apresente a média da coluna contendo o número de filmes

~~~python
import pandas as pd

data_frame = pd.read_csv('actors.csv')
print(data_frame.head())
media_filmes = data_frame['Number of Movies'].mean()
print(f'A média é {media_filmes}')
~~~

A saida dele foi: A média é 37.88

## Parte 3: Apresente o nome do ator/atriz com a maior média por filme

~~~python
import pandas as pd

data_frame = pd.read_csv('actors.csv')
print(data_frame.head())
maior_media = data_frame['Average per Movie'].idxmax()
media_ator_max = data_frame.loc[maior_media, 'Average per Movie']
ator_media_max = data_frame.loc[maior_media, 'Actor']
print(f'O ator com a maior média por filmes é {ator_media_max}, com {media_ator_max} de média')
~~~

A saida dele foi: O ator com a maior média por filmes é Anthony Daniels, com 451.8 de média

## Parte 4: Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência

~~~python
import pandas as pd

data_frame = pd.read_csv('actors.csv')
print(data_frame.head())
filme_frequente = data_frame['#1 Movie'].value_counts().head(5)
print(filme_frequente)
~~~

A saida dele foi: 
#1 Movie

The Avengers 6 vezes

Catching Fire 4 vezes

Harry Potter / Deathly Hallows (P2) 4 vezes

Star Wars: The Force Awakens 3 vezes

The Dark Knight 3 vezes

# Apache Spark

## Parte 1: Realizar o pull da imagem jupyter/all-spark-notebook

~~~
docker pull jupyter/all-spark-notebook
~~~
Um docker pull para baixar a imagem do jupyter

## Parte 2: Criar um container a partir da imagem

~~~
docker run -it -p 8888:8888 jupyter/all-spark-notebook 
~~~

Um docker run para criar o conteiner

## Parte 3: Em outro terminal, execute o comando `pyspark` no seu container. Pesquise sobre o comando  docker exec para realizar esta ação. Utilize as flags -i e -t no comando.

~~~
docker exec -i -t quirky_torvalds pyspark
~~~

Um docker exec para rodar o pyspark no conteiner

~~~Python
from pyspark.sql.functions import split, size
file_name = 'README.md'
df = spark.read.text(file_name)
df_contagem_palavras = df.select(size(split(df.value, '/s+')).alias('contagem_palavras'))
df_contagem_palavras = df.select(size(split(df.value, '\s+')).alias("word_count"))
contagem_total = df_contagem_palavras.agg({'word_count':'sum'}).collect()[0][0]
print('total de palavras é:', contagem_total)

~~~

A sequência de comandos usado no pyspark para pegar o total de palavras no meu README

<img src="/Sprint-7/Secao_3/imgs/Spark_Jupyter.png" alt="Spark_Jupyter" width="1000" height="200">

</details>

<details>
<summary>Seção 4</summary>

# Lab-Glue

## Parte 1: Preparando os dados de origem

Fizemos o upload do arquivo nomes.csv para o bucket s3
<img src="/Sprint-7/Secao_4/imgs/bucket_input.png" alt="bucket_input" width="1000" height="200">

## Parte 2: Configurando sua conta para utilizar o AWS Glue

Demos permissão para o usuário usar o glue
<img src="/Sprint-7/Secao_4/imgs/permissao_user.png" alt="permissao_user" width="1000" height="200">

## Parte 3: Criando a IAM Role para os jobs do AWS Glue

Criamos a role no IAM
<img src="/Sprint-7/Secao_4/imgs/iam_role.png" alt="iam_role" width="1000" height="200">

## Parte 4: Configurando as permissões no AWS Lake Formation

Demos a permissão no lake formation
<img src="/Sprint-7/Secao_4/imgs/lake_formation.png" alt="lake_formation" width="1000" height="200">

## Parte 5: Criando novo job no AWS Glue

Criamos um novo job no aws glue
<img src="/Sprint-7/Secao_4/imgs/job_no_glue.png" alt="job_no_glue" width="1000" height="200">

### Parte 5.1: Somente eliminar os jobs

### Parte 5.2: Sua vez!

Nessa parte tivemos que fazer 7 consultas usando o nomes.csv:

1: Imprima o schema do dataframe gerado no passo anterior

2: Imprimir a contagem de linhas presentes no dataframe

3: Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe

4: Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.

5: Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu

6: Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe.
Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente

7: Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3.
    Atenção aos requisitos:
        A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do path s3://<BUCKET>/lab-glue/
        O formato deve ser JSON
        O particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem)

Primeiro:
~~~Python
df.printSchema()
~~~
Saida:
|-- nome: string
|-- sexo: string
|-- total: string
|-- ano: string

Segundo:
~~~Python
line_count = df_sp.count()
print("Número de linhas no DataFrame:", line_count)
~~~
Saida:
Número de linhas no DataFrame: 1825433

Terceiro:
~~~Python
count_by_year_sex = df_sp.groupBy("ano").pivot("sexo").count().orderBy(desc('ano'))
~~~
Saida:
+----+-----+-----+
| ano|    F|    M|
+----+-----+-----+
|2014|19067|13977|
|2013|19191|14012|
|2012|19468|14216|
|2011|19540|14329|
|2010|19800|14241|
|2009|20165|14519|
|2008|20439|14606|
|2007|20548|14383|
|2006|20043|14026|
|2005|19175|13358|
|2004|18819|13216|
|2003|18423|12750|
|2002|18081|12479|
|2001|17966|12295|
|2000|17652|12111|
|1999|16938|11606|
|1998|16593|11298|
|1997|16155|10810|
|1996|15889|10530|
|1995|15754|10326|
+----+-----+-----+
only showing top 20 rows

Quarto:
~~~Python
df_feminino = df_sp.filter(col("sexo") == "F").orderBy(desc('total')).limit(1)
df_feminino.show()
~~~
Saida:
+-----+----+-----+----+
| nome|sexo|total| ano|
+-----+----+-----+----+
|Linda|   F|99680|1947|
+-----+----+-----+----+


Quinto:
~~~Python
df_masculino = df_sp.filter(col("sexo") == "M").orderBy(desc('total')).limit(1)
df_masculino.show()
~~~
Saida:
+-----+----+-----+----+
| nome|sexo|total| ano|
+-----+----+-----+----+
|James|   M|94755|1947|
+-----+----+-----+----+

Sexto:
~~~Python
count_by_year_sex_ = total_df.groupBy("ano").sum("total").orderBy("ano").limit(10)
count_by_year_sex_.show()
~~~
Saida:
+----+----------+
| ano|sum(total)|
+----+----------+
|1880|    201484|
|1881|    192699|
|1882|    221538|
|1883|    216950|
|1884|    243467|
|1885|    240855|
|1886|    255319|
|1887|    247396|
|1888|    299480|
|1889|    288950|
+----+----------+


Setimo:
~~~Python
nomes_upper = df.withColumn("nome", upper(col("nome")))
nomes_upper_sp = nomes_upper.toDF()
# Printando os nomes em maiúsculo separando em pastas
nomes_upper_sp.write.partitionBy('sexo','ano').json(target_path, mode="append")

job.commit()
~~~
Saida:
<img src="/Sprint-7/Secao_4/imgs/saida_7.png" alt="saida_7" width="1000" height="200">
<img src="/Sprint-7/Secao_4/imgs/saida_7_M.png" alt="saida_7_M" width="1000" height="200">
<img src="/Sprint-7/Secao_4/imgs/saida_7_F.png" alt="saida_7_F" width="1000" height="200">

As Saidas de cada um foram pegas do log do AWS Glue com exceção da saida 7 que criou uma pasta no s3

## Parte 6: Criando novo crawler

Criamos um crawler
<img src="/Sprint-7/Secao_4/imgs/Crawler.png" alt="Crawler" width="1000" height="200">

</details>


<details>
<summary>Seção 5</summary>

# ETL-Desafio

## Parte 1: Implementar código Python:
Primeiro criamos um arquivo python para ler os csv's sem filtrar os dados, utilizamos a lib Boto3 para carragar na AWS e gravamos no S3 os csv's

~~~Python
import boto3
import os
csv_series = 'series.csv'
csv_movies = 'movies.csv'
bucket_name = 'etl-desafio'
file_path_movies = 'Raw/Local/CSV/Movies/2023/09/01/'
file_path_series = 'Raw/Local/CSV/Series/2023/09/01/'

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token_key = os.getenv('AWS_SESSION_TOKEN')
s3 = boto3.client('s3', aws_access_key_id = aws_access_key, aws_secret_access_key = aws_secret_key, aws_session_token = aws_session_token_key)

s3.upload_file(csv_series, bucket_name,file_path_series + csv_series)
s3.upload_file(csv_movies, bucket_name,file_path_movies + csv_movies)

~~~
## Parte 2:Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado

Depois criamos um arquivo Dokerfile para carregar um cointeiner para implementar o arquivo python
~~~Dockerfile
FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install boto3

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
ENV AWS_SESSION_TOKEN=

CMD ["python", "etl.py"]
~~~
## Parte 3:Executar localmente o container docker para realizar a carga dos dados ao S3
Usamos os comando a segui para executar o docker:

~~~
docker build -t etl.py .
docker run etl.py
~~~

Como os arquivos csv's superam o limite do github e não foi dito se precisavamos ou não do volume do docker preferi deixar sem eles aqui até receber a resposta

</details>