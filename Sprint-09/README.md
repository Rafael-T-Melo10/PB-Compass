# Descrição

Nesta sprint, continuamos a enfrentar os desafios que iniciamos na sprint anterior. Começamos com um exercício de modelagem de dados para aprimorar nossas habilidades. No início, realizamos um exercício de aquecimento, criando diagramas para representar a estrutura relacional e dimensional de um banco de dados. Em seguida, traduzimos esses diagramas em código SQL.

Após essa fase inicial, enfrentamos o desafio de tratar os dados em formato JSON que havíamos coletado na sprint anterior. Nosso objetivo era transformar esses dados em formato Parquet e remover qualquer informação não confiável. Essa etapa foi crucial para elevar nossos dados da camada "raw" para a camada "trusted", conforme estabelecido no Assignment 3.

No Assignment 4, aplicamos uma modelagem dimensional aos dados que tínhamos em mãos, permitindo-nos compreender melhor suas relações e estruturas. Finalmente, no Assignment 5, realizamos a última etapa de limpeza antes de transferir nossos dados para a camada "refined", garantindo que estivessem prontos e confiáveis para análises posteriores.

Essas atividades não apenas desafiaram nossas habilidades técnicas, mas também consolidaram nosso entendimento sobre a importância da qualidade e integridade dos dados em cada etapa do processo.

<details>
<summary>Seção 2</summary>

## Modelagem Relacional
Nessa etapa fizemos a modelagem relacional do banco de dados concessionaria, primeiro o diagrama depois o código SQL que criava as tabelas:

<img src="/Sprint-09/secao-2/diagrama_relacional.png" alt="Modelagem Relacional" width="1150" height="550">

~~~SQL
CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
)

INSERT OR IGNORE INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao

CREATE TABLE Combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
)

INSERT OR IGNORE INTO Combustivel (idCombustivel, tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao

CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    idCombustivel INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
)

INSERT OR IGNORE INTO Carro (idCarro, idCombustivel, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT idCarro, idCombustivel, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao

CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
)

INSERT OR IGNORE INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao

CREATE TABLE DetalhesLocacao (
    idLocacao INT,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    horaEntrega TIME,
    dataEntrega DATETIME,
    horaLocacao TIME,
    dataLocacao DATETIME,
    kmCarro INT,
    FOREIGN KEY (idLocacao) REFERENCES Locacao(idLocacao)
)

INSERT OR IGNORE INTO DetalhesLocacao (idLocacao, qtdDiaria, vlrDiaria, horaEntrega, dataEntrega, horaLocacao, dataLocacao, kmCarro)
SELECT idLocacao, qtdDiaria, vlrDiaria, horaEntrega, dataEntrega, horaLocacao, dataLocacao, kmCarro
FROM tb_locacao

CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCarro INT,
    idCliente INT,
    idVendedor INT,
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
)

INSERT OR IGNORE INTO Locacao (idLocacao, idCarro, idCliente, idVendedor)
SELECT idLocacao, idCarro, idCliente, idVendedor
FROM tb_locacao

~~~


## Modelagem Dimensional
Depois fizemos a modelagem dimensional do banco de dados concessionaria, primeiro o diagrama depois o código SQL que criava views:

<img src="/Sprint-09/secao-2/Diagrama_dimensional.png" alt="Modelagem Dimensional" width="1150" height="550">


~~~SQL
CREATE VIEW DimensaoVendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao

CREATE VIEW DimensaoCombustivel AS
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao

CREATE VIEW DimensaoCarro AS
SELECT C.idCarro, C.idCombustivel, C.classiCarro, C.marcaCarro, C.modeloCarro, C.anoCarro
FROM tb_locacao C
JOIN DimensaoCombustivel CF ON C.idCombustivel = CF.idCombustivel

CREATE VIEW DimensaoCliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao

CREATE VIEW DimensaoDataEntrega AS
SELECT
    dataEntrega,
    horaEntrega,
    CAST(substr(dataEntrega, 1, 4) AS INT) AS ano,
    CAST(substr(dataEntrega, 5, 2) AS INT) AS mes,
    CAST(substr(dataEntrega, 7, 2) AS INT) AS dia
FROM tb_locacao

CREATE VIEW DimensaoDataLocacao AS
SELECT
    dataLocacao,
    horaLocacao,
    CAST(substr(dataLocacao, 1, 4) AS INT) AS ano,
    CAST(substr(dataLocacao, 5, 2) AS INT) AS mes,
    CAST(substr(dataLocacao, 7, 2) AS INT) AS dia
FROM tb_locacao

CREATE VIEW FatosLocacao AS
SELECT L.idLocacao, L.idCarro, L.idCliente, L.idVendedor, L.horaEntrega,
        L.dataEntrega, L.horaLocacao, L.dataLocacao, L.kmCarro, l.qtdDiaria, L.vlrDiaria
FROM tb_locacao L
JOIN DimensaoCarro LC ON L.idCarro = LC.idCarro
JOIN DimensaoCliente CL ON L.idCliente = CL.idCliente
JOIN DimensaoVendedor V ON L.idVendedor = V.idVendedor


~~~

</details>

<details>
<summary>Seção 3</summary>

<details>
<summary>Assignment 3</summary>
Nesse assignment tivemos que pegar nossos json's e CSV's na camada raw, tratar os dados não confiáveis e colocar eles na camada trusted em formato parquet:

CSV ===> Parquet
~~~Python
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
~~~

JSON ===> Parquet

~~~Python
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
~~~
</details>


<details>
<summary>Assignment 4</summary>

No assignment 4 tivemos que pegar nossos dados da trusted e fazer a modelagem deles para depois colocarmos eles na refined:

### Modelagem do parquet Actors
<img src="/Sprint-09/secao-3/Assignment-4/modelo_dim_atores.png" alt="Modelagem Dimensional Atores" width="1150" height="550">

### Modelagem do parquet Genre
<img src="/Sprint-09/secao-3/Assignment-4/modelo_dim_genero.png" alt="Modelagem Dimensional Genero" width="1150" height="550">

</details>

<details>
<summary>Assignment 5</summary>

No assignment 5 tivemos que pegar os dados remodelados e coloca-los na refined, como eu fiz a modelagem dimensional pelo AWS Athena, onde as tabelas ja ficavam salvas no banco de dados do Glue, eu fiz um código com pyspark para pegar as tabelas criadas no Athena e coloca-lás na refined:

<img src="/Sprint-09/secao-3/Assignment-5/athena-tables.png" alt="athena-tables" width="450" height="750">

~~~Python
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

~~~
</details>


</details>
