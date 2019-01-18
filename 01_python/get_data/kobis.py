import os
import datetime
import requests
import csv
import pandas as pd

reference_date = datetime.datetime(2019,1,13)

boxoffice_file_template = open('./boxoffice_template.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(boxoffice_file_template)
writer.writerow(['movie_code', 'title', 'audience', 'recorded_at'])

for i in range(10):
    current_date = reference_date + datetime.timedelta(days=(i * (-7)))
    if current_date.month < 10 and current_date.day < 10:
        current_date_str = f'{current_date.year}0{current_date.month}0{current_date.day}'
    elif current_date.month < 10:
        current_date_str = f'{current_date.year}0{current_date.month}{current_date.day}'
    elif current_date.day < 10:
        current_date_str = f'{current_date.year}{current_date.month}0{current_date.day}'
    else:
        current_date_str = f'{current_date.year}{current_date.month}{current_date.day}'

    key = os.getenv('KOBIS_KEY')
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={current_date_str}&weekGb=0'

    res = requests.get(URL)
    data_dict = res.json()
    boxofficeresult_dict = data_dict['boxOfficeResult']
    
    for i in range(len(boxofficeresult_dict['weeklyBoxOfficeList'])):
        movieCd = boxofficeresult_dict['weeklyBoxOfficeList'][i]['movieCd']
        movieNm = boxofficeresult_dict['weeklyBoxOfficeList'][i]['movieNm']
        audiAcc = boxofficeresult_dict['weeklyBoxOfficeList'][i]['audiAcc']
        recorded_at = current_date_str
        boxoffice_result = [movieCd, movieNm, audiAcc, recorded_at]
        writer.writerow(boxoffice_result)

boxoffice_file_template.close()

boxoffice_duplicated_df = pd.read_csv('./boxoffice_template.csv')
print(boxoffice_duplicated_df.head())
boxoffice_df = boxoffice_duplicated_df.drop_duplicates(['movie_code'])
boxoffice_df.to_csv('./boxoffice.csv')

movie_file = open('./movie.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(movie_file)
writer.writerow(['movie_code', 'movie_name_ko', 'movie_name_en', 'movie_name_og', 'prdt_year', 'genres', 'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3'])

for val in boxoffice_df['movie_code']:
    key = 'c7a75f2ce8783b5fdb9054ee8ac5f717'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={val}'

    res = requests.get(URL)
    data_dict = res.json()
    movieinforesult_dict = data_dict['movieInfoResult']

    movieCd = movieinforesult_dict['movieInfo']['movieCd']
    movieNm = movieinforesult_dict['movieInfo']['movieNm']
    movieNmEn = movieinforesult_dict['movieInfo']['movieNmEn']
    movieNmOg = movieinforesult_dict['movieInfo']['movieNmOg']
    prdtYear = movieinforesult_dict['movieInfo']['prdtYear']
    genres = movieinforesult_dict['movieInfo']['genres'][0]['genreNm']
    directors = movieinforesult_dict['movieInfo']['directors'][0]['peopleNm']
    audits = movieinforesult_dict['movieInfo']['audits'][0]['watchGradeNm']
    actors = ['', '', '']
    if movieinforesult_dict['movieInfo']['actors']:
        for i in range(len(movieinforesult_dict['movieInfo']['actors'])):
            if i > 2:
                break
            actors[i] = movieinforesult_dict['movieInfo']['actors'][i]['peopleNm']

    boxoffice_result = [movieCd, movieNm, movieNmEn, movieNmOg, prdtYear, genres, directors, audits, actors[0], actors[1], actors[2]]
    writer.writerow(boxoffice_result)

movie_file.close()

boxoffice_df = pd.read_csv('./boxoffice.csv')
movie_df = pd.read_csv('./movie.csv')
movie_kobis_df = pd.merge(boxoffice_df, movie_df).drop(columns=['Unnamed: 0'])
movie_kobis_df.to_csv('./moviekobis.csv')