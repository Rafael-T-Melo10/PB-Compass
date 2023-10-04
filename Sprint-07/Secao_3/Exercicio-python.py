import pandas as pd

data_frame = pd.read_csv('actors.csv')
print(data_frame.head())

maior_filme = data_frame['Number of Movies'].idxmax()
filmes_max = data_frame.loc[maior_filme, 'Number of Movies']
ator_max = data_frame.loc[maior_filme, 'Actor']
print(f'O ator com o maior número de filmes é {ator_max}, com {filmes_max} filmes')

media_filmes = data_frame['Number of Movies'].mean()
print(f'A média é {media_filmes}')

maior_media = data_frame['Average per Movie'].idxmax()
media_ator_max = data_frame.loc[maior_media, 'Average per Movie']
ator_media_max = data_frame.loc[maior_media, 'Actor']
print(f'O ator com a maior média por filmes é {ator_media_max}, com {media_ator_max} de média')

filme_frequente = data_frame['#1 Movie'].value_counts().head(5)
print(filme_frequente)