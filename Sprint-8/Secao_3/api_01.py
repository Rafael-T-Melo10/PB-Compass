import requests
import json
import boto3
import os
# A função lambda usada na AWS
def lambda_handler(event, context):
    # As variáveis
    file_path_1 = '/tmp/resultados_actors.json'
    file_path_2 = '/tmp/resultados_genre.json'
    file_path_0 = 'Raw/TMDB/JSON/2023/09/14/'
    actors = ['Jack%20Black', 'Dwayne%20Johnson']
    api_key = '57435fa8f5ab634ed0c829d299830df1'
    base_url = 'https://api.themoviedb.org/3'
    bucket_name = 'etl-desafio'

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NzQzNWZhOGY1YWI2MzRlZDBjODI5ZDI5OTgzMGRmMSIsInN1YiI6IjY0Zjg2ZWVhNGNjYzUwMTg2OGRhM2ZkYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aKRY93KMv3gpTSjRCn9GtShVtZSXaYVGo9wxZuPwnBE"
    }
    
    # Conectando a AWS com as key temporarias
    aws_access_key = os.getenv('ASIASHOQC4ZSVNBCXAHM')
    aws_secret_key = os.getenv('3QoEAKBGifU8ykKgj8RCRBg6Mpn520He8DdGZDPl')
    aws_session_token_key = os.getenv('IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJGMEQCIGCKYuQ4jaJGnY4L48sIGi9/1+4hyx2XZwah9d3WBSc4AiBQ4Btlt5EELeDjqhGYc+hByXKUJePdZxTQcSsBidkIsSqbAwhGEAAaDDE1MzQ0NDYwNzU4OSIMmB9N3BX5NEUo+Fd6KvgCpSfsj8rR+n6hhCMT0laGeWaDC+uyv59ox6vjTCQ1yR2mN8uUYUN/7vI7WSODWHrKpY8rroNemeqokCw34QnbXfWRkdmx0iVr0MHmj2N5QvQI57jqe3dqvwyhavqOVimHihJ7gQDxlVatLv/oG5ag4zyb7Dz8BYnicvdpxFTxY9JlO+8jRe6klR19raiVd+71ibmQPJtGZZaFDoVH5GAoC2E//uNVf2arJqEP+u958JfPS3ek+TC9fWkgBWBlzQxMkLNagg2GFnj62CxNzoKzL5HrRkugeBx7W19JWsuBZtvE0fCizFxuwCg++/z2GfFIud2Ac1NLh7CsyrxEQfjXMaO7xQY/WhZJE9rI5GXKk32yBZ9b5tpnL3FOMxJ32adMrtkrWFtq0n4hE79d4fJPY0YzAAWuoi/UoGxCU1hFjYI4x0RKDyVbstysu7gXdQEA6mU3L+0YLeDiQyC2XKCz9E4JswFvrvyZ84nsPBWk/UxilUu11rRS7jDCgIyoBjqnARHVYLWb3ZNbChPR/OvmW0rXGPho4ZxRg3zGQ/4iUPGWlGJQP8Gj38zC9CsIC3HRtNkXyR7Ohit8MC3lAY9+gIcSU9g4smLQ0mHp8XTdiT8E+d653lWRrMLIN0PWtEaymJKnr2Dz86T+9TWTD4B8cKxac9Qu8v/nMaYY5iPGuLM8QZgJakaXMNofMx1EOZs3qx/L4rdUZTP7jk1gdV5eL4O+KuksVf4i')
    
    # As variáveis que quardam os requests
    results_actors = []
    results_genres = []
    
    # Fazendo um for para fazer um request por nome na lista actors
    for actor in actors:
      url = f'{base_url}/search/person?api_key={api_key}&query={actor}&include_adult=false&language=en-US&page=1'
      response = requests.get(url, headers=headers)
      data = response.json()
      results_actors.append(data)
    
    # O request que pega todos os filmes com os generos 16 e 35 (Animação e Comédia)
    url = f'{base_url}/discover/tv?api_key={api_key}&include_adult=false&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=16%2C35'
    response = requests.get(url, headers=headers)
    data = response.json()
    results_genres.append(data)
    
    # A função que escreve as saidas dos requests em formato JSON
    def create_json_aws(path, results):
      with open(path, 'w') as json_file:
          json.dump(results, json_file, indent=4)
    
    # As 2 saidas
    create_json_aws(file_path_1, results_actors)
    create_json_aws(file_path_2, results_genres)
    
    # Escrevendo os dados usando o boto3
    s3 = boto3.client('s3', aws_access_key_id = aws_access_key, aws_secret_access_key = aws_secret_key, aws_session_token = aws_session_token_key)
    s3.upload_file(file_path_1, bucket_name,file_path_0 + 'Resultados_Atores')
    s3.upload_file(file_path_2, bucket_name,file_path_0 + 'Resultados_Genero')