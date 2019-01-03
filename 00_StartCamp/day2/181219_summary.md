# 12. 19. 수업 정리

```python
cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}
```

## list 문제풀이 1

```python
for city, temp in cities_temp.items():
    avg_temp = round(sum(temp) / len(temp), 2)
    print("{0} : {1}".format(city, avg_temp))
```

```python
for city in cities_temp:
    temp = cities_temp[city]
    avg_temp = round((sum(temp) / len(temp)), 2)
    print(city + " : " + str(avg_temp))
```

## list 문제풀이 2

```python
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
```

```python
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
```

## HTML 기본

1. **HTML** stands for **H**yper**T**ext **M**arkup **L**anguage and is used to create the structure and content of a webpage.
2. Most HTML elements contain opening and closing tags with raw text or other HTML tags between them.
3. HTML elements can be nested inside other elements. The enclosed element is the child of the enclosing parent element.
4. Any visible content should be placed within the opening and closing `<body>` tags .
5. Headings and sub-headings, `<h1>` to `<h6>` tags, are used to enlarge text. 
6. `<p>`, `<span>` and `<div>` tags specify text or blocks.
7. The `<em>` and `<strong>` tags are used to emphasize text. 
8. Line breaks are created with the `<br>` tag. 
9. Ordered lists (`<ol>`) are numbered and unordered lists (`<ul>`) are bulleted. 
10. Images (`<img>`) and videos (`<video>`) can be added by linking to an existing source.