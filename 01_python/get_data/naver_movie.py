import os
import requests
from time import sleep
import csv
import pandas as pd

movie_kobis_df = pd.read_csv('./moviekobis.csv')

naver_movie_file = open('./navermovie.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(naver_movie_file)
writer.writerow(['title', 'thumb_url', 'link_url', 'user_rating'])

URL = 'https://openapi.naver.com/v1/search/movie.json?query='

client_id = os.getenv('NAVER_CLIENT_ID')
client_secret = os.getenv('NAVER_CLIENT_SECRET')
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
    }

for val in movie_kobis_df['title']:
    res = requests.get(URL + val, headers=headers)
    data_dict = res.json()
    print(data_dict)

    image = data_dict['items'][0]['image']
    link = data_dict['items'][0]['link']
    userRating = data_dict['items'][0]['userRating']

    navermovie_result = [val, image, link, userRating]
    writer.writerow(navermovie_result)
    sleep(0.05)

naver_movie_file.close()
navermovie_df = pd.read_csv('./navermovie.csv')
movie_all_df = pd.merge(movie_kobis_df, navermovie_df).drop(columns=['Unnamed: 0', 'title'])
movie_all_df.to_csv('./movieall.csv')

navermovie_answer_df = movie_all_df[['movie_code', 'thumb_url', 'link_url', 'user_rating']]
navermovie_answer_df.to_csv('./movie_naver.csv')