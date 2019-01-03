import requests

url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"

'''
res = requests.get(url, verify = False).text
type(res) == str 이므로
'''

res = requests.get(url, verify = False)
data_dict = res.json()

lotto_list = []

for key, val in data_dict.items():
    if "drwtNo" in key:
        lotto_list.append(val)

lotto_list.sort()
bonus_number = data_dict["bnusNo"]
print(lotto_list)