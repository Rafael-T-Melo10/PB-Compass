import csv # O import do csv

def ler_arquivo(nome_arquivo): # Uma função para ler o arquivo
    with open(nome_arquivo, encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        return list(leitor_csv) # Retorna uma lista com o conteudo do csv

def notas_estudantes(estudantes): # Uma função para armazenar as notas, nomes, a média e as 3 maiores notas
    relatorio = [] # Um relatório para depois armazenar o que é pedido
    for estudante in estudantes: # Um for para que cada linha(aluno) do csv sejá separado 
        nome = estudante[0] # Armazena o nome dos estudantes
        notas = list(map(int, estudante[1:])) # Armazena as notas em formato de lista usando um map para trasnformar as notas em int
        tres_maiores_notas = sorted(notas, reverse = True)[:3] # Pega as notas, poe em ordem decrescente e separa os 3 maiores
        media_tres_nota = round(sum(tres_maiores_notas)/3, 2) # Pega a média das 3 maiores notas e limita para 2 casas decimais
        relatorio.append((nome, tres_maiores_notas, media_tres_nota)) # Adiciona o nome, as 3 maiores notas e a médias no relatório
    return relatorio

nome_arquivo = 'estudantes.csv' # O arquivo csv
linhas_separadas = ler_arquivo(nome_arquivo) # As linhas do csv
relatorio = notas_estudantes(linhas_separadas) # O relatório dos alunos
relatorio_ordenado = sorted(relatorio, key=lambda x: x[0]) # E um sorted para mostrar em ordem alfabetica as notas

for nome, notas, media in relatorio_ordenado: # Um print do relatório
        print(f"Nome: {nome} Notas: {notas} Média: {media}")