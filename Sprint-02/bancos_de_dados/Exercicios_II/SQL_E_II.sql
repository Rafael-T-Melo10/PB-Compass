-- SQLite --
-- Questão 1 --
SELECT 
    titulo, 
    valor
FROM livro
ORDER BY valor DESC
LIMIT 10

-- Questão 2 --

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
