import boto3
import os
csv_series = 'series.csv'
csv_movies = 'movies.csv'
bucket_name = 'etl-desafio'
file_path_movies = 'Raw/Local/CSV/Movies/2023/09/01/'
file_path_series = 'Raw/Local/CSV/Series/2023/09/01/'

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token_key = os.getenv('AWS_SESSION_TOKEN')
s3 = boto3.client('s3', aws_access_key_id = aws_access_key, aws_secret_access_key = aws_secret_key, aws_session_token = aws_session_token_key)

s3.upload_file(csv_series, bucket_name,file_path_series + csv_series)
s3.upload_file(csv_movies, bucket_name,file_path_movies + csv_movies)
