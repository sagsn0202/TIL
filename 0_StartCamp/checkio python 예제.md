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

