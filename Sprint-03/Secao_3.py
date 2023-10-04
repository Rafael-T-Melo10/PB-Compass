# Exercícios 1

# Um input para ler o nome e a idade atual da pessoa
nome = input('Coloque seu nome')
idade = int(input('Coloque sua idade'))
anoCem = 2023 + (100 - idade) # A conta que mostra quando a pessoa fará 100 anos
print(f'Você, {nome}, fará 100 anos em {anoCem}')

# Exercícios 2

# Recebe os 3 valores e confere se são pares ou impares
for i in range(3):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Par:", numero)
    else:
        print("Ímpar:", numero)

# Exercícios 3

# Um print que mostra os valores pares de 0 até 20
for i in range(21):
    if i % 2 == 0:
        print(i)

# Exercícios 4

# Um print dos valores primo entre 1 até 100
for i in range(2, 101): # O primeiro primo é 2 por isso o range começa com 2, e vai até 101 para pegar o 100
    e_primo = True
    for j in range(2, int(i ** 0.5) + 1): # A conta matemática que confere se o número é primo
        if i % j == 0:
            e_primo = False
            break
    if e_primo:
        print(i,)

# Exercícios 5

# O código que mostra a saida no formato dia/mes/ano
dia = 22
mes = 10
ano = 2022
print(f'{dia}/{mes}/{ano}')
