-- SQLite
-- Exercício VIII

WITH vendas_count AS (
    SELECT
        vend.cdvdd,
        vend.nmvdd,
        count(ven.status) AS contagem
    FROM tbvendas AS ven
    LEFT JOIN tbvendedor AS vend
        ON vend.cdvdd = ven.cdvdd
    WHERE ven.status = 'Concluído' 
    GROUP BY vend.cdvdd, vend.nmvdd
)

SELECT 
    vendas_count.cdvdd,
    vendas_count.nmvdd
FROM vendas_count
WHERE contagem = (SELECT MAX(contagem) FROM vendas_count)

-- Exercício IX

WITH vendas_count AS (
    SELECT 
        pro.cdpro,
        ven.nmpro,
        count(ven.qtd) AS quantidade 
    FROM tbestoqueproduto AS pro
    LEFT JOIN tbvendas AS ven
        ON ven.cdpro = pro.cdpro
    WHERE ven.dtven BETWEEN '2014-02-03' AND '2018-02-02'
    GROUP BY ven.qtd
)

SELECT 
    vendas_count.cdpro,
    vendas_count.nmpro
FROM vendas_count
WHERE quantidade = (SELECT MAX(quantidade) FROM vendas_count)

-- Exercício X

SELECT 
    vend.nmvdd as vendedor,
    sum(ven.qtd * ven.vrunt ) AS valor_total_vendas,
    round((sum(ven.qtd * ven.vrunt ) * vend.perccomissao * 0.01), 2) AS comissao
FROM tbvendedor AS vend
LEFT JOIN tbvendas AS ven
    ON vend.cdvdd = ven.cdvdd
    AND ven.status = 'Concluído'
GROUP BY vend.nmvdd
ORDER BY comissao DESC
 
-- Exercício XI

WITH produt_count AS (
    SELECT
        ven.cdcli,
        ven.nmcli,
        sum(ven.qtd * ven.vrunt ) AS gasto
    FROM tbvendas as ven
    WHERE ven.status = 'Concluído'
    GROUP BY ven.cdcli
)
SELECT
    produt_count.cdcli,
    produt_count.nmcli,
    produt_count.gasto
FROM produt_count
where gasto = (SELECT MAX(gasto) FROM produt_count)
 
-- Exercício XII

WITH depend_count AS(
    SELECT
        dep.cddep,
        dep.nmdep,
        dep.dtnasc,
        sum(ven.qtd * ven.vrunt ) AS valor_total_vendas
    FROM tbdependente AS dep
    LEFT JOIN tbvendas AS ven
        ON ven.cdvdd = dep.cdvdd
    WHERE ven.status = 'Concluído'
    GROUP BY ven.cdvdd
)
SELECT 
    depend_count.cddep,
    depend_count.nmdep,
    depend_count.dtnasc,
    depend_count.valor_total_vendas
FROM depend_count
WHERE valor_total_vendas =  (SELECT MIN(valor_total_vendas) FROM depend_count)
 
-- Exercício XIII

with canal_count AS(
    SELECT
        ven.cdpro,
        ven.nmcanalvendas,
        ven.nmpro,
        count(ven.cdpro) AS quantidade_vendas
    FROM tbvendas AS ven
    WHERE ven.status = 'Concluído'
    GROUP BY ven.cdpro
)
SELECT 
    canal_count.cdpro
    canal_count.nmcanalvendas
    canal_count.nmpro
    canal_count.quantidade_vendas
FROM canal_count
WHERE 




SELECT *
FROM tbvendedor
SELECT *
FROM tbdependente
SELECT *
FROM tbestoqueproduto
SELECT *
FROM tbvendas
