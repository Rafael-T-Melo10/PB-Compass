from functools import reduce # O importe do reduce

def calcula_saldo(lancamentos) -> float: # A função que calcula os lançamentos
    # Um map para transformar os valores com D em negativos e os com C em positivos
    lancamentos_valores = map(lambda item: - item[0] if item[1] == 'D' else item[0], lancamentos) 
    # Um reduce para fazer o calculo em todos os itens da lista
    saldo = reduce(lambda x, valor: x + valor, lancamentos_valores, 0)
    return saldo


