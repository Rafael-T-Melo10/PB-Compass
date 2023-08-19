# Descrição

Nesta sprint, o nosso foco principal foi aprofundar significativamente o nosso conhecimento na plataforma AWS. Ao mesmo tempo, aplicamos os conceitos que havíamos aprendido em sprints anteriores, como a manipulação de arquivos CSV na fase do S3, a utilização de SQL durante a etapa no AWS Athena, e a implementação de Docker na fase da Lambda.

Durante esse período, fui apresentado a novas ferramentas essenciais da AWS, incluindo o Amazon Kinesis, Elastic MapReduce (EMR), Amazon QuickSight e Redshift, entre outras. A experiência foi enriquecedora, ampliando meu leque de habilidades na utilização da plataforma.

Destaco também a contribuição fundamental do nosso instrutor, Marcos. Sua orientação especializada desempenhou um papel crucial no aprofundamento do meu entendimento sobre a certificação de Cloud Practitioner da AWS. Além disso, tive a oportunidade de participar de diversos PartnerCasts, o que me permitiu realizar simulações práticas e explorar o banco de questões da AWS de maneira mais abrangente, solidificando assim o meu conhecimento.

Essa sprint nenhum curso me deu certificado então coloquei as provas, em formato de print, na pasta de certificados.

<details>
<summary>Amazon S3</summary>

Nesse exercício de S3 tive que criar um Bucket para habilitar a hospedagem de site estático, e liberar as configurações de acesso público, após liberar o acesso tive que adicionar uma política de no bucket, adicionei um documento de erro para as notificações e testei o site

## Etapa 1:Criar um bucket
<img src="/Sprint-6/s3/fotos/etapa-1-s3.png" alt="etapa-1-s3" width="1000" height="200">

## Etapa 2: Habilitar hospedagem de site estático
<img src="/Sprint-6/s3/fotos/etapa-2-s3.png" alt="etapa-2-s3" width="1000" height="200">

## Etapa 3: editar as configurações do Bloqueio de acesso público
<img src="/Sprint-6/s3/fotos/etapa-3-s3.png" alt="etapa-3-s3" width="1000" height="200">

## Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível

~~~json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::Bucket-Name/*"
            ]
        }
    ]
}
~~~

## Etapa 5: Configurar um documento de índice
<img src="/Sprint-6/s3/fotos/etapa-5-s3.png" alt="etapa-5-s3" width="1000" height="400">

~~~html
<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>Home Page do meu WebSite - Tutorial de S3</title>
</head>
<body>
  <h1>Bem-vindo ao meu website</h1>
  <p>Agora hospedado em Amazon S3!</p>
  <a href="nome do arquivo CSV a ser baixado">Download CSV File</a> 
</body>
</html
~~~

## Etapa 6: configurar documento de erros
<img src="/Sprint-6/s3/fotos/etapa-6-s3.png" alt="etapa-6-s3" width="1000" height="400">

## Etapa 7: testar o endpoint do site
<img src="/Sprint-6/s3/fotos/etapa-7-s3.png" alt="etapa-7-s3" width="1000" height="300">
</details>

<details>
<summary>Amazon Athena</summary>

Nesse exercício do Amazon Athena tive que criar um banco de dados, criar uma tabela, abrir o CSV e usar o Athena para criar queries de sql para buscar informações no CSV.<br>
Junto com as queries eu coloquei os CSVs com as saídas delas.

## Etapa 1: Configurar Athena
<img src="/Sprint-6/athena/fotos/etapa-1-athena.png" alt="etapa-1-athena" width="1000" height="300">

~~~sql
CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes (
nome STRING,
sexo STRING,
total INT,
ano INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION 's3://etapa1/dados/'
~~~
## Etapa 2: Criar um banco de dados
<img src="/Sprint-6/athena/fotos/etapa-2-athena.png" alt="etapa-2-athena" width="1000" height="300">

~~~sql
select nome 
from meubanco.nomes 
where ano = 1999 
order by total 
limit 15
~~~

## Etapa 3: Criar uma tabela
<img src="/Sprint-6/athena/fotos/etapa-3-athena.png" alt="etapa-3-athena" width="1000" height="300">

~~~sql
WITH Decades AS (
	SELECT DISTINCT FLOOR(ano / 10) * 10 AS decade
	FROM nomes
	WHERE ano >= 1950
),
RankedNames AS (
	SELECT FLOOR(n.ano / 10) * 10 AS decade,
		n.nome,
		SUM(n.total) AS total_ocorrencias,
		RANK() OVER(
			PARTITION BY FLOOR(n.ano / 10) * 10
			ORDER BY SUM(n.total) DESC
		) AS rank
	FROM nomes n
		JOIN Decades d ON FLOOR(n.ano / 10) * 10 = d.decade
	GROUP BY FLOOR(n.ano / 10) * 10,
		n.nome
)
SELECT decade,
	nome,
	total_ocorrencias
FROM RankedNames
WHERE rank <= 3
ORDER BY decade,
	rank
~~~
</details>


<details>
<summary>Amazon Lambda</summary>

Nesse exercício do Amazon Lambda tive que criar uma função lambda, construir o código, criar uma layer e colocar em prática
 
## Etapa 1: Criar a função do Lambda
<img src="/Sprint-6/lambda/fotos/etapa-1-lambda.png" alt="etapa-1-lambda" width="1000" height="300">

## Etapa 2: Construir o código
<img src="/Sprint-6/lambda/fotos/etapa-2-lambda.png" alt="etapa-2-lambda" width="1000" height="300">

## Etapa 3: Criar uma Layer
<img src="/Sprint-6/lambda/fotos/etapa-3-lambda.png" alt="etapa-3-lambda" width="1000" height="300">

## Etapa 4: Utilizando a Layer
<img src="/Sprint-6/lambda/fotos/etapa-4-lambda.png" alt="etapa-4-lambda" width="1000" height="300">

</details>
