import requests
import random

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
        # .items() 없이 : val 대신 lotto_list[key] 활용
lotto_list.sort()
bonus_number = data_dict["bnusNo"]

print("로또 번호 : " + str(lotto_list))
print("보너스 번호 : " + str(bonus_number))

# 로또 난수 생성
numbers = list(range(1, 46))
my_lotto_list = random.sample(numbers, 6)
my_lotto_list.sort()

print("내 번호 : " + str(my_lotto_list))

# 로또 집합 클래스 전환
lotto_set = set(lotto_list)
my_lotto_set = set(my_lotto_list)
same_number = len(lotto_set.intersection(my_lotto_set))

if same_number == 6:
        print("1등 입니다.")
elif same_number == 5:
        if bonus_number in my_lotto_list:
                print("2등 입니다.")
        else:
                print("3등 입니다.")
elif same_number == 4:
        print("4등 입니다.")
elif same_number == 3:
        print("5등 입니다.")
else:
        print("순위권 밖입니다.")

# count = 0

# for my_number in my_lotto_list:
#         for real_number in lotto_list:
#                 if my_number == real_number:
#                         count += 1

# print(count)