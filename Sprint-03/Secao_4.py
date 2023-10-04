# Exercícios 6

a = set([1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
c = a.intersection(b) # Pega a interseção das 2 listas
lista = list(c)
print(lista)

# Exercícios 7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
c = []
for i in a:
    if i % 2 != 0:
        c.append(i)
print(c)

# Exercícios 8

# A lista da questão
lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in lista:
    if palavra == palavra[::-1]: # Printa se as palavras são palíndromos
        print(f'A palavra: {palavra} é um palíndromo')
    else:  # Printa se as palavras não são palíndromos
        print(f'A palavra: {palavra} não é um palíndromo')

# Exercícios 9

# As listas da questão
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
# Um print para mostrar os dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos"
for indice, primeiroNome in enumerate(primeirosNomes):
    sobreNome = sobreNomes[indice]
    idade = idades[indice]
    print(f'{indice} - {primeiroNome} {sobreNome} está com {idade} anos')

# Exercícios 10

def nova_lista(): # A função que pega a lista e tira as duplicadas

    lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
    lista_sem_duplicatas = list(set(lista)) # Transforma em set para remover as duplicadas
    print(lista_sem_duplicatas)

nova_lista()

# Exercícios 11

arquivo = open('arquivo_texto.txt', 'r') # Abrindo o arquivo txt
conteudo = arquivo.read() # Lendo o txt
print(conteudo, end='') # Printando sem quebrar linha

# Exercícios 12

import json # O import json

with open('person.json', 'r') as arquivo: # Carregando o Json
    dados = json.load(arquivo)

print(dados) # Printando os dados do Json

# Exercícios 13

def my_map(lista, f): # Recebe uma lista e uma função
    nova_lista = []
    for i in lista: 
        conta = f(i) # A variável que recebe a conta
        nova_lista.append(conta) # Adicionando a lista com os valores ao quadrado
    return nova_lista

def potencia(valor): # A função que eleva ao quadrado
    return valor ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(lista, potencia)
print(resultado)

# Exercícios 14

def imprimir_parametros(*args, **kwargs): # Recebe os números das variaveis não noemados e os nomeados 

    for parametro in args: # Printa os não nomeados
        print(parametro)

    for valor in kwargs.values(): # Printa os nomeados
        print(valor)

imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

# Exercícios 15

class Lampada: # A classe lampada
    def __init__(self, ligada) -> None: # O método inícial, com o atribito ligado
        self.ligada = ligada

    def liga(self): # O método liga
        self.ligada = True

    def desliga(self): # O método desliga
        self.ligada = False

    def esta_ligada(self): # O método esta ligado
        return self.ligada

lampada = Lampada(False) # O objeto lampada
lampada.liga()
print('A lâmpada está ligada?', lampada.esta_ligada())
lampada.desliga()
print('A lâmpada ainda está ligada?', lampada.esta_ligada())

# Exercícios 16

def somar(valores_string): # Recebe a string
    valores = valores_string.split(',') # Separa ela por virgulas
    valores = [int(num) for num in valores] # Transdorma em inteiros
    soma = sum(valores) # Soma eles
    return soma 
valores_string = '1,3,4,6,10,76'
resultado = somar(valores_string)
print(resultado)

# Exercícios 17

def dividir_lista(lista): # Recebe a lista
    tamanho = len(lista) # Pega o tamanho total dela
    lista_dividida = tamanho // 3 # transforma a lista dividida no mesmo valor do tamanho total dividido por 3
    lista_1 = lista[:lista_dividida] # Coloca os valores 0 de até 1 terço
    lista_2 = lista[lista_dividida:lista_dividida*2] # Coloca os valores de 1 terço até 2 vezes 1 terço
    lista_3 = lista[lista_dividida*2:] # Coloca os valores de 2 vezes 1 terço até o fim
    return lista_1, lista_2, lista_3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_lista(lista) # Imprime as 3 partes

print(parte1,parte2,parte3)

# Exercícios 18

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
valores = list(speed.values())
valores_sem_duplicados = list(set(valores)) # Colocando os 12 valores em um set para tirar os duplicados
print(valores_sem_duplicados)

# Exercícios 19
# Gerando os valores aleatorios de 0 a 500
import random
random_list = random.sample(range(500), 50)
lista_ordenada = sorted(random_list)
lista_meio = len(random_list) // 2

# A conta da mediana dos valores
if len(random_list) % 2 == 1:
    mediana = lista_ordenada[lista_meio]
else:
    mediana = (lista_ordenada[lista_meio - 1] + lista_ordenada[lista_meio]) / 2

media = sum(random_list) / len(random_list) # A conta da média dos valores

valor_minimo = min(random_list) # A conta do valor mínimo dos valores

valor_maximo = max(random_list) # A conta do valor máximo dos valores
print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo:{valor_maximo}')

# Exercícios 20

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_invertido = a[::-1] # Imprimindo a lista de trás para frente
print(a_invertido)