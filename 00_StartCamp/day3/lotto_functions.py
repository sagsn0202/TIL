import requests
from bs4 import BeautifulSoup
import random

# 로또 번호 난수 생성기입니다.
def pick_lotto():
    my_lotto_list = sorted(random.sample(range(1, 46), 6))
    print("내 번호 : {}".format(my_lotto_list))
    return my_lotto_list

# 로또 API로부터 로또 번호를 받기 위함입니다.
def get_lotto():

    # 로또 회차를 입력 받습니다.
    while True:
        try:
            draw = int(input("회차를 입력하시오 : "))
            break
        
        except ValueError:
            print("숫자를 입력하시길 바랍니다.")

    # # 로또 사이트에서 최신 회차 호출
    #     draw_url = "https://www.nlotto.co.kr/common.do?method=main"
    #     draw_res = requests.get(draw_url).text
    #     draw_soup = BeautifulSoup(draw_res, "html.parser")
    #     draw = draw_soup.select_one("#lottoDrwNo")

    '''
    res = requests.get(url, verify = False).text
    type(res) == str 이므로
    '''

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}".format(draw)
    res = requests.get(url)
    data_dict = res.json()

    if data_dict["returnValue"] == "fail":
        print("없는 회차입니다.")
        return get_lotto()

    lotto_dict = {}
    lotto_list = []
    
    # .items() 없이 : val 대신 lotto_list[key] 활용 가능
    for key, val in data_dict.items():
        if "drwtNo" in key:
            lotto_list.append(val) 
    lotto_list.sort()
    lotto_dict["numbers"] = lotto_list

    bonus_number = data_dict["bnusNo"]
    lotto_dict["bonus"] = bonus_number

    print("{0}회차 로또 번호 : {1}".format(draw, lotto_dict))
    return lotto_dict


# 로또 번호를 비교하여 순위를 알아봅니다.
def am_i_lucky(my_lotto_list, lotto_dict):
 
    lotto_set = set(lotto_dict["numbers"])
    bonus_number = lotto_dict["bonus"]

    same_number = len(lotto_set.intersection(set(my_lotto_list)))

    if same_number == 6:
        return "1등 입니다."
    elif same_number == 5:
        if bonus_number in my_lotto_list:
            return "2등 입니다."
        else:
            return "3등 입니다."
    elif same_number == 4:
        return "4등 입니다."
    elif same_number == 3:
        return "5등 입니다."
    else:
        return "순위권 밖입니다."