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