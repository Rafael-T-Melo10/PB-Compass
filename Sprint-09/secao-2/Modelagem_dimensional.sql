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

