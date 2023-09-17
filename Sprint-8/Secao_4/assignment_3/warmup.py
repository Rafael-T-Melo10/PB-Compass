import random
import csv

# Criando uma lista com 250 números
list_limit = 250
inf_limit = 1
sup_limit = 1000

list_num = []

for _ in range(list_limit):
    random_num = random.randint(inf_limit, sup_limit)
    list_num.append(random_num)

list_num.reverse()
print(list_num)

# Lista de animais

list_anim = ['Cachorro', 'Gato', 'Elefante', 'Leão', 'Tigre', 'Girafa', 'Zebra', 'Urso', 'Canguru', 'Rinoceronte', 'Hipopótamo', 'Coelho', 'Pinguim', 'Golfinho', 'Arara', 'Coruja', 'Sapo', 'Cobra', 'Peixe', 'Tartaruga' ]
nome_arquivo = "animais.csv"

list_anim.sort()

# Criando um csv com os nomes da lista animal 
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    for animal in list_anim:
        escritor_csv.writerow([animal])