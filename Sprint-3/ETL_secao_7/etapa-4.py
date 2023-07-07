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

indice_filme = cabecalho.index('#1 Movie')

frequencia_filmes = {}

# Conta a quantdade de vezes que apareceu
for linha in dados:
    filme = linha[indice_filme]
    if filme in frequencia_filmes:
        frequencia_filmes[filme] += 1
    else:
        frequencia_filmes[filme] = 1

# Obter as 5 maiores frequências
maiores_frequencias = sorted(frequencia_filmes.items(), key=lambda x: x[1], reverse=True)[:5]

with open('etapa-4.txt', 'w') as arquivo_saida:
    print("Filmes mais frequentes:", file=arquivo_saida)
    for filme, frequencia in maiores_frequencias:
        print("Filme:", filme, file=arquivo_saida)
        print("Frequencia:", frequencia, file=arquivo_saida)
        print('', file=arquivo_saida)