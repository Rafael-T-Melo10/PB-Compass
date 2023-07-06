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

# A parte que pega o nome do filme mais frequente e sua respectiva frequência.
indice_filme = cabecalho.index('#1 Movie')

frequencia_filmes = {}

for linha in dados:
    filme = linha[indice_filme]
    if filme in frequencia_filmes:
        frequencia_filmes[filme] += 1
    else:
        frequencia_filmes[filme] = 1

maior_frequencia = max(frequencia_filmes.values())

filmes_mais_frequentes = [filme for filme, frequencia in frequencia_filmes.items() if frequencia == maior_frequencia]

print("Filme(s) mais frequente(s):")
for filme in filmes_mais_frequentes:
    print("Filme:", filme)
    print("Frequência:", maior_frequencia)