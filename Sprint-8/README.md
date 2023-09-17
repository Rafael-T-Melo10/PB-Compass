# Descrição

Durante esta sprint, demos início ao nosso projeto para concluir o programa de bolsas. Primeiramente, criamos nossa conta no TMBD e cuidadosamente selecionamos os conjuntos de dados que seriam fundamentais nas próximas etapas. Recebemos orientações para escolher com precisão nossos objetivos antes de fazer nossas escolhas. Com isso em mente, optei por realizar uma análise centrada nos meus atores e dubladores favoritos: Jack Black e Dwayne Johnson. Ambos desempenharam papéis essenciais em filmes de animação que são os meus favoritos, bem como em outras produções muito engraçadas. Minha abordagem envolverá a comparação das performances de dublagem desses dois talentosos artistas e a atribuição de notas com base nesse critério.

<details>
<summary>Seção 2</summary>

# Testando a API

~~~Python
# Esse foi o código da seção 2 da sprint 8
import requests
import pandas as pd

from IPython.display import display

# Aqui conecta com a API
api_key = '57435fa8f5ab634ed0c829d299830df1'

url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR'

response = requests.get(url)

# Aqui pega a resposta da API e salva em uma variável
data = response.json()
filmes = []

# Aqui pega todos os itens na variável data e os coloca em formato de dicionário para depois dar append na lista filme
for movie in data['results']:
    df = {'Titulo': movie['title'],
    'Data de lançamento': movie['release_date'],
    'Visão geral': movie['overview'],
    'Votos': movie['vote_count'],
    'Média de votos:': movie['vote_average']}

    filmes.append(df)

# Aqui mostra um dataframe da lista filmes
df = pd.DataFrame(filmes)
display(df)

~~~
</details>

<details>
<summary>Seção 3</summary>

# Fazendo os requests:

~~~Python
# Fazendo um for para fazer um request por nome na lista actors
for actor in actors:
  url = f'{base_url}/search/person?api_key={api_key}&query={actor}&include_adult=false&language=en-US&page=1'
  response = requests.get(url, headers=headers)
  data = response.json()
  results_actors.append(data)

# O request que pega todos os filmes com os generos 16 e 35 (Animação e Comédia)
url = f'{base_url}/discover/tv?api_key={api_key}&include_adult=false&include_null_first_air_dates=false&language=en-US&page=1sort_by=popularity.desc&with_genres=16%2C35'
response = requests.get(url, headers=headers)
data = response.json()
results_genres.append(data)
~~~

# a dockerfile que faz a layer:

~~~Dockerfile
FROM amazonlinux:2.0.20200602.0
RUN yum update -y
RUN yum install -y \
python3-pip \
zip \
RUN yum -y clean all
RUN python3.7 -m pip install --upgrade pip
~~~

# Os comandos para rodar a dockerfile:

## Criando a imagem
~~~
docker build -t amazonlinuxpython37 .
~~~

## Rodando a imagem
~~~
docker run -it amazonlinuxpython37 bash
~~~

## Criando a layer
~~~
cd ~
mkdir layer_dir
cd layer_dir/
mkdir python
cd python/
pwd
~~~

## Baixando as bibliotecas
~~~
pip3 install requests
pip3 install json
~~~

</details>

<details>
<summary>Seção 4</summary>

# Criando o arquivos nomes_aleatorios:

~~~Python
import names
import time
import random

# Criando a lista de nomes
random.seed(40)

qtd_nomes_unicos = 3000

qtd_nomes_aleatorios = 10000000

nome_arquivo_txt = 'nomes_aleatorios.txt'

aux=[]

for i in range(0, qtd_nomes_unicos):

    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados=[]

# Colocando os nomes na lista dados
for i in range(0,qtd_nomes_aleatorios):

    dados.append(random.choice(aux))

# Escrevendo um txt com os nomes
with open(nome_arquivo_txt, mode='w', newline='') as arquivo_txt_lab:

    for dado in dados:
        arquivo_txt_lab.write(dado + '\n')
~~~
# Criando o csv com os animais
~~~Python
# Lista de animais

list_anim = ['Cachorro', 'Gato', 'Elefante', 'Leão', 'Tigre', 'Girafa', 'Zebra', 'Urso', 'Canguru',
             'Rinoceronte', 'Hipopótamo', 'Coelho', 'Pinguim', 'Golfinho', 'Arara', 'Coruja', 'Sapo', 'Cobra', 'Peixe', 'Tartaruga' ]
nome_arquivo = "animais.csv"

list_anim.sort()

# Criando um csv com os nomes da lista animal 
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    for animal in list_anim:
        escritor_csv.writerow([animal])
~~~

# Pegando a lista de nomes aleatorios e transformando em dataframe:

~~~Python
nome_arquivo_txt = 'nomes_aleatorios.txt'

df_nomes = spark.read.csv(nome_arquivo_txt)
df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')
df_nomes.show(10)
df_nomes.printSchema()
~~~

# Fazendo uma coluna com as escolaridades aleatórias:  

~~~Python
escolaridade = ['Fundamental', 'Medio ', 'Superior']

def add_random_escolaridade():
  return random.choice(escolaridade)
add_random_escolaridade_udf = udf(add_random_escolaridade, StringType())

df_nomes = df_nomes.withColumn('Escolaridade', add_random_escolaridade_udf())
~~~

# Fazendo uma coluna com os países aleatórios:  

~~~Python
pais = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 'Guiana' 'Francesa' ]

def add_random_pais():
  return random.choice(pais)
add_random_pais_udf = udf(add_random_pais, StringType())

df_nomes = df_nomes.withColumn('Pais', add_random_pais_udf())
~~~

# Fazendo coluna com os anos de nascimento aleatórios:

~~~Python
df_nomes = df_nomes.withColumn('AnoNascimento', (rand() * (2010 - 1945) + 1945).cast('int'))
~~~

# Fazendo um novo dataframe somente com os valores de ano de nascimento acima de 2000 em pyspark e SQL:

~~~Python
df_select = df_nomes.filter(df_nomes['AnoNascimento'] >= 2001)
df_select.show(10)
df_select.printSchema()
df_nomes.createOrReplaceTempView ('pessoas')
spark.sql('SELECT * FROM pessoas WHERE AnoNascimento >= 2001').show(10)

~~~

# Filtrando a geração millennial com pyspark e SQL:

~~~Python
df_nomes.filter((df_nomes['AnoNascimento'] >= 1980) & (df_nomes['AnoNascimento'] <= 1994)).show(10)
spark.sql('SELECT * FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994').show(10)
~~~

#  Criando um dataframe com uma coluna filtrando a geração de cada pessoa com pyspark e SQL:

~~~Python
baby_boomers = (1944, 1964)
generation_x = (1965, 1979)
millennials = (1980, 1994)
generation_z = (1995, 2015)

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

df_geracao.createOrReplaceTempView('pessoas_com_geracao')
query = '''
    SELECT Pais, Geracao, COUNT(*) AS Quantidade
    FROM pessoas_com_geracao
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao
'''

df_resultado = spark.sql(query)
df_resultado.show()
~~~
</details>
