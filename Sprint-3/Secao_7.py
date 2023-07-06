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

# A parte que pega o ator/atriz com a maior média de faturamento por filme
indice_media_por_filme = cabecalho.index('Average per Movie')
indice_ator = cabecalho.index('Actor')

maior_faturamento = 0
ator_com_maior_faturamento = ''

for linha in dados:
    media_faturamento = float(linha[indice_media_por_filme])
    if media_faturamento > maior_faturamento:
        maior_faturamento = media_faturamento
        ator_com_maior_faturamento = linha[indice_ator]

print("Ator/atrizes com a maior média de faturamento por filmes:")
print("Nome:", ator_com_maior_faturamento)
print("Maior média de faturamento:", maior_faturamento)