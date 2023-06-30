# Exercícios 6

a = set([1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
c = a.intersection(b)
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

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in lista:
    if palavra == palavra[::-1]:
        print(f'A palavra: {palavra} é um palíndromo')
    else:
        print(f'A palavra: {palavra} não é um palíndromo')

# Exercícios 9

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, primeiroNome in enumerate(primeirosNomes):
    sobreNome = sobreNomes[indice]
    idade = idades[indice]
    print(f'{indice} - {primeiroNome} {sobreNome} está com {idade} anos')

# Exercícios 10

def nova_lista():

    lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
    lista_sem_duplicatas = list(set(lista))
    print(lista_sem_duplicatas)

nova_lista()

# Exercícios 11

arquivo = open('arquivo_texto.txt', 'r')
conteudo = arquivo.read()
print(conteudo, end='')

# Exercícios 12

import json

with open('person.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)

# Exercícios 13

def my_map(lista, f):
    nova_lista = []
    for i in lista:
        conta = f(i)
        nova_lista.append(conta)
    return nova_lista

def potencia(valor):
    return valor ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(lista, potencia)
print(resultado)

# Exercícios 14

def imprimir_parametros(*args, **kwargs):

    for parametro in args:
        print(parametro)

    for valor in kwargs.values():
        print(valor)

imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

# Exercícios 15

class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

lampada = Lampada(False)
lampada.liga()
print('A lâmpada está ligada?', lampada.esta_ligada())
lampada.desliga()
print('A lâmpada ainda está ligada?', lampada.esta_ligada())

# Exercícios 16

def somar(valores_string):
    valores = valores_string.split(',')
    valores = [int(num) for num in valores]
    soma = sum(valores)
    return soma
valores_string = '1,3,4,6,10,76'
resultado = somar(valores_string)
print(resultado)

# Exercícios 17

def dividir_lista(lista):
    tamanho = len(lista)
    lista_dividida = tamanho // 3
    lista_1 = lista[:lista_dividida]
    lista_2 = lista[lista_dividida:lista_dividida*2]
    lista_3 = lista[lista_dividida*2:]
    return lista_1, lista_2, lista_3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_lista(lista)

print(parte1,parte2,parte3)

# Exercícios 18

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
valores = list(speed.values())
valores_sem_duplicados = list(set(valores))
print(valores_sem_duplicados)

# Exercícios 19

import random
random_list = random.sample(range(500), 50)
lista_ordenada = sorted(random_list)
lista_meio = len(random_list) // 2
if len(random_list) % 2 == 1:
    mediana = lista_ordenada[lista_meio]
else:
    mediana = (lista_ordenada[lista_meio - 1] + lista_ordenada[lista_meio]) / 2
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)
print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo:{valor_maximo}')

# Exercícios 20

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_invertido = a[::-1]
print(a_invertido)