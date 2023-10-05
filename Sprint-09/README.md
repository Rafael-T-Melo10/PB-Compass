# Descrição

Nesta sprint, continuamos a enfrentar os desafios que iniciamos na sprint anterior. Começamos com um exercício de modelagem de dados para aprimorar nossas habilidades. No início, realizamos um exercício de aquecimento, criando diagramas para representar a estrutura relacional e dimensional de um banco de dados. Em seguida, traduzimos esses diagramas em código SQL.

Após essa fase inicial, enfrentamos o desafio de tratar os dados em formato JSON que havíamos coletado na sprint anterior. Nosso objetivo era transformar esses dados em formato Parquet e remover qualquer informação não confiável. Essa etapa foi crucial para elevar nossos dados da camada "raw" para a camada "trusted", conforme estabelecido no Assignment 3.

No Assignment 4, aplicamos uma modelagem dimensional aos dados que tínhamos em mãos, permitindo-nos compreender melhor suas relações e estruturas. Finalmente, no Assignment 5, realizamos a última etapa de limpeza antes de transferir nossos dados para a camada "refined", garantindo que estivessem prontos e confiáveis para análises posteriores.

Essas atividades não apenas desafiaram nossas habilidades técnicas, mas também consolidaram nosso entendimento sobre a importância da qualidade e integridade dos dados em cada etapa do processo.

<details>
<summary>Seção 2</summary>

## Modelagem Relacional
Nessa etapa fizemos a modelagem relacional do banco de dados concessionaria, primeiro o diagrama depois o código SQL que criava as tabelas:

<img src="/Sprint-09/secao-2/diagrama_relacional.png" alt="Modelagem Relacional" width="250" height="250">

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

<img src="/Sprint-09/secao-2/Diagrama_dimensional.png" alt="Modelagem Dimensional" width="750" height="450">


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