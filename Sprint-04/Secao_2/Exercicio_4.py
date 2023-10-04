def calcular_valor_maximo(operadores, operandos) -> float: # função para pegar os valores maximos
    operacoes = { # Um dicionario com as operações matematicas, onde usa um lambda para transformar de string em operação
        '+': lambda x, y: x + y, # Soma
        '-': lambda x, y: x - y, # Subtração
        '*': lambda x, y: x * y, # Multiplicação
        '/': lambda x, y: x / y, # Divisão
        '%': lambda x, y: x % y # Resto
    }
    conta = zip(operadores, operandos) # Um zip para juntar os operadores com os operandos
    # Um map para pegar a operação e juntar com os valores de detro das tuplas
    resultados = map(lambda x: operacoes[x[0]](x[1][0], x[1][1]), conta) # Um map para pegar a operação e juntar com os valores de detro das tuplas
    return max(resultados) # O return

