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
