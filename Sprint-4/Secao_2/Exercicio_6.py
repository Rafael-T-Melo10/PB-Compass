def maiores_que_media(conteudo: dict) -> list: # A função que pega os valores do dic, tira a média e ordena
    valores = list(conteudo.values()) # Pega os valores do dicio
    media = sum(valores) / len(valores) # Faz a nédia 
    # Usa um lambda para pegar os valores maiores que a média
    maiores_que_media = list(filter(lambda x: x[1] > media, conteudo.items())) 
    maiores_que_media.sort(key=lambda x: x[1]) # Ordena a lista
    return maiores_que_media 

conteudo = { # O dicionário
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(conteudo)
print(resultado)

