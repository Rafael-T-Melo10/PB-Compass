-- SQLite
-- Exercício I

SELECT *
FROM livro
WHERE publicacao > '2014-12-31'
ORDER BY cod 

-- Exercício II

SELECT 
    titulo, 
    valor
FROM livro
ORDER BY valor DESC
LIMIT 10

-- Exercício III

SELECT 
    edit.nome,
    ende.cidade,
    ende.estado,
    count(liv.titulo) AS quantidade
FROM editora AS edit
LEFT JOIN endereco AS ende
    ON edit.endereco = ende.codendereco
LEFT JOIN livro AS liv
    ON edit.codeditora = liv.editora
GROUP BY edit.nome
HAVING quantidade > 0
ORDER BY quantidade DESC
LIMIT 5

-- Exercício IV

SELECT 
    aut.nome, 
    aut.codautor,
    aut.nascimento,
    count(liv.titulo) AS quantidade
FROM autor AS aut
LEFT JOIN livro AS liv
    ON aut.codautor = liv.autor
GROUP BY aut.nome
ORDER BY aut.nome

-- Exercício V

SELECT DISTINCT aut.nome
FROM livro AS liv
JOIN autor AS aut ON liv.autor = aut.codautor
JOIN editora AS edit ON liv.editora = edit.codeditora
JOIN endereco AS ende ON edit.endereco = ende.codendereco
WHERE ende.estado NOT IN ('PARANÁ', 'RIO GRANDE DO SUL')
ORDER BY aut.nome 

-- Exercício VI

SELECT
    aut.nome,
    aut.codautor,
    count(titulo) AS quantidade_publicacoes 
FROM autor AS aut
LEFT JOIN livro AS liv
    ON aut.codautor = liv.autor
GROUP BY aut.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1

-- Exercício VII

SELECT
    aut.nome
FROM autor AS aut
LEFT JOIN livro AS liv
    ON aut.codautor = liv.autor
GROUP BY aut.nome
HAVING count(titulo) = 0
ORDER BY aut.nome 