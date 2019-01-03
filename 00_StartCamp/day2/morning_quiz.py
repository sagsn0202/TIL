# 1
my_score = [79, 84, 66, 93]
my_average = sum(my_score)/len(my_score)
print(my_average)

# 2
your_score = {
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100
}
your_average = sum(your_score.values())/len(your_score)
print(your_average)

# 3
cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}

# cities_temp.items()은 list와 같은 dict_item 객체이다.
for city, temp in cities_temp.items():
    avg_temp = round(sum(temp) / len(temp), 2)
    print("{0} : {1}".format(city, avg_temp))

# for city in cities_temp:
#     temp = cities_temp[city]
#     avg_temp = round((sum(temp) / len(temp)), 2)
#     print(city + " : " + str(avg_temp))

# 4
max_temp = -257
min_temp = 100

for city, temp_list in cities_temp.items():
    if max_temp < max(temp_list):
        max_temp = max(temp_list)
        max_day = temp_list.index(max(temp_list)) + 1
        max_city = city
print("Hottest : {0}이며 온도는 {1}도 이고, {2}번째 날입니다.".format(max_city, max_temp, max_day))
    
for city, temp_list in cities_temp.items():
    if min_temp > min(temp_list):
        min_temp = min(temp_list)
        min_day = temp_list.index(min(temp_list)) + 1
        min_city = city
print("Coldest : {0}이며 온도는 {1}도 이고, {2}번째 날입니다.".format(min_city, min_temp, min_day))

all_temp = []
for key, val in cities_temp.items():
    all_temp += val

high_temp = max(all_temp)
low_temp = min(all_temp)

hottest = []
coldest = []

for key, val in cities_temp.items():
    if high_temp in val:
        hottest.append(key)
    if low_temp in val:
        coldest.append(key)

print(hottest, coldest)