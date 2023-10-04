def inteiro(string): # Uma função para pegar as strings do txt e passar para int
    return int(string.strip())

with open('number.txt', 'r') as arquivo: # Abrindo o txt
    linha = arquivo.readlines()

lista_numeros = list(map(inteiro, linha)) # Aplicando a função inteiro em todos os itens do txt

pares = list(filter(lambda x: x % 2 == 0, lista_numeros)) # Filtrando os pares
cinco_maiores = sorted(pares, reverse=True)[:5] # Ordenando e pegando os 5 maiores
soma_cinco = sum(cinco_maiores) # Somando os 5 maiores
print(cinco_maiores) # Printando os 5 maiores
print(soma_cinco) # Printando a soma dos 5 maiores