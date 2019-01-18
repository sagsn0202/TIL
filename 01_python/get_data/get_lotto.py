import requests

"""
https://www.dhlottery.co.kr/common.do
?
method=getLottoNumber
&
drwNo=837
"""

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

res = requests.get(URL)
data_dict = res.json()

if data_dict['returnValue'] == 'fail':
    print('없는 회차입니다.')

lotto_dict = {}
lotto_list = []

for key, val in data_dict.items():
    if 'drwtNo' in key:
        lotto_list.append(val)

lotto_list.sort()
print(lotto_list)