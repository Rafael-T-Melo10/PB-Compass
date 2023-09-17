import names
import time
import random

random.seed(40)

qtd_nomes_unicos = 3000

qtd_nomes_aleatorios = 10000000

nome_arquivo_txt = 'nomes_aleatorios.txt'

aux=[]

for i in range(0, qtd_nomes_unicos):

    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados=[]

for i in range(0,qtd_nomes_aleatorios):

    dados.append(random.choice(aux))

with open(nome_arquivo_txt, mode='w', newline='') as arquivo_txt_lab:

    for dado in dados:
        arquivo_txt_lab.write(dado + '\n')