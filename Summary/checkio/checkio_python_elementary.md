## 곱하기 연산

### My Answer

```python
def mult_two(a, b):
    return a * b
```

### Great Answer

```python
from operator import mul as mult_two
```

## 이름과 나이 표시

### My Answer

```python
def say_hi(name: str, age: int) -> str:
    return "Hi. My name is %s and I'm %d years old" % (name, age)
```

### Great Answer

```python
say_hi = "Hi. My name is {} and I'm {} years old".format
```

```python
def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"
```

```python
def say_hi(name, age):
    t = Template("Hi. My name is $name and I'm $age years old")
    return t.substitute(name=name, age=age)
```

## 대문자 시작과 점 끝

### My Answer

```python
def corret_sentence(text: str) -> str:
small = text[0]
    capital = small.upper()
    text = capital + text[1:]
if text[-1] == ".":
    text = text
    else:
    text = text + "."
    return text
```

### Great Answer

```python
def correct_sentence(text: str) -> str:   
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
```

```python
def correct_sentence(text :str) -> str:
    if text[-1] != '.':
        text = text + '.'
    return text.replace(text[0], text[0].upper(), 1)
```

```python
def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text
```

## 문장에서 첫 단어

### My Answer

```python
def first_word(text: str) -> str:
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.split()
    return text[0]
```

### Great Answer

```python
import re # 정규 표현식을 지원하기 위한 re(regular expression의 약어) 모듈
def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)
```

```python
def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').strip()
    return text.split()[0]
```

```python
first_word = lambda text: text.replace(',', ' ').replace('.', ' ').split()[0]
# lambda는 익명함수이다.
```

## 두번째 글자 index

### My Answer

```python
def second_index(text: str, symbol: str) -> [int, None]:
    symbol_count = text.count(symbol)
    if symbol_count >= 2:
        first = text.find(symbol)
        return text.find(symbol, first + 1)
    else:
        return None
```

### Great Answer

```python
def second_index(text: str, symbol: str) -> [int, None]:
    if symbol_count < 2:
        return None
    first = text.find(symbol)
    return text.find(symbol, first +1)
```

```python
def second_index(text: str, symbol: str) -> [int, None]:
    try:
        return text.index(symbol, (text.index(symbol)+1))
    except ValueError:
        return None
```

```python
def second_index(text, char):
    count = 0
    for i, c in enumerate(text):
        if c == char:
            count = count + 1
            if count == 2:
                return i
    return None
‘’’
enumerate는 "열거하다"라는 뜻. 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로, 
인덱스 값을 포함하는 enumerate 객체를 리턴. enumerate 함수는 for문과 함께 자주 사용.
‘’’
```

```python
def second_index(text: str, symbol: str):
    num = text.find(symbol, text.find(symbol)+1)
    return num if num>-1 else None
```

## Between Marker

### My Answer

```python
def between_markers(text: str, begin: str, end: str) -> str:
    try:
        begin_index = text.index(begin) + len(begin)
    except ValueError:
        begin_index = 0
    try:
        end_index = text.index(end)
    except ValueError:
        end_index = len(text)
    return text[begin_index:end_index]
```

### Great Answer

```python
def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]
```

```python
def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0
    if end in text:
        end_index = text.find(end)
    else:
        end_index = len(text)
    return text[begin_index:end_index]
```

## 수치값 비교하여 키값 호출

### My Answer

```python
def best_stock(data):
    max_price = 0
    answer = ""
    for k in data:
        if data[k] > max_price:
            max_price = data[k]
            answer = k
    return answer
```

### Great Answer

```python
def best_stock(data):
    return max(data, key=data.__getitem__)
```

```python
def best_stock(data):
    return max(data, key=data.get)
```

```python
def best_stock(data):
    return max(data, key=lambda x: data[x])
```

## 문장 내 글자 세기

### My Answer

```python
def popular_words(text: str, words: list) -> dict:
    text_list = text.split()
    lower_text_list = list(map(lambda x: x.lower(), text_list))
count_word_dict = {}
    for word in words:
        count_word_dict[word] = lower_text_list.count(word)
    return count_word_dict
```

### Great Answer

```python
def popular_words(text, words):
    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}
```

```python
def popular_words(text, words):
    return dict(zip(words, map(text.lower().split().count, words)))
```

```python
def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    splitted_words = text.split()
    answer = {}
    for word in words:
        answer[word] = splitted_words.count(word)
    return answer
```

## dict 큰 값 순서로 정렬

### Answer

```python
def bigger_price(limit, data):
    return sorted(data, key=lambda x: x['price'], reverse = True)[:limit]
```

## 나눗셈 가르치기

### My Answer

```python
def checkio(number: int) -> str:
    if number % 3 == 0:
        if number % 5 == 0:
            return "Fizz Buzz"
        else:
            return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
```

### Great Answer

```python
def checkio(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return str(number)
```

```python
def checkio(number):
    return 'Fizz' * (not number % 3) + ' ' * (not number % 15) + 'Buzz' * (not number % 5) or str(number)
```

```python
def checkio(number):
    d3 = number % 3 == 0
    d5 = number % 5 == 0
    if d3 and d5:
        return "Fizz Buzz"
    elif d3:
        return "Fizz"
    elif d5:
        return "Buzz"    
    return str(number)
```

```python
def checkio(number):
    return {
        (True, True): "Fizz Buzz",
        (True, False): "Fizz",
        (False, True): "Buzz",
        (False, False): str(number),
    }[not number % 3, not number % 5]
```

## 큰 수와 작은 수 차이

### My Answer

```python
def checkio(*args):
	if args:
    	return max(args) - min(args)
	else:
    	return 0
```

### Great Answer

```python
def checkio(*args):
    return max(args) - min(args) if args else 0
```

```python
def checkio(*args):
    return args and max(args) - min(args) or 0
```

```python
def checkio(*args):
    return max(args, default=0) - min(args, default=0)
```

## 리스트 인덱스가 짝수

### My Answer

```python
def checkio(array):
    if array:
        even_sum = 0
        x = 0
        while x < len(array):
            even_sum += array[x]
            x += 2
        answer = even_sum * array[-1]
        return answer
    else:
        return 0
```

### Great Answer

```python
def checkio(array):
    if not array:
        return 0
    return sum(array[::2]) * array[-1]
```

```python
def checkio(array):
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]
```

```python
checkio = lambda x: sum(x[::2]) * x[-1] if x else 0
```

```python
def checkio(array):
    return sum(array[::2]) * array[-1] if array else 0
```

## 문장에서 대문자

### My Answer

```python
from string import ascii_uppercase
def find_message(text: str) -> str:
    caps = ""
    for alpha in text:
        if alpha in ascii_uppercase:
            caps += alpha
    return caps
```

### Great Answer

```python
find_message = lambda text: ''.join(filter(str.isupper, text))
```

```python
def find_message(text):
    return ''.join(cap for cap in text if cap.isupper())
```

## 세 개의 연속된 숫자

### My Answer

```python
def checkio(words: str) -> bool:
    count = 0
    for word in words.split():
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False
```

### Great Answer

```python
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
```

```python
import re
def checkio(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))
'''
([a-zA-Z]+ ){2} means this ([a-zA-Z]+ ) twice.

‘+’ is equals {1,} that means it needs to have more than one.

than '([a-zA-Z]+ ){2}[a-zA-Z]+’ is same as '[a-zA-Z]{1,} [a-zA-Z]{1,} [a-zA-Z]{1,}’.it’s means it will only match when have a string with a sequence of 3 letter separated by space
'''
```

```python
import re

def checkio(words):
    return bool(re.search('\D+ \D+ \D+', words))
```

## 인덱스가 지수로

### My Answer

```python
def index_power(array: list, n: int) -> int:
    if not len(array) < n + 1:
        return array[n] ** n
    else:
        return -1
```

### Great Answer

```python
def index_power(array, n):
    try: return array[n] ** n
    except IndexError: return -1
```

```python
def index_power(array, n):
    return array[n] ** n if n < len(array) else -1
```

## Right to Left

### My Answer

```python
def left_join(phrases):
    spoken_words = ""
    
    for phrase in phrases:
        phrase = phrase.replace("right", "left")
        spoken_words += phrase + ","

    return spoken_words[:-1]
```

### Great Answer



## 각 자리수 곱하기

### My Answer

```python
def checkio(number: int) -> int:
    
    result = 1
    number_str = str(number)
    
    for n in number_str:
        if int(n) != 0:
            result *= int(n)
            
    return result
```

### Great Answer



## 십진법으로 전환

### My Answer

```python
def checkio(str_number: str, radix: int) -> int:
    try:
        convert = int(str_number, radix)
        return convert
    except ValueError:
        return -1
```

### Great Answer



## 절대값으로 정렬

### My Answer

```python
def checkio(numbers_array: tuple) -> list:
    abs_sorted_numbers_array = sorted(numbers_array, key = lambda x: abs(x))
    return abs_sorted_numbers_array
```

### Great Answer

```python

```



## 가장 많이 나온 값 찾기

### My Answer

```python
def most_frequent(data: list) -> str:
    
    max_count = None
    non_redup_data = list(set(data))

    for x in non_redup_data:
        count = data.count(x)
        if max_count == None or count > max_count:
            max_count = count
            frequent_word = x
            
    return frequent_word
```

### Great Answer

```python

```



## 튜플 인덱스 활용

### My Answer

```python
def easy_unpack(elements: tuple) -> tuple:
    return (elements[0], elements[2], elements[-2])
```

### Great Answer

```python

```

