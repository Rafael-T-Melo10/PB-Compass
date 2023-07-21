def conta_vogais(texto: str) -> int: # A função que a questão dá
    vogal = lambda letra: letra.lower() in 'aeiou' # Um lambda para se a letra estiver em 'aeiou' colocar ela em minusculo
    vogais_encontradas = filter(vogal, texto) # Um filter para salvar as vogais encontradas
    contagem_vogais = len(list(vogais_encontradas)) # Um len para pegar o total de vogais
    return contagem_vogais