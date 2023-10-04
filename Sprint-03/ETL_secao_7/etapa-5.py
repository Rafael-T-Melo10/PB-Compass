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

dados_ordenados = sorted(dados, reverse=True, key=lambda linha: float(linha[indice_faturamento_bruto]))

# A parte que pega a lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.
indice_faturamento_bruto = cabecalho.index('Total Gross')
indice_ator = cabecalho.index('Actor')

with open('etapa-5.txt', 'w') as arquivo_saida:
    print('Faturamento bruto por ator:', file = arquivo_saida)
    for linha in dados_ordenados:
        nome_ator = linha[indice_ator]
        faturamento_bruto  = float(linha[indice_faturamento_bruto])
        print('Nome: ', nome_ator, file = arquivo_saida)
        print('media de faturamento: ', faturamento_bruto, file = arquivo_saida)
        print('', file = arquivo_saida)