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
</details>

<details>
<summary>Seção 4</summary>

# Lab-Glue

</details>