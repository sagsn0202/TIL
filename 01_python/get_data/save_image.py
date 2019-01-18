import urllib.request
from time import sleep
import csv
import pandas as pd

movie_all_df = pd.read_csv('./movieall.csv')

for idx, row in movie_all_df.iterrows():
    url = row['thumb_url']
    code = row['movie_code']
    code_path = f'./images/{code}.jpg'
    urllib.request.urlretrieve(url, code_path)