# Uma função para ler as informações do arquivo .csv e tratar os dados

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    cabecalho = linhas[0].strip().split(',') # Pega o cabeçalho

    dados = []
    for linha in linhas[1:]: # Um for para pegar as linhas do csv
        linha = linha.strip() 
        valores = []

        i = 0 
        while i < len(linha): # Um while para percorrer os caractereres da linha
            if linha[i] == '"': # Se encontrar '"' pula as aspas e continua procurando por ','
                i += 1
                inicio = i
                while i < len(linha) and linha[i] != '"':
                    i += 1
                fim = i
                valor = linha[inicio:fim]
                i += 1

            else: # Se encontroar um valor normal continua procurando por ','
                inicio = i
                while i < len(linha) and linha[i] != ',':
                    i += 1
                fim = i
                valor = linha[inicio:fim]

            valores.append(valor)
            i += 1

        if len(valores) == len(cabecalho):  # Verifica se o número de valores está correto
            dados.append(valores)

    return cabecalho, dados

cabecalho, dados = ler_arquivo_csv('actors.csv')

# A parte que pega o Ator/atrizes com o maior número de filmes e a respectiva quantidade. 
indice_numero_filmes = cabecalho.index('Number of Movies')
indice_ator = cabecalho.index('Actor')

maior_numero_filmes = 0
ator_com_mais_filmes = ''

for linha in dados:
    numero_filmes = int(linha[indice_numero_filmes])
    if numero_filmes > maior_numero_filmes:
        maior_numero_filmes = numero_filmes
        ator_com_mais_filmes = linha[indice_ator]

print("Ator/atrizes com o maior número de filmes:")
print("Nome: ", ator_com_mais_filmes)
print("Número de filmes: ", maior_numero_filmes)