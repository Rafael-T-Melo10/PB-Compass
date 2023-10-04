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

# A parte que pega o a média de faturamento bruto por ator.
indice_faturamento_total = cabecalho.index('Total Gross')
indice_numero_de_filmes = cabecalho.index('Number of Movies')
indice_ator = cabecalho.index('Actor')

with open('etapa-2.txt', 'w') as arquivo_saida:
    print('Media de faturamento por ator:', file = arquivo_saida)
    for linha in dados:
        nome_ator = linha[indice_ator]
        faturamento_total = float(linha[indice_faturamento_total]) # Pegando os valores e transformando em floats
        numero_de_filmes = float(linha[indice_numero_de_filmes]) # Pegando os valores e transformando em floats
        media_filme = faturamento_total / numero_de_filmes # A conta da média
        media_filme_arredondada = round(media_filme, 1) # Arredondando a média
        print('Nome:', nome_ator, file=arquivo_saida)
        print('Media de faturamento:', '{:.2f}'.format(media_filme_arredondada), file=arquivo_saida)
        print('', file=arquivo_saida)