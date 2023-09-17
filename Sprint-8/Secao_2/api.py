# Esse foi o código da seção 2 da sprint 8
import requests
import pandas as pd

from IPython.display import display

# Aqui conecta com a API
api_key = '57435fa8f5ab634ed0c829d299830df1'

url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR'

response = requests.get(url)

# Aqui pega a resposta da API e salva em uma variável
data = response.json()
filmes = []

# Aqui pega todos os itens na variável data e os coloca em formato de dicionário para depois dar append na lista filme
for movie in data['results']:
    df = {'Titulo': movie['title'],
    'Data de lançamento': movie['release_date'],
    'Visão geral': movie['overview'],
    'Votos': movie['vote_count'],
    'Média de votos:': movie['vote_average']}

    filmes.append(df)

# Aqui mostra um dataframe da lista filmes
df = pd.DataFrame(filmes)
display(df)
