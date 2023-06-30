# Exercícios 1

nome = input('Coloque seu nome')
idade = int(input('Coloque sua idade'))
anoCem = 2023 + (100 - idade)
print(f'Você, {nome}, fará 100 anos em {anoCem}')

# Exercícios 2

for i in range(3):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Par:", numero)
    else:
        print("Ímpar:", numero)

# Exercícios 3

for i in range(21):
    if i % 2 == 0:
        print(i)

# Exercícios 4

for i in range(2, 101):
    e_primo = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            e_primo = False
            break
    if e_primo:
        print(i,)

# Exercícios 5

dia = 22
mes = 10
ano = 2022
print(f'{dia}/{mes}/{ano}')

