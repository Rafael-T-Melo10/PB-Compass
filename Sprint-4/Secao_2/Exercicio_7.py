def pares_ate(n:int): # A função para pegar os pares de 2 em 2
    for num in range(2, n + 1, 2): # Um range de 2 até n + 1 para incluir o n
        yield num # Retorna os números

n = 10 # Um n aleatorio

gera_num = pares_ate(n)        
for par in gera_num: # O print dos valores de n
    print(par)