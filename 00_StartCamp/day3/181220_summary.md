# 12. 20. 수업 정리

* (HTML) 모든 태그는 "의미"가 있다.
  * 왕국에서 기사에게 주는 작위와 같다.
  * 예를 들어 h1, ul, ol 등은 역할이다.
  * 과거에는 div로"만" 설정하였다.
  * 그러므로 "형태"보다 "의미"가 중요하다.
  * 즉, 각 태그에 대해 사용자가 설정을 바꿀 수 있다.
* conventional(지켜야 할 사항)과 refactoring(코드를 짜임새 있게)
* 인자와 리턴
  * yes in yes out
  * yes in no out
  * no in yes out
  * no in no out
* print와 return
  * 함수에서는 return으로 기입하자.
  * print는 디버깅용이다.

## sets

unordered collection

```python
list = [1, 2, 3]
tuple = (1, 2, 3)
set = {1, 2, 3}
```

## return

```python
>>> a = sorted([3, 2, 1])
>>> b = [3, 2, 1].sort()
>>> print(a, b)
[1, 2, 3] None
```

## import

import"만" 하면 파일 전체를 불러옴.

그러므로 from ~ import 구문을 사용하자.

## "__"

main 함수가 없으므로, 객체로 구현

```python
print(__name__)

def main():
    return "__에 대하여 알아보자."

if __name__ == '__main__':
    main()

def average(numbers):
    return sum(numbers) / len(numbers)

def cube(x):
    return x ** 3

__main__
```

```python
print(__name__)

# import math_functions
# math_functions.average([1, 2, 3])
# math_functions.cube(4)

from math_functions import average, cube

print(average([1, 2, 3]))
print(cube(4))

__main__
math_functions
2.0
64
```

##  cloud9

sudo ~ : 경고 무시

ctrl + c : cancle

$, >, % : prompt

flask run -h 0.0.0.0 -p 8080

export FLASK_ENV=development => 수정할 때마다 컴파일 과정 생략

```python
from flask import Flask, jsonify
from random import sample

# Flask 클래스 초기화 및 app 객체 만들기
app = Flask(__name__)

# "/"가 있는 것을 인덱스 화면이다.
@app.route("/")
def index():
    return "Happy Hacking"
    
@app.route("/hi")
def hi():
    return "Hello SSAFY"
    
@app.route("/pick_lotto")
def pick_lotto():
    return jsonify(sample(range(1, 46), 6))
    
@app.route("/get_lotto")
def get_lotto():
    data = {
        "numbers" : [1, 2, 3, 4, 5, 6],
        "bonus" : 7
    }
    return jsonify(data)
```

