-- SQLite --
-- Exercício VIII --

WITH vendas_count AS (
    SELECT
        vend.cdvdd,
        vend.nmvdd,
        COUNT(ven.status) AS contagem
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

-- Exercício IX --

WITH vendas_count AS (
    SELECT 
        pro.cdpro,
        ven.nmpro,
        COUNT(ven.qtd) AS quantidade 
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

-- Exercício X --

SELECT 
    vend.nmvdd as vendedor,
    SUM(ven.qtd * ven.vrunt ) AS valor_total_vendas,
    ROUND((SUM(ven.qtd * ven.vrunt ) * vend.perccomissao * 0.01), 2) AS comissao
FROM tbvendedor AS vend
LEFT JOIN tbvendas AS ven
    ON vend.cdvdd = ven.cdvdd
    AND ven.status = 'Concluído'
GROUP BY vend.nmvdd
ORDER BY comissao DESC
 
-- Exercício XI --

WITH produt_count AS (
    SELECT
        ven.cdcli,
        ven.nmcli,
        SUM(ven.qtd * ven.vrunt ) AS gasto
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
 
-- Exercício XII --

WITH depend_count AS(
    SELECT
        dep.cddep,
        dep.nmdep,
        dep.dtnasc,
        SUM(ven.qtd * ven.vrunt ) AS valor_total_vendas
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
 
-- Exercício XIII --

with canal_count AS(
    SELECT
        ven.cdpro,
        ven.nmcanalvendas,
        ven.nmpro,
        SUM(ven.qtd) AS quantidade_vendas
    FROM tbvendas AS ven
    WHERE ven.status = 'Concluído'
    GROUP BY ven.cdpro, ven.nmcanalvendas
)
SELECT 
    canal_count.cdpro,
    canal_count.nmcanalvendas,
    canal_count.nmpro,
    canal_count.quantidade_vendas
FROM canal_count
WHERE canal_count.nmcanalvendas IN ('Matriz', 'Ecommerce')
ORDER BY canal_count.quantidade_vendas
 
-- Exercício XIV --

SELECT
    estado,
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado
ORDER BY gastomedio desc
 
-- Exercício XV --

SELECT cdven
FROM tbvendas
WHERE deletado = 1
ORDER BY cdven ASC

-- Exercício XVI --

SELECT
    estado,
    nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM tbvendas  
WHERE status = 'Concluído'
GROUP BY estado, nmpro
ORDER BY estado, nmpro ASC
