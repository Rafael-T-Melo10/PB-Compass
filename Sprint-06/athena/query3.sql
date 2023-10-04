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